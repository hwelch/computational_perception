import matplotlib.pyplot as plt
import numpy as np
import wave

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


# speech wave file handling

filepath = "C:\\Users\\hunte\\Documents\\Spring 2023\\Computer Perception\\A1\\A1b\\speech.wav"
speech = wave.open(filepath, mode='rb')
framerate = speech.getframerate()
print(framerate)
speech = list(speech.readframes(speech.getnframes()))

def plot_time(start, end):
    num_of_points = len(speech[int(start * framerate): int(end * framerate)])
    time = np.arange(start, end, (end - start) / num_of_points)
    indx = (time * framerate).astype(int)
    extracted_speech = np.array(indx)

    plt.plot(time, extracted_speech)
    plt.title("Extracted Speech from 3.0 to 3.1 seconds")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.show()

# e_speech = envelope(speech, 500)
# plt.plot(e_speech)
# plt.title("Enveloped Speech from Entire .wav file")
# plt.xlabel("Sample Index")
# plt.ylabel("Amplitude")
# plt.show()

plot_time(3.0, 3.1)
