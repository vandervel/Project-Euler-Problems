# Sum of primes below 2 million


def eratosthenes(n):
    
    total = 0
    
    if n <= 1:
        print("n must be greater than 1")
        return
    
    primes = [True for i in range(n+1)]
    p = 2
    
    while(p <= math.sqrt(n)):
        
        if(primes[p] == True):
            
            for i in range(p**2, n+1, p):
                
                primes[i] = False
        p += 1
        
    primes[0] = False
    primes[1] = False
    
    for p in range(n + 1):
        if primes[p]:
            total += p
    
    print(total)
        

    

eratosthenes(2000000)
