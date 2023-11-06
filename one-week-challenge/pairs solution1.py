def pairs(k, arr):
    pairs = 0
    for i in range(len(arr)):
        search = 0
        search = arr[i] + k
        for j in range(len(arr)):
            if search == arr[j]:
                pairs += 1
    print(pairs)
    return(pairs)


