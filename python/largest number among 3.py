a = int(input("enter number: "))
b = int(input("      : "))
c = int(input("      : "))
if a > b and a > c:
    print(f"{a} is the greatest")
elif b > a and b > c:
    print(f"{b} is the greatest")
else:
    print(f"{c} is the greatest")