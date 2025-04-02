# ex_45.py 
# ex_41.py 응용
import math
def mean(l):
    S =0
    for x_k in l :
        S += x_k
    N = len(l)
    M = S / N

    return M

def std(l):
    m = mean(l)
    # S=0
    # for x_k in l :
    #     S += (x_k -m)**2
    # var = S/ len(l)
    var = mean([(x_k -m)**2 for x_k in l])
    sigma= math.sqrt(var)
    return sigma

# l = [1,2,3,4,5,6,7,8]
# print(std(l))


#########################모듈화 하기위해서 추가 
if __name__ == '__main__' :
    print("Test code")
    L = [1,2,3,4,5,6,7,8]
    print(std(L))