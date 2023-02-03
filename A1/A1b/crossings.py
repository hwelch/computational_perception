
# a function to compute the indicies of where a function first equals or crosses a specific threshold
def crossings(arr, threshold, direction = 'both'):
    crosses = []
    i = 1
    while i < len(arr):
        if arr[i] == threshold and arr[i - 1] != threshold:
            crosses.append(i)
        elif arr[i] > threshold and arr[i - 1] < threshold and (direction == 'both' or direction == 'negpos'):
            crosses.append(i)
        elif arr[i] < threshold and arr[i - 1] > threshold and (direction == 'both' or direction == 'posneg'):
            crosses.append(i)
        i += 1
    return crosses



test_arr = [1, 2, 3, 4, 1, 2, 3, -1, -5, -7, 0, -1, 1]
exp = [4, 7, 12]
print(crossings(test_arr, 1))
