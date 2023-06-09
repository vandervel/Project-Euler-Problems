# Smallest number evenly divisible by integers 1 through 20.


import functools 

def gcd(a, b):
    
    return gcd(b, a%b) if b else a

def lcm(a, b):
    
    return b * (a/gcd(a, b))
    
    
print(functools.reduce(lcm, range(1, 21)))
