# function to downsample data and get the lower, upper, and block indicies of each

def envelope(y, nblocks = 10):
    ylower = []
    yupper = []
    blockindices = []

    size_block = int(len(y) / nblocks)

    remainders = len(y) % nblocks
    # if we have remainders the first few blocks need to take an extra element
    if remainders > 0:
        size_block += 1

    index = 0
    iteration_num = 0
    while index < len(y):
        # here we are setting the size of the block back to the original number after we have gotten through the correct number of blocks that need an extra element
        if iteration_num == remainders and remainders != 0:
            size_block -= 1
        else: size_block 
        if index + size_block < len(y):
            upper = index + size_block
        else:
            upper = len(y)
        arr = y[index: upper]
        ylower.append(min(arr))
        yupper.append(max(arr))
        blockindices.append(index)
        index = upper
        iteration_num += 1
    return ylower, yupper, blockindices

test_arr = [1, 2, 3, 4, 1, 2, 3, -1, -5, -7, 0, -1, 1, ]
yl, yu, bi = envelope(test_arr)
print(yl, yu, bi)