def caesarCipher(s, k):
    orig_alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    rot_alph = rotate_alph(k, orig_alph)
    new_s = [char for char in s]
    ans = []
    for i in range(len(new_s)):
        if new_s[i].isalpha() == False:
            ans.append(new_s[i])
        elif new_s[i].isupper():
            new_s[i] = new_s[i].lower()
            position = search_position(i, new_s, orig_alph)
            ans.append(rot_alph[position].upper())
        else:
            position = search_position(i, new_s, orig_alph)
            ans.append(rot_alph[position])
    print(''.join(ans))
    return ''.join(ans)

def search_position(i, new_s, orig_alph):
    if new_s[i] in orig_alph:
        position = orig_alph.index(new_s[i])
        return position
    else:
        print("s[i] is not in the alphabet, and is not -")
        return

def rotate_alph(k, orig_alph):
    remainder = k % 26
    k = remainder
    rot_alph = [0]*(26-k)
    for i in range(len(orig_alph)-k):
        rot_alph[i] = orig_alph[k + i]
    
    for i in range(k):
        rot_alph.append(orig_alph[i])
    
    return (rot_alph)



s = "159357lcfd"
k = 98
caesarCipher(s, k)
