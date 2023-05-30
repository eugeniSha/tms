dict = {"key1": 1, "key2": 2, "key3": 3,}
new_dict = {v: k for k, v in dict.items()}
print(new_dict)