# 변수 정의
IMAGE_NAME = python-env
TAG = 3.10

# 도커 이미지 빌드
all:
	docker build -t $(IMAGE_NAME):$(TAG) . && \
	docker run -it --name $(IMAGE_NAME)-container $(IMAGE_NAME):$(TAG)

# 도커 이미지 제거
clean:
	docker rmi -f $(IMAGE_NAME):$(TAG) && \
	docker system prune -f && \
	docker rm -f $(IMAGE_NAME)-container
