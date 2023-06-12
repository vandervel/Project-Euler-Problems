# Sum of the digits of the number 2^1000

num = 2**1000
str_num = str(num)
num_sum = 0

for i in str_num:
    
    num_sum += int(i)
    
print(num_sum)
    
