import json

data_file = open("data.json")
data = data_file.read()

py_data = json.loads(data)

print(type(py_data))
print(type(py_data[0]))
print(py_data[0]["empname"])
print(py_data[0]["salary"])

print(py_data[1]["empname"])
print(py_data[1]["salary"])

browserdata = {
    "browsername":"chrome",
    "version":"128",
    "headless": False
}

print(type(browserdata))

newdata = json.dumps(browserdata)
print(type(newdata))
print(newdata)