#
# def msg():
#     def inner_msg():
#         print("Welcome")
#     return inner_msg
#
# new_msg = msg()
# new_msg()

def add(a,b):
    print(a+b)


def more_add(fn):
    def inner_add(x,y):
        if x < 1000:
            x = x + 1000
        if y < 1000:
            y = y + 1000
        return fn(x,y)
    return inner_add

# sum1 = more_add(reduce_sum)
# sum1(100,200)



@more_add
def reduce_sum(a,b):
    print(a+b-10)

@more_add
def add(a,b):
    print(a+b)

reduce_sum(100,200)

add(100,200)