# First triangluar number to have over 500 divisors.


def get_factors(n):
    return sum(2 for i in range(1, round(math.sqrt(n)+1)) if not n % i)
  
  

def triangle_nums(limit):
    
    triangles = []
    
    for i in range(1, limit+1):
        
        triangles.append(int((i *(i + 1)) / 2))
        
    return triangles
  
  
for i in triangle_nums(100000):
    
    if get_factors(i) > 500:
        
        print(i)
        break
