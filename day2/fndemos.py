# Function with no arg
def add():
    print(' Add function ')

add()

# Function with 2 args
def add(number1,number2):
    print(f'sum of {number1} and {number2} is {number1+number2}')

add(20,30)

# Function with 1 arg
def textlength(sentence):
    return len(sentence)

lengthoftext = textlength("Welcome to Python programming")
print(lengthoftext)

# Function with arbitary args
def dummyfn(*args):
    print(len(args))

dummyfn(10,20)
dummyfn(10,20,30,40)

# Function with default value
def sumofnumbers(num1,num2=0):
    print(num1+num2)

sumofnumbers(10,20)

# function with arbitrary keyword arguments
def new_fn(**kwargs):
    print(kwargs['firstname'])
    print(kwargs['lastname'])

new_fn(firstname='Chris', lastname='Evert')

marks = [90,98,96,94,100]

def avg_calc(marklist):
    print(sum(marklist)/len(marklist))

avg_calc(marks)


def greet():
    print("Good Morning")

def welcome(greetfn):
    print('Inside welcome')
    greetfn()

welcome(greet)