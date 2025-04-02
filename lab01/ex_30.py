# ex_30.py 다음 모양의 별을 출력해보기
#     *     1
#    ***    3
#   *****   5
#  *******  7
# ********* 9



n = 5
for i in range(n):
    for j in range(n-i-1):
        print(' ',end='')
    for h in range(2*i+1):
        print('*',end='')
    print()

'''
n = 6
S = '*'
B = ' '
for i in range(n):
    print(f"{B*(n-i-1)}{S*(1+2*i)}{B*(n-i-1)}")
'''
'''
# 가운데 정렬 방법
n = 6
S = '*'
B = ' '
for i in range(n):
    print(f"{S*(1+2*i):^{2*n-1}}")
'''





