
# Sum of squares: sum of first n squared natural numbers
# Difference between the sum of squares of first one hundred natural numbers:

total = 0
num_sum = 0

for i in range(1, 101):
    num_sum += i
    
for i in range(1, 101):
    square = i ** 2
    total += square
    
sum_square = num_sum ** 2

print(sum_square - total)
