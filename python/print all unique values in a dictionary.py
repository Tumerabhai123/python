my_dict = {'roll_no': 26, 'marks': 90, 'age': 26, 'id': 800}
unique_values = []
for value in my_dict.values():
    if value not in unique_values:
        unique_values.append(value)
print("unique values:", unique_values)