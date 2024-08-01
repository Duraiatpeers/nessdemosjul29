import csv

emp_data_file = open('data.csv')

file_reader = csv.reader(emp_data_file)

for data in file_reader:
    if(data[3] == 'hyderabad'):
        print(data)

