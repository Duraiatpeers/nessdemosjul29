class Counter:

    def __iter__(self):
        self.value=1
        return self

    def __next__(self):
        new_value = self.value
        self.value +=1
        return new_value

counter = Counter()
mycounter = iter(counter)

print(next(mycounter))
print(next(mycounter))
print(next(mycounter))
print(next(mycounter))



