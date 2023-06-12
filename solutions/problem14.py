# Find the starting number for a Collatz sequence that produces the longest chain.


def collatz_sequence(start):
    
    counter = 1
    while start != 1:
        
        if start % 2 == 0:
            
            start = start/2
            
        else:
            
            start = 3*start + 1
            
            
        counter += 1
    return counter
  
  
max_length = 0
max_start = 0

for i in range(2, 1000000):
    
    length = collatz_sequence(i)
    
    if length > max_length:
        
        max_length = length
        
        max_start = i
        
print(max_start)
