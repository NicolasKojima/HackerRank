

def LHSfunction(s, LHS):
    store = [0]*int(len(s))
    for i in range(int((len(s)))):
        for j in range(len(LHS)):
            if s[i] == LHS[j]:
                store[i] = j
    return store


def RHSfunction(s, RHS):
    store = [0]*int(len(s))
    for i in range(int((len(s)))):
        for j in range(len(RHS)):
            if s[i] == RHS[j]:
                store[i] = j
    return store
    
def isBalanced(s):
    if len(s) % 2 == 1:
        return "NO"
        
    LHS = ["{", "(", "["]
    RHS = ["}", ")", "]"]
    half = int(len(s)/2)

    s_l = s[:half]
    s_r = s[half:]
    print(s_l, s_r, "db1")

    arr_LHS = LHSfunction(s_l, LHS)
    arr_RHS = RHSfunction(s_r, RHS)

    arr_RHS = arr_RHS[::-1]
    print(arr_LHS, arr_RHS)
    for i in arr_LHS:
        if arr_LHS[i] != arr_RHS[i]:
            print("no")
            return "NO"
    print("yes")
    return "YES"
        
s = "{(([])[])[]}[]"
isBalanced(s)