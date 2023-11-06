

def diagonalDifference(arr):
    right = 0
    left = 0
    length = len(arr[0])
    for i in range(length):
        num = arr[i][i]
        right += num

    for i in range(length):
        num = arr[i][length - 1 - i]
        left += num


    diff = abs(right - left)
    return diff

arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
diagonalDifference(arr)

