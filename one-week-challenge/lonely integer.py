def lonelyinteger(a):
    
    dict = {}

    for num in a:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
    
    for num in dict:
        if dict[num] == 1:
            return num

    return

a = [0, 0, 1, 2, 1]
lonelyinteger(a)