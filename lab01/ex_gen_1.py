#

def get_number_generator(n):
    for i in range(n):
        print("before")
        yield i
        print("after")

# number = get_number_generator(3)
# print(next(number,'end'))
# print()

# print(next(number,'end'))
# print()

# print(next(number,'end'))
# print()
# ######################
# g = get_number_generator(10)

# for i in g :
#     print(i)

def inf_number_gen():
    i=1
    F=[] =[]
    F[0]= 0
    F[1]= 1
    while True :
        yield i 
        i+=1
        F[i]=F[i-1]+F[i-1]


g = inf_number_gen()
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))