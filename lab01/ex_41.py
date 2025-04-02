# ex_41.py 평균 구하는 함수
# 숫자로 채워진 리스트 또는 튜플을 입력 받아 평균을 구하는 함수
# def mean(l):
#     total=0
#     for i in range(len(l)) :
#         total += l[i] 
#     return total/len(l)


# avg = mean((1,2,3,4,5,6))
# print(avg)

def mean(l):
    S =0
    for x_k in l :
        S += x_k
    N = len(l)
    M = S / N

    return M

avg = mean((1,2,3,4,5,6))
print(avg)
