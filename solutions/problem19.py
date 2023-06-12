# Number of sundays that landed on the first of the month in the twentieth century.


months = [31,
         28,
         31,
         30,
         31,
         30,
         31,
         31,
         30,
        31,
         30,
        31]


def count_sundays():
    
    day = 1
    sunday_count = 0
    
    for i in range(1901, 2001):
        
        for j in months:
            
            day += j
            if day % 4 == 0:
                day += 1
            if day % 7 == 0:
                sunday_count += 1
                
    return sunday_count

print(count_sundays())
                
