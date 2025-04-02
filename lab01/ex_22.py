# ex_22.py 1에서 n까지의 합
# 사용자에게 임의의 자연수 n을 입력받고, 1에서 n까지 모두 합산하는 프로그램


number =int(input("임의의 자연수를 입력해주세요. : "))
count = 0
for i in range(1,number+1):
    count += i

print(f"1부터{number}까지의 합은{count}입니다.")