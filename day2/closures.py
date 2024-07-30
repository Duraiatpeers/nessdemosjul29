
# value = 100
#
# def demo():
#     value = 1
#     value = value+1000
#     print(value)
#
# demo()
# print('Outside demo', value)
#
# value = 100
#
# def demo():
#     global value
#     value = value+1000
#     return value
#
# value = demo()
#
# def d1():
#     print(value)
#
# d1()

#Nested function
# def outer():
#     print('Outer function')
#
#     def inner():
#         print('Inner function')
#
#     inner()
#
# outer()


# msg = 'Inside outer function'
#
# def outer():
#     print(msg)
#
#     def inner():
#
#         print(msg)
#
#     inner()
#
# outer()




# def outer():
#     msg = 'Inside outer function'
#     print(msg)
#
#     def inner():
#         nonlocal msg
#         msg = 'Inside inner function'
#         print(msg)
#
#     inner()
#
# outer()

# msg = 'Inside outer function'
#
# def outer():
#     print(msg)
#
#     def inner():
#         nonlocal msg
#         msg = 'Inside inner function'
#         print(msg)
#
#     inner()
#
# outer()



# def say():
#     greeting = "Welcome"
#
#     def display():
#         print(greeting)
#
#     return display
#
# fn = say()
# fn()




def sum(func):
    def wrapper():
        value = func()
        return value+value
    return wrapper

def square(func):
    def wrapper():
        value = func()
        return value * value

    return wrapper


@sum
def fn1():
    return 10;

@square
def fn2():
    return 20;

# sumv = fn1()
# print(sumv)

# square(fn2)
# squarev = fn2()
# print(squarev)

# Function - that needs to be enhanced
#     - Pass this function to the another function, enhance it and send back the new function
#
# Execute the original function that is decorated with the enhanced feature



def dec(*args):
    print('inside dec')

    def inner(func):
        print(args[0])
        return func
    return inner

@dec('ness demos')
def demo_fn():
    return 0

demo_fn()
