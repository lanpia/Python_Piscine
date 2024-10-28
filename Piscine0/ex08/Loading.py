import sys
import time
import shutil

def ft_tqdm(iterable):
	"""
Decorate an iterable object, returning an iterator which acts exactly
like the original iterable, but prints a dynamically updating
progressbar every time a value is requested.

Parameters
----------
iterable  : iterable, optional
	Iterable to decorate with a progressbar.
	Leave blank to manually manage the updates.
desc  : str, optional
	Prefix for the progressbar.
total  : int or float, optional
	The number of expected iterations. If unspecified,
	len(iterable) is used if possible. If float("inf") or as a last
	resort, only basic progress statistics are displayed
	(no ETA, no progressbar).
	If `gui` is True and this parameter needs subsequent updating,
	specify an initial arbitrary large positive number,
	e.g. 9e9.
leave  : bool, optional
	If [default: True], keeps all traces of the progressbar
	upon termination of iteration.
	If `None`, will leave only if `position` is `0`.
file  : `io.TextIOWrapper` or `io.StringIO`, optional
...
Returns
-------
out  : decorated iterator.

	"""
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
