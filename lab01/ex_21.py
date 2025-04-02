# ex_21.py 구구단 출력 프로그램
# - 사용자로부터 단수를 입력받고, 해당하는단의 구구단 테이블을 출력

number =int(input("궁금한 구구단을 정수로 입력해주세요. : "))
for i in range(1,10):
    print(f"{number} x {i} = {number * i}")
    if i == 10 :
        break