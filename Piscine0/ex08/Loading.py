import sys
import time
import shutil

def ft_tqdm(iterable):
	total = len(iterable)  # 전체 작업 수
	start_time = time.time()  # 시작 시간 기록

	# 터미널 너비 계산
	term_width = shutil.get_terminal_size().columns
	min_bar_length = 20  # 프로그레스 바의 최소 길이
	reserved_space = 35  # 진행 상태 문자열의 공간 (퍼센트, 인덱스, 시간 등)
	# 프로그레스 바 길이 설정
	bar_length = max(min_bar_length, term_width - reserved_space)
	for i, item in enumerate(iterable, 1):
		# 진행률 계산
		elapsed_time = time.time() - start_time
		progress = i / total
		filled_length = int(bar_length * progress)  # 채워진 부분 길이 계산
		bar = '=' * filled_length + '>' + ' ' * (bar_length - filled_length)
		# 진행 상태 출력 형식
		percent = int(progress * 100)
		sys.stdout.write(f"\r{percent}%|[{bar}]| {i}/{total} [{elapsed_time:.2f}s]")
		sys.stdout.flush()  # 출력 갱신
		# yield 현재 item
		yield item
	# 작업 완료 시 줄바꿈
	print()
