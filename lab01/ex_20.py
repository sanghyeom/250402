# ex_20.py 3의배수 출력
# - 100보다 작은 3의 배수를출력하세요.

'''
number =  0
while number < 100 :
    print(number)
    number += 3
'''

for i in range(0,100,3):
    print(i)
    if i >= 100 :
        break