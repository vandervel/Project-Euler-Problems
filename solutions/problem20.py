# Sum of the digits of the number 100!

def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return n
    return n * factorial(n-1)
  
  
digit = factorial(100)
str_digit = str(digit)

d_sum = 0

for i in str_digit:
    d_sum += int(i)

print(d_sum)
    
