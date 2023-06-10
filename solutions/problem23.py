# Sum of all positive integers that cannot be written as sum
# of two abundant numbers 


def is_abundant(n):
    
    if sum(get_proper_divisors(n)) > n:
        return True
    return False

def get_proper_divisors(n):
    
    divisors = []
    
    for i in range(1, int(n/2)+1):
        
        if n % i == 0:
            divisors.append(i)
    return divisors     

  
abundants = []

for i in range(28123):
    if is_abundant(i):
        abundants.append(i)

        
        
sums = [0]*28124
num_abundants = len(abundants)

for x in range(0, num_abundants):
    for y in range(x, num_abundants):
        sum_of_2 = abundants[x] + abundants[y]
        if sum_of_2 <= 28123:
            if sums[sum_of_2] == 0:
                sums[sum_of_2] = sum_of_2

total = 0
for j in range(1, len(sums)):
    if(sums[j] == 0):
        total += j

print(total)
