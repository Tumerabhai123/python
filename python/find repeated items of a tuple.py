tuple = [34, 56, 56, 34, 69, 28, 88, 11, 11]
repeated = []
for item in tuple:
    if tuple.count(item) > 1 and item not in repeated:
        repeated.append(item)
print("repeated items: ", repeated)