# ex_34.py 리스트 합계 구하기
# 정수들을 담은 nums리스트가 있다.
# numbers=[10,4,5,-1,6,12,40]
# 짝수 번째 원소들의 합계를 구하기

'''
numbers=[10,4,5,-1,6,12,40]
total = 0
for j in range(round(len(numbers)/2)):
    numbers[2*j] = 0
print(numbers)
for i in numbers :
    total += i

print(total)
'''
# numbers=[10,4,5,-1,6,12,40]
# total=0
# for i in numbers[1::2] : 
#     total += int(i)
# print(total)


# 최대 최솟값 도출하기
numbers=[10,4,5,-1,6,12,40]
total=0
max = numbers[0]
min = numbers[0]
for i in numbers :
    if max<=i :
        max = i
    if min > i :
        min = i
print('max :',max)
print('min :',min)