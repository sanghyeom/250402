# ex_27.py 모든 구구단 출력 프로그램
# 2단부터 9단까지 구구단을 출력하는 프로그램
# 각 단 사이에는 ---------- 같은 적당한 구분 문자를 출력한다.

line= '-'*20
for number in range(2,10):
    print(line)
    for i in range(1,10):
        print(f"{number} x {i} = {number * i}")
        if i == 9 :
            break
print(line)