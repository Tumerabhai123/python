num = int(input("enter number: "))
original = num
reversed = 0
while num > 0:
    digit = num % 10
    reversed = digit + reversed * 10
    num //= 10
print(f"original: {original}")
print(f"reversed: {reversed}")