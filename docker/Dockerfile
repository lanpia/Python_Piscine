# 베이스 이미지로 Python 3.10을 사용
FROM python:3.10-slim

# 컨테이너 내 작업 디렉토리를 설정
WORKDIR /app

# 필요 패키지 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Python 패키지 설치를 위한 requirements.txt 파일 작성
COPY requirements.txt .

# Python 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 기본 명령어
CMD ["python3"]
