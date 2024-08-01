
def demo():
    print('first msg')
    msg = 'Welcome'
    yield msg

    print('second msg')
    yield
    print('third msg')
    yield

# returns generator object
print(demo())
gen = demo()

print(next(gen))
next(gen)
next(gen)

even_numbers = [2,4,6,8,10]
print(type(even_numbers))

square_of_even_numbers = [x * x for x in even_numbers ]
print(type(square_of_even_numbers))
print(square_of_even_numbers)

gen_square_of_even_numbers = (x * x for x in even_numbers)
print(type(gen_square_of_even_numbers))
print(gen_square_of_even_numbers)
print(next(gen_square_of_even_numbers))
print(next(gen_square_of_even_numbers))
print(next(gen_square_of_even_numbers))








