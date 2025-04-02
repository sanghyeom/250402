#

def outer_func(msg):
    def inner_func():
        # print(f"메세지:{msg}")
        print("메세지")
    return inner_func

closure = outer_func("니하오")

closure = outer_func("니하오2")
closure()