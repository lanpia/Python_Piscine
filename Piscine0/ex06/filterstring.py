import sys
from ft_filter import ft_filter

def main():
	try:
		if len(sys.argv) != 3:
			raise AssertionError("The arguments are bad")
		if not sys.argv[2].isdigit():
			raise AssertionError("The arguments are bad")
		print(list(ft_filter(lambda x: len(x) > int(sys.argv[2]), sys.argv[1].split())))
	except AssertionError as e:
		print(f"AssertionError: {e}")

if __name__ == "__main__" :
	main()
