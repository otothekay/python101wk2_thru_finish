import numpy as np

### Problem 1
'''
a + b = 180
b = 5x - 22
b = 8x + 46
'''

left_side = np.array([[1,1,0],
                     [0,1,-5],
                     [0,1,-8]])
right_side = np.array([[180],
                      [-22],
                      [46]])
solution1 = np.linalg.solve(left_side,right_side)
print(solution1)

### Problem 2
'''
a + b = 180
a = 2x+1
b = 3x-31 
'''

left_side2 = np.array([[1,1,0],
                       [1,0,-2],
                       [0,1,-3]])
right_side2 = np.array([[180],
                       [1],
                       [-31]])
solution2 = np.linalg.solve(left_side2,right_side2)
print(solution2)

### Problem 3
'''
What is the difference between 
.dot() and @ in python's numpy math functions?

ANS: @ calls on a function called .matmul() while .dot() is its own function.  
Sometimes they produce the same answer, but other times they don't.  
I know the reason is math related but I don't understand the math
referenced in the documentation or why .matmul() broadcasts its arrays sometimes.
'''

