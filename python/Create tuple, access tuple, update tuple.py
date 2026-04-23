tuple1 = (10, "Aarya", 40.34, 2345.6789)
tuple2 = (56.56, "Omkar", 67)
for item in tuple1:
    print(item)
print("updating list:")
list1 = list(tuple1)
list1[1] = "Atharva"
tuple1_new = tuple(list1)
print(tuple1_new)
del tuple1
print("deleted the entire tuple")