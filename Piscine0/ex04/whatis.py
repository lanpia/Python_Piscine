import sys

def check_odd_or_even():
	# assert len(sys.argv) == 2, "argument is not an integer"
	# assert len(sys.argv) <= 2, "more than one argument is provided"
    try:
        if len(sys.argv) < 2:
            raise AssertionError("argument is not an integer")
        elif len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        num = int(sys.argv[1])
        if num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except ValueError:
        print("AssertionError: argument is not an integer")

if __name__ == "__main__":
    check_odd_or_even()
