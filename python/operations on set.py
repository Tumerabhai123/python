A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("original sets:", A, B)
intersect = A & B
print("intersection:", intersect)
union = A | B
print("Union:", union)
difference = A - B
print("Difference:", difference)
symmetric_difference = A ^ B
print("symmetric difference:", symmetric_difference)
print("In Set A & B before clear:", A, B)
A.clear()
B.clear()
print("set A & B after clear:", A, B)