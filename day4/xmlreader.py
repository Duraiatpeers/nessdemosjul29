from xml.dom import minidom


file_reader = minidom.parse("data.xml")
model_list = file_reader.getElementsByTagName("model")

print(model_list)
print(model_list[0].attributes['name'].value)
print(model_list[1].attributes['name'].value)