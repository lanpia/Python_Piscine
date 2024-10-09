import sys

def check_odd_or_even():
		# 인자가 하나인지 확인
		if len(sys.argv) != 2:
				raise AssertionError("more than one argument is provided" \
														if len(sys.argv) > 2 \
														else "argument is not an integer")

		try:
				# 문자열을 정수로 변환 시도
				num = int(sys.argv[1])
		except ValueError:
				# 정수로 변환할 수 없는 경우
				raise AssertionError("argument is not an integer")

		# 홀수, 짝수 여부 확인
		if num % 2 == 0:
				print("I'm Even.")
		else:
				print("I'm Odd.")

if __name__ == "__main__":
		check_odd_or_even()
