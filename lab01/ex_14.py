r = float(input('원의 반지름을 입력하세요:'))
pi = 3.1416
area = pi*r**2
cir = 2*r*pi
dia = 2*r
print(f"반지름이 {r}인 원의면적은 {area:0.4}입니다\n 이 원의 둘레는 {cir:0.4}입니다.\n 이 원의 지름은 {dia}입니다.")
