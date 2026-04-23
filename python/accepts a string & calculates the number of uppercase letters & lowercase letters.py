def calculate(text):
    uppercase = 0
    lowercase = 0
    for char in text:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
    print("uppercase letters:", uppercase)
    print("lowercase letters:", lowercase)

text = input("enter a string in uppercase and lowercase letters: ")
calculate(text)