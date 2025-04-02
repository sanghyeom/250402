# ex_51.py 
import ex_45
s = input("평균을 구할 숫자를 입력하세요(콤마 또는 공백으로 구분): ")

# ##############################
# if s.count(',') == 0:
#     s.split(',')

#     # m=ex_45.mean(s)
#     # print(m)
# else :
#     print(s.split())
#     m=ex_45.mean(s)
#     print(m)
# ################################3
s=s.replace(',',' ')
L= s.split()
print(L)

L= [int(i) for i in s.replace(',',' ').split()]
print(ex_45.mean(L))