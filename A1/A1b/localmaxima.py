def localmaxima(arr):
    local_maxes = []
    i = 1
    while i < len(arr) - 1:
        if arr[i - 1] < arr[i] and arr[i + 1] < arr[i]:
            local_maxes.append(i)
        i += 1
    return local_maxes

test_arr = [1, 2, 3, 4, 1, 2, 3, -1, -5, -7, 0, -1]
print(localmaxima(test_arr))