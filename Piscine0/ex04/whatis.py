import sys

# 첫 번째 인수는 항상 스크립트 이름입니다
script_name = sys.argv[0]

# 나머지 인수들
arguments = sys.argv[1:]

# 인수 출력
print(f"스크립트 이름: {script_name}")

if len(sys.argv) - 1 != 1:
	print("AssertionError: more than one argument is provided")
else :
      print((type(sys.argv[1])))
      if type(sys.argv) != int:
            print("AssertionError: argument is not an integer")
      else :
            print(f"argv: {enumerate(arguments, 1)}")