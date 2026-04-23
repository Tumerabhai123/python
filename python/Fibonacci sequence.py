
terms = 10
a = 0
b = 1
print("Fibonacci sequence:")
for _ in range(terms):
    print(a)
    
    # Calculate the next number
    next_number = a + b
    
  
    a = b
    b = next_number