def caesarCipher(s, k):
    orig_alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    rot_alph = rotate_alph(k, orig_alph)
    print(rot_alph)
    
def rotate_alph(k, orig_alph):
    rot_alph = [0]*(26-k)
    for i in range(len(orig_alph)-k):
        rot_alph[i] = orig_alph[k + i]
    
    for i in range(k):
        rot_alph.append(orig_alph[i])
    
    return (rot_alph)

s = "Hello-World"
k = 5
caesarCipher(s, k)

