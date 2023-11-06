
def count_digits(number):
    # Convert the number to a string and use len() to count the characters
    # This works for both positive and negative integers
    return len(str(abs(number)))


def superDigit(n, k):
    n = int(n)
    length = count_digits(n)
    num = n
    for i in range(k-1):
        n *= (10**(length))
        n += num

    while n > 9:
        sum = 0
        length = count_digits(n)
        for i in range(length):
            sum += int(str(n)[i])
        n = sum
    print(n)
    return n


n = 4757362
k = 10000
superDigit(n, k)