# ex_42.py 평균 구하는 함수와 컴프리헨션
# ex_38에서 만든 함수를 숫자로 채워진 리스트 or 튜플을 
# 입력받아 평균을 구하는 함수를 다음 두 학급의 시험 점수를
# 저장한 2차원 리스트에 컴프리 헨션을 이용하여 적용하기
def mean(l):
    S =0
    for x_k in l :
        S += x_k
    N = len(l)
    M = S / N
    return M


X = [[78,80,95,55,67,43],[45,67,90,87,88,93]]
L = [round(mean(n),2) for n in X]
print(L)



# avg = mean([1,2,3,4,5])
# print(avg)