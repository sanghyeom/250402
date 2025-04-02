# ex_try.py 에러메세지 출력 변경
operations = {'+': lambda x, y: x + y,
              '-': lambda x, y: x - y,
              '*': lambda x, y: x * y,
              '/': lambda x, y: x / y #if y != 0 else "오류: 0으로 나눌 수 없습니다"
              }
# number1 = float(input('첫 번째 숫자를 입력해 주세요:'))
# number2 = float(input('두 번째 숫자를 입력해 주세요:'))
# cal = input('연산자를 입력하세요 (+, -, *, /): ')
# print(f"{number1} {cal} {number2} = {operations[cal](number1,number2)}")
# #####################################3
# number1 = float(input('첫 번째 숫자를 입력해 주세요:'))
# number2 = float(input('두 번째 숫자를 입력해 주세요:'))
# cal = input('연산자를 입력하세요 (+, -, *, /): ')
# if cal in operations.keys() :
#     result = print(f"{number1} {cal} {number2} = {operations[cal](number1,number2)}")
#     print(result)
# else :
#     print("올바른 연산이 아닙니다.")
######################################
try:
    number1 = float(input('첫 번째 숫자를 입력해 주세요:'))
    number2 = float(input('두 번째 숫자를 입력해 주세요:'))
    cal = input('연산자를 입력하세요 (+, -, *, /): ')
    result = operations[cal](number1,number2)
    print(result)
    
except KeyError as e:
    print("알수없는 에러 1.")
except ValueError as e : 
    print("알수없는 에러 2.")
except ZeroDivisionError as e:
    print("알수없는 에러3.")
    print(e)
finally : 
    print("프로그램이 종료되었습니다.")

    