# ex_35.py 행렬 덧셈
# for문을 중첩해서 두행렬의 덧셈을 수행하는 코드 만들기

A =[[1,0,1],
    [0,2,0],
    [1,2,1]]
B = [[2,3,1],
     [0,1,1],
     [1,1,1]]

C = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(A)):
    for j in range(len(A[i])):
        C[i][j] = A[i][j] + B[i][j]
        print(C[i][j])
print(C)