# Find index of first Fibonacci number to contain a thousand digits

fib_numbers = []
a = 0
b = 1
while len(str(a)) < 1000:
    a , b = b , a + b
    fib_numbers.append(a)
    


print(fib_numbers.index(fib_numbers[-1])+ 1)
