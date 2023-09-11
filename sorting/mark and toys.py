#https://www.hackerrank.com/challenges/mark-and-toys/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

k = 0
prices = 0

prices.sort()
pay = 0
loop = 0
toys = 0
while pay < k:
    if loop == 0:
        pay = prices[loop]
        loop += 1
        toys += 1
    else:
        pay += prices[loop]
        loop += 1
        toys += 1
toys -= 1        
