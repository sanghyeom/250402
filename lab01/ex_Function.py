# # ex_func.py

# def dummy():
#     print("i am a dummy function.")

# dummy()

# def dummy2() :
#     print("i am a dummy function.2")
#     return 10
# dummy2()
# print(dummy2())
# i = dummy2()
# def add(a,b):
#     C = a+b
#     print(C)

# add(1,3)
x = 'global'
def print_x():
    print(x)
    x = 'local'
    print(x)

print_x()
print(x)