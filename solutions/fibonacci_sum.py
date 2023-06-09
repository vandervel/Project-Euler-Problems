# Sum of even-valued fibonacci numbers less than or equal to 4 million

def fibonacci(n):
    
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
        
total = 0

for i in range(34):
    f = fibonacci(i)
    
    if f % 2 == 0:
        
        total = total + f
        
print(total)
