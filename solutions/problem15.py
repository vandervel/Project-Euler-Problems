# The number of lattice paths in a n x n grid is equal to 2n choose n. Thus, we can calculate
# the number of lattice paths in a 20 x 20 grid by calculating 2n choose n or 40 choose 20 as follows:

# define simple recursive function for generating the factorial of an integer n

def factorial(n):
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# define simple function to calculate the binomial coefficient for integers n and k

def binomial_coef(n, k):
    return factorial(n) / (factorial(k) * factorial(n-k))


# get answer, which is 137846528820
print(binomial_coef(40, 20))
