def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2)
    save = 0
    end = a[mid-1:]
    new_end =[]
    for i in range(len(end)):
        save = end[len(end)-i-1]
        new_end.append(save)
        print(new_end)
        
    
    a = a[:mid-1] + new_end
    print(a)
    return a

a = [1,2,3,4,5,6,7,8]
n = len(a)
findZigZagSequence(a, n)