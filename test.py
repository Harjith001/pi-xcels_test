def optimized_repetition(arr):
    hash_map = {}

    ans = -1

    for i in range(len(arr)):
        if hash_map.get(arr[i]) != None:
            ans = hash_map.get(arr[i])
            break
        else:
            hash_map[arr[i]] = i
        

    return ans


arr = [1, 2 ,3 ,4]

print(optimized_repetition(arr))

