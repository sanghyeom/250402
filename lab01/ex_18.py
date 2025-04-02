# ex_18.py 입력한숫자를 0으로 만들기
# 사용자로부터 숫자를 입력 받고, 
# 그 숫자가 0이 될대까지 while 루프를 반복하고
# 반복 번수를 출력한다.

number = int(input("임의의 정수를 입력해주세요"))
count = 0
while number > 0 :
    print(number)
    number -= 1
    count += 1
    if number == 0 :
        print("0")
        print(f"{count}번 반복되었습니다.")
        break