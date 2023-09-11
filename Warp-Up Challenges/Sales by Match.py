
# There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

# Example


# There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

# Function Description

# Complete the sockMerchant function in the editor below.

# sockMerchant has the following parameter(s):

# int n: the number of socks in the pile
# int ar[n]: the colors of each sock
# Returns

# int: the number of pairs

def sockMerchant(n, ar):
    # Create a dictionary to count the frequency of each color
    color_count = {}
    for color in ar:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    # Count the number of pairs for each color and sum them up
    total_pairs = 0
    for count in color_count.values():
        total_pairs += count // 2

    return total_pairs