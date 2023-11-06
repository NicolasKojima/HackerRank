def is_palindrome(s):
    print(s == s[::-1])
    return s == s[::-1]

def palindromeIndex(s):
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            if is_palindrome(s[:i] + s[i+1:]):
                return i
            elif is_palindrome(s[:length - i - 1] + s[length - i:]):
                return length - i - 1
            else:
                return -1
    return -1

s= "aaab"
palindromeIndex(s)


def findZigZagSequence(a, n):
        a.sort()
        mid = int(n/2)
        a[mid], a[n-1] = a[n-1], a[mid]

        st = mid + 1
        ed = n - 2
        while(st <= ed):
                a[st], a[ed] = a[ed], a[st]
                st = st + 1
                ed = ed - 1

        for i in range (n):
                if i == n-1:
                        print(a[i])
                else:
                        print(a[i], end = ' ')
        return

test_cases = int(input())
for cs in range(test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)