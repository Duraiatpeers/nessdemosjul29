import os

# data_file = open("data.txt")
# # print(data_file.read())
#
# # print(data_file.readline())
# # print(data_file.readline())
#
# for line_text in data_file:
#     print(line_text)
#
# data_file.close()

# with open('data.txt','a') as data_file:
#     data_file.write("\nPython is used in Automation, AI/ML\n")

if(os.path.exists("data.txt")):
    with open('data.txt','r') as data_file:
        data_file.seek(10)
        print(data_file.read())
    # data_file.write("location:11")
else:
    print("Data file doesn't exist")

# os.remove("data.txt")
print(os.path.exists("data.txt"))

print(os.listdir())

#ValueError: I/O operation on closed file.
# for line_text in data_file:
#     print(line_text)


