'''
a = -3
if a >0 :
    print("positive")
elif a<:
    print("negative")
else: 
    print("zero")
'''

height = float(input('키(m)를 입력해 주세요:'))*0.01
weight = float(input('몸무게를 입력해 주세요:'))
BMI = weight/height**2

if BMI >= 25:
    print ("당신은 비만입니다.")
elif 23<= BMI:
    print ("당신은 과체중입니다.")
elif 18.5<= BMI:
    print ("당신은 정상입니다.")
else :
    print ("당신은 저체중입니다.")
    