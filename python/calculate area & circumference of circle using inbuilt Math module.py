import math
def calculate(r):
    area = math.pi * r * r
    circumference = 2 * math.pi * r
    print("area:", round(area, 4))
    print("circumference:", round(circumference, 4))

r = float(input("enter radius: "))
calculate(r)