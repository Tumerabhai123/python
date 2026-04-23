m1 = float(input("enter marks: "))
m2 = float(input("      : "))
m3 = float(input("      : "))
m4 = float(input("      : "))
m5 = float(input("      : "))
total = m1 + m2 + m3 + m4 + m5
avg = total / 5
if avg >= 90:
    print("grade A")
elif avg >= 80:
    print("grade B")
elif avg >= 70:
    print("grade C")
elif avg >= 60:
    print("grade D")
elif avg >= 50:
    print("grade E")
else:
    print("fail")