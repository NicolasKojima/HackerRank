# There is a string, , of lowercase English letters that is repeated infinitely many times. Given an integer, , find and print the number of letter a's in the first  letters of the infinite string.

# Example


# The substring we consider is , the first  characters of the infinite string. There are  occurrences of a in the substring.

# Function Description

# Complete the repeatedString function in the editor below.

# repeatedString has the following parameter(s):

# s: a string to repeat
# n: the number of characters to consider

s = "aba"
n = 10

a_count_in_s = s.count('a')

full_repetitions = n // len(s)

remaining_length = n % len(s)

a_count_in_remaining = s[:remaining_length].count('a')

total_a_count = (a_count_in_s * full_repetitions) + a_count_in_remaining
print (total_a_count)
