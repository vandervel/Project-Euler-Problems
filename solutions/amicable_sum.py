# Find the sum of all amicable numbers under 1000
# Amicable numbers: If d(n) is the sum of all divisors of n, then 
# two integers a and b are an amicable pair if d(a) = b and d(b) = a, and a != b. 

def sum_div(n):
    
    total = 1
    for x in range(2, int(math.sqrt(n) + 1)):
        if n % x == 0:
            total += x
            y = n // x
            if y > x:
                total += y
    return total

def amicable_numbers(limit):
    for a in range(limit):
        b = sum_div(a)
        if a != b and sum_div(b) == a:
            yield a

print(sum(amicable_numbers(10000)))
