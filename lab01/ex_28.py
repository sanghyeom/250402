# ex_28.py 

'''
#선생님예제 별 5개 5줄로 찍기,
for i in range(5):
    for j in range(5):
        print('*',end='')
    print()
'''

#선생님예제 응용,(이중 루프 연습)
n = 5
for i in range(n):
    for j in range(i+1):
        print('*',end='')
    print()


'''
#그냥 선생님예시 안보고 생각나는대로 구현해보기
i = '*'
for number in range(1,6):
    print(f"{i*number}")
'''