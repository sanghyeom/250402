# ex_39.py 리스트 컴프리헨션
# 1~20 까지 짝수만 포함하는 리스트 만들기
############################
# 컴프리헨션 (Comprehension)
# 리스트, 사전등에 적용가능
# 내포문법 [표현식 for 항목 순회가능객체 [if 조건]]
# Ex) L= [n for n in range(1,6) if n % 2 ==1] 
# L = []
# for n in range(1,6): 
#     if n % 2 == 1 :
#         L.append(n)
# print(L)
#

L = [n for n in range(1,21) if n % 2 == 0] 
print(L)