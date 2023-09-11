
# You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. Find the minimum number of swaps required to sort the array in ascending order.

# Example


# Perform the following steps:

# i   arr                         swap (indices)
# 0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
# 1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
# 2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
# 3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
# 4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
# 5   [1, 2, 3, 4, 5, 6, 7]
# It took  swaps to sort the array.

# Function Description

# Complete the function minimumSwaps in the editor below.

# minimumSwaps has the following parameter(s):

# int arr[n]: an unordered array of integers


arr = [] # dont need this, just to undo error 
swap = 0
x = 0
while x < len(arr):
    if arr[x] != x+1:
        position = arr.index(x+1)
        temp = arr[x]
        arr[x] = arr[position]
        arr[position] = temp
        swap += 1
    x += 1
print (swap)