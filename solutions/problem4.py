# Largest palindrome product of two 3-digit numbers


from itertools import permutations

def is_palindrome(n):
    
    
    n_str = str(n)
    length = len(n_str)
    half_length = int(len(n_str)/2)
    
    for i in range(0, length):
        
        if n_str[i] != n_str[length-i-1]:
            
            return False
        
    return True
    
    
max_palindrome = 0
num1 = 0
num2 = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        
        product = i * j
        if is_palindrome(product) and product > max_palindrome:
                num1 = i
                num2 = j
                max_palindrome = product
                

print(max_palindrome)
print(num1, num2)
