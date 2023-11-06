

def minimumBribes(q):
    # bubble sort with s = number of swaps
    s = 0
    # bubble sort - condition
    while q != sorted(q):
        # bubble sort - loop over list
        for i in range(len(q) - 1):
            # if any number moved forward more than 2, too chaotic
            if q[i] - (i + 1) > 2:
                print("Too chaotic")
                return
            # bubble sort - swap
            if q[i] > q[i + 1]:
                s += 1
                q[i], q[i + 1] = q[i + 1], q[i]
    print(s)



q = [1,2,5,3,7,8,6,4]
minimumBribes(q)