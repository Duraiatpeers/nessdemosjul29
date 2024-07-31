def gendemo(marks):
    for mark in marks:
        yield mark


marks = [80,90,100,80,98]

gen = gendemo(marks)

print(gen)
print(next(gen))
print(next(gen))
print(next(gen))




