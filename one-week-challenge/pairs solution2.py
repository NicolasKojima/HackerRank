def count_elements(arr):
    element_count = {}
    for item in arr:
        if item in element_count:
            element_count[item] += 1
        else:
            element_count[item] = 1
    return element_count


def pairs(k, arr):
    unique_int = list(set(arr))
    print(unique_int, "HERE")
    repeated_num = count_elements(arr)
    pairs = 0
    
    for i in range(len(unique_int)):
        for k in range(len(unique_int)):
            if unique_int[i] + k == unique_int[k]:
                print("here", i, k, "int i:", unique_int[i], repeated_num, pairs)
                if unique_int[k] in repeated_num:
                    pairs += repeated_num[unique_int[k]]
                    # print(unique_int[i], repeated_num, pairs)
    print(pairs)

# Example usage:
my_array = [1, 3, 3, 3, 5, 5, 5, 9, 11, 13, 15, 14, 14, 14, 19, 20]
k = 2
element_count = pairs(k, my_array)
print(element_count)