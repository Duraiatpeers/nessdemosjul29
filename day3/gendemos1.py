import sys

def gen_numbers(n):
    list1 = []
    for i in range(n):
            list1.append()
            yield list1

def gen_numbers_new(n):
    newlist = []
    for i in range(n):
        newlist.append(i)
    return newlist

print(sys.getsizeof(gen_numbers(1000000)))
print(sys.getsizeof(gen_numbers_new(1000000)))


