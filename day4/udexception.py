from day4.CounterError import CounterError

def count_words(input_text):
    word_count = 0
    try:
        if(input_text ==''):
            raise CounterError("Counter issue")
        else:
            word_count = len(input_text.split(' '))

    except CounterError as ce:
        print(ce)

    return word_count


print(count_words("Welcome to Python programming"))
print(count_words(""))

