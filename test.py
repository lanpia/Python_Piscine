import asyncio
import websockets
import json
import requests
import time
import hmac
import hashlib
import math
import ssl
from typing import Optional

API_KEY_RAW = "YOUR_API_KEY"
API_SECRET_RAW = "YOUR_API_SECRET"
API_KEY = API_KEY_RAW.encode('ascii', 'ignore').decode('ascii')
API_SECRET = API_SECRET_RAW.encode('ascii', 'ignore').decode('ascii')

SYMBOL = "ENAUSDT"
INITIAL_INVESTMENT_USDT = 100.0
ORDER_GAP = 0.005

while True:
    try:
        info = requests.get(
            "https://api.bybit.com/v5/market/instruments-info",
            params={"category": "linear", "symbol": SYMBOL},
            timeout=10
        ).json()["result"]["list"][0]
        QTY_STEP = float(info["lotSizeFilter"]["qtyStep"])
        TICK_SIZE = float(info["priceFilter"]["tickSize"])
        QTY_DECIMALS = int(-math.log10(QTY_STEP))
        PRICE_DECIMALS = int(-math.log10(TICK_SIZE))
        break
    except Exception:
        time.sleep(5)

def _sign(ts: str, rw: str, body: str) -> str:
    return hmac.new(API_SECRET.encode(), (ts + API_KEY + rw + body).encode(), hashlib.sha256).hexdigest()

class BybitPriceStreamer:
    def __init__(self, symbol: str = SYMBOL):
        self.symbol = symbol
        self.last_price: Optional[float] = None
        self.running = True
        self.ws = None

    async def connect(self):
        url = "wss://stream.bybit.com/v5/public/linear"
        ssl_context = ssl.create_default_context()
        try:
            async with websockets.connect(url, ssl=ssl_context) as ws:
                self.ws = ws
                await ws.send(json.dumps({"op": "subscribe", "args": [f"tickers.{self.symbol}"]}))
                while self.running:
                    try:
                        msg = await asyncio.wait_for(ws.recv(), timeout=5.0)
                        data = json.loads(msg)
                        if "data" in data and "lastPrice" in data["data"]:
                            self.last_price = float(data["data"]["lastPrice"])
                    except asyncio.TimeoutError:
                        continue
                    except asyncio.CancelledError:
                        break
        except GeneratorExit:
            print("[⚠️ GeneratorExit 감지됨 - 루프 종료]")
        except Exception as e:
            print(f"[⚠️ WebSocket 오류 발생] {e}")
        finally:
            if self.ws:
                try:
                    await self.ws.close()
                    await self.ws.wait_closed()  # ✅ 소켓 완전 종료 대기
                except Exception:
                    pass
            print("[ℹ️ WebSocket 정상 종료됨]")


    def stop(self):
        self.running = False

    def get_price(self) -> Optional[float]:
        return self.last_price

def send_order_to_bybit(order: dict) -> Optional[str]:
    url = "https://api.bybit.com/v5/order/create"
    ts, rw = str(int(time.time() * 1000)), "5000"
    price_for_qty = order["price"] if order["price"] is not None else order["trigger_price"]
    raw_qty = order["value"] / price_for_qty
    qty = math.floor(raw_qty / QTY_STEP) * QTY_STEP
    qty_str = f"{qty:.{QTY_DECIMALS}f}"

    price_str = None
    if order["price"] is not None:
        px = round(order["price"] / TICK_SIZE) * TICK_SIZE
        price_str = f"{px:.{PRICE_DECIMALS}f}"

    pos_idx = 1 if order["side"] == "Buy" else 2
    body = {
        "category": "linear", "symbol": order["symbol"],
        "side": order["side"], "orderType": "Limit",
        "qty": qty_str, "timeInForce": "GTC", "positionIdx": pos_idx
    }
    if price_str: body["price"] = price_str
    if "trigger_price" in order:
        tp = order["trigger_price"]
        body.update({
            "triggerPrice": f"{tp:.{PRICE_DECIMALS}f}",
            "triggerDirection": order["trigger_direction"],
            "triggerBy": "LastPrice"
        })
    if order.get("reduce_only", False):
        body["reduceOnly"] = True

    body_json = json.dumps(body, separators=(',', ':'))
    sig = _sign(ts, rw, body_json)
    headers = {
        "Content-Type": "application/json",
        "X-BAPI-API-KEY": API_KEY,
        "X-BAPI-TIMESTAMP": ts,
        "X-BAPI-SIGN": sig,
        "X-BAPI-RECV-WINDOW": rw
    }

    resp = requests.post(url, headers=headers, data=body_json, timeout=10).json()
    return resp.get("result", {}).get("orderId")

def cancel_order_bybit(order_id: str, symbol: str):
    url = "https://api.bybit.com/v5/order/cancel"
    ts, rw = str(int(time.time() * 1000)), "5000"
    body = {"category": "linear", "symbol": symbol, "orderId": order_id}
    body_json = json.dumps(body, separators=(',', ':'))
    sig = _sign(ts, rw, body_json)
    headers = {
        "Content-Type": "application/json",
        "X-BAPI-API-KEY": API_KEY,
        "X-BAPI-TIMESTAMP": ts,
        "X-BAPI-SIGN": sig,
        "X-BAPI-RECV-WINDOW": rw
    }
    requests.post(url, headers=headers, data=body_json, timeout=10)

def get_execution(order_id: str, symbol: str) -> Optional[float]:
    url = "https://api.bybit.com/v5/execution/list"
    ts, rw = str(int(time.time() * 1000)), "5000"
    params = {"category": "linear", "symbol": symbol, "orderId": order_id}
    query = "&".join(f"{k}={v}" for k, v in sorted(params.items()))
    sig = _sign(ts, rw, query)
    resp = requests.get(url, headers={
        "X-BAPI-API-KEY": API_KEY,
        "X-BAPI-TIMESTAMP": ts,
        "X-BAPI-SIGN": sig,
        "X-BAPI-RECV-WINDOW": rw
    }, params=params, timeout=10)
    try:
        data = resp.json()
    except:
        return None
    if data.get("retCode") != 0:
        return None
    lst = data.get("result", {}).get("list", [])
    return float(lst[0]["execPrice"]) if lst else None

async def run_auto_trade_with_realtime_monitoring():
    streamer = BybitPriceStreamer()
    stream_task = asyncio.create_task(streamer.connect())

    while streamer.get_price() is None:
        await asyncio.sleep(0.5)
    first_price = round(streamer.get_price() * (1 - ORDER_GAP), PRICE_DECIMALS)

    oid1 = send_order_to_bybit({"symbol": SYMBOL, "side": "Buy", "price": first_price, "value": INITIAL_INVESTMENT_USDT})
    if not oid1:
        streamer.stop()
        stream_task.cancel()
        return

    filled = False
    price_flage = True
    while not filled:
        current = streamer.get_price()
        if current is not None:
            pct = (current - first_price) / first_price * 100
            if current > first_price * 1.01:
                print("[🔄] +1%↑, 주문 취소 & 재발주")
                cancel_order_bybit(oid1, SYMBOL)
                first_price = round(current * (1 - ORDER_GAP), PRICE_DECIMALS)
                oid1 = send_order_to_bybit({"symbol": SYMBOL, "side": "Buy", "price": first_price, "value": INITIAL_INVESTMENT_USDT})

        if price_flage == True:
                print(f"[🕒 MONITOR] Current: {current:.{PRICE_DECIMALS}f} (Order: {first_price:.{PRICE_DECIMALS}f}, {pct:+.2f}%)")
        exec_price = get_execution(oid1, SYMBOL)
        if exec_price is not None:
            print(f"[✅ 1차 체결] Price: {exec_price}")
            filled = True
            price_flage = False
            break
        await asyncio.sleep(1)

    streamer.stop()
    stream_task.cancel()
    try:
        await stream_task
    except asyncio.CancelledError:
        pass
    except Exception as e:
        print(f"[⚠️ WebSocket 종료 오류] {e}")

    tp2 = round(exec_price * (1 - ORDER_GAP), PRICE_DECIMALS)
    oid2 = send_order_to_bybit({
        "symbol": SYMBOL, "side": "Sell", "price": None,
        "value": INITIAL_INVESTMENT_USDT,
        "trigger_price": tp2, "trigger_direction": 2
    })
    print(f"[STEP2] Trigger Sell sent at {tp2}, ID={oid2}")

if __name__ == "__main__":
    async def main():
        await run_auto_trade_with_realtime_monitoring()
        await asyncio.sleep(0.1)  # 조금 더 대기
        await asyncio.get_event_loop().shutdown_asyncgens()  # ✅ Task 정리

    try:
        asyncio.run(main())  # ✅ 안전한 run 방식
    except KeyboardInterrupt:
        print("🔴 사용자에 의해 중단됨")
