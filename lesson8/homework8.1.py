string = b'r\xc3\xa9sum\xc3\xa9'
print(string)
new_string = string.decode(encoding="utf-8")
print(new_string)
too_new_string = new_string.encode(encoding="Latin1")
print(type(too_new_string))
last_string = too_new_string.decode(encoding="Latin1")
print (last_string)