# ex_29.py 다음 모양의 별을 출력해보기
# *****
# ****
# ***
# **
# *


n = 5
for i in range(n):
    for j in range(n-i):
        print('*',end='')
    print()


'''
i = '*'
for number in range(6,1,-1):
    print(f"{i*number}")
'''