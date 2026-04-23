list1 = [12, 23, 24, 45]
list2 = [12, 67, 89, 34]
common = []
for item in list1:
    if item in list2:
        common.append(item)
print(common)