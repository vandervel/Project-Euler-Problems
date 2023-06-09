# Find product abc where a^2 + b^2 = c^2 and a + b + c = 1000


m = 2

limit = 1000
c = 0
while(c < limit):
    
    for n in range(1, m+1):
        
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
        
        if (a == 0 or b == 0 or c == 0):
            break
        
        
        if a + b + c == 1000:
            print(a)
            print(b)
            print(c)
            
            print(a * b * c)
            break
        
        
    m += 1
