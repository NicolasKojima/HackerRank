
def isBalanced(s):
    storage= ["empty"]
    LHS = ["{", "(", "["]
    RHS = ["}", ")", "]"]
    
    for i in range(len(s)):
        if s[i] == LHS[0]:
            storage.append(0)
        elif s[i] == LHS[1]:
            storage.append(1)
        elif s[i] == LHS[2]:
            storage.append(2)
        elif storage[-1] != "empty" and s[i] == RHS[storage[-1]]:
            storage.pop()
        else:
            print("No")
            return "NO"
    if storage[-1] != "empty":
        print("NO")
        return "NO"
    else:
        print("Yes")
        return "YES"
            
# s = "{[(])}"
s = "(){}[()[][]]{}(())()[[([])][()]{}{}(({}[]()))()[()[{()}]][]]{"
isBalanced(s)