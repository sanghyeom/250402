# ex_43.py 

def print_all(*args,**kwargs):
    print("positional argument tuple:",args)
    print("keyword argument dict:",kwargs)

print_all(1,2,3,4,x=10,y=20,c=300)
