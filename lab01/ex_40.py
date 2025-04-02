# ex_40.py 몫과 나머지 구하는 함수

# def dafsfads():
#     M=int(input("나눠질 수를 입력하세요: "))
#     N=int(input("나눌 수를 입력하세요: "))
#     A = int((M-M%N)/N)
# # print(A)
# print(f"({A}, {M % N})")


# def Qr(x,y):
#     x,y>0
#     q= x//y
#     r= x%y

#     return (q,r)

# x= 10
# y= 3
# ret= Qr(x,y)
# print (ret[0],ret[1])
x=int(input("나눠질 수를 입력하세요: "))
y=int(input("나눌 수를 입력하세요: "))
# def Qr(x,y):
#     Count = 0
#     if x>0 : 
#         if y>0 :
#             while x-y >= 0 :
#                 x -= y
#                 Count += 1
#             return Count,x
#         else:
#             return "y를 0보다 큰 숫자로 입력하세요."
#     else:
#         return "x를 0보다 큰 숫자로 입력하세요."
    
# print(Qr(x,y))



def Qr(x,y):
    Count = 0
    while x>0 and y>0 : 
        while x-y >= 0 :
            x -= y
            Count += 1
        return Count,x
    else:
        return "0보다 큰 숫자로 입력하세요."
print(Qr(x,y))