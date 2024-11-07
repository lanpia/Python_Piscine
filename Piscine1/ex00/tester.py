# tester.py 예시

from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15]
weight = [165.3, 38.4]

bmi = give_bmi(height, weight)
print(bmi, type(bmi))  # 출력: [22.507863455018317, 29.0359168241966] <class 'list'>
print(apply_limit(bmi, 26))  # 출력: [False, True]
