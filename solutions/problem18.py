
# Redefine the triangle in question as follows:
triangle = [
  [75],
  [95, 64],
  [17, 47, 82],
  [18, 35, 87, 10],
  [20, 4, 82, 47, 65],
  [19, 1, 23, 75, 3, 34],
  [88, 2, 77, 73, 7, 63, 67],
  [99, 65, 4, 28, 6, 16, 70, 92],
  [41, 41, 26, 56, 83, 40, 80, 70, 33],
  [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
  [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
  [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
  [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
  [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
  [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
]

# This defines the triangle as a 2 dimensional array, which will be is
# optimal for the iterations we need to conduct in our solution.


# Dynamic problem solution. The optimal solution is defined by the 
# recurrence OPT(i, j) which is the greatest possible sum of the path
# terminating at the i, jth element. After iterating through the triangle,
# the optimal solution is returned.
def find_solution(n):
    
    for i in range(len(n) - 2, -1, -1):
        for j in range(len(n[i])):
            n[i][j] += max(n[i+1][j], n[i+1][j+1])
    
    print(triangle)
    return n[0][0]

print(find_solution(triangle))
