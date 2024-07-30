# Map,filter,reduce
from functools import reduce

bonus = [100,200,300]

def doublecalc(bonus):
    return bonus*2

new_list = map(doublecalc,bonus)

print(new_list)

for val in new_list:
    print(val)

scores = [60,70,80,90,100]

# filtered_values = []
# for score in scores:
#     if(score > 75):
#         filtered_values.append(score)

# print(filtered_values)

filtered_values = filter(lambda score: score >= 75, scores)
print(list(filtered_values))



# scores = [60,70,80,90,100]
#
# total = 0
# for score in scores:
#     total += score
#
# print(total)

def sum(num1,num2):
    return num1+num2

# scores = [60,70,80,90,100]

total = reduce(sum,scores)
print(total)