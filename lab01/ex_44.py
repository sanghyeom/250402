# ex_44.py lambda 함수를 이요한 계산기 프로그램.
operations = {'+': lambda x, y: x + y,
              '-': lambda x, y: x - y,
              '*': lambda x, y: x * y,
              '/': lambda x, y: x / y if y != 0 else "오류: 0으로 나눌 수 없습니다"
              }
# number1 = float(input('첫 번째 숫자를 입력해 주세요:'))
# number2 = float(input('두 번째 숫자를 입력해 주세요:'))
# cal = input('연산자를 입력하세요 (+, -, *, /): ')
# print(f"{number1} {cal} {number2} = {operations[cal](number1,number2)}")
number1 = float(input('첫 번째 숫자를 입력해 주세요:'))
number2 = float(input('두 번째 숫자를 입력해 주세요:'))
cal = input('연산자를 입력하세요 (+, -, *, /): ')
if cal in operations.keys() :
    result = print(f"{number1} {cal} {number2} = {operations[cal](number1,number2)}")
    print(result)
else :
    print("올바른 연산이 아닙니다.")
