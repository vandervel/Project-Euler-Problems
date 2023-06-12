# 10001st prime number


def is_prime(n):
    if n > 1:
        
        for i in range(2, n):
            
            if n % i == 0:
                return False
        return True
    else: return False
    
    
prime_count = 0
counter = 0
while True:
    
    if is_prime(counter):
        
        prime_count += 1
        
    if prime_count == 10001:
        break
        
    counter += 1

print(counter)
