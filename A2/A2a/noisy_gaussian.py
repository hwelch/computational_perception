import numpy as np
import matplotlib.pyplot as plt

# function to generate a waveform
def genwaveform(N=100, alpha=0.1, A=1, sigma=1, noisetype="Gaussian"):
    if noisetype == "Gaussian":
        # initialize the noise to a random normal function
        noise = np.random.normal(0, sigma, N)
    elif noisetype == "uniform":
        # initialize the noise to a random uniform function
        noise = np.random.uniform(-sigma / 2, sigma / 2, N)

    # initalize events to an array of 0's of size N
    events = np.zeros(N)

    # randomly choose indices for the events to occue based on the probability and the length of the waveform 
    event_indices = np.random.choice(np.arange(N), size=int(alpha * N), replace=False)

    # the events that are at the indices are now set to amplitude A
    events[event_indices] = A

    # finally we just add these two values together to get the waveform and return both the waveform and event_indices
    waveform = noise + events
    return waveform, event_indices


# plot the waveform
def plot_genwaveform(N=100, alpha=0.1, A=1, sigma=1, noisetype="Gaussian"):
    waveform, event_indices = genwaveform(N, alpha, A, sigma, noisetype)
    plt.plot(waveform)
    plt.scatter(event_indices, np.ones_like(event_indices) * A * waveform[event_indices], marker='x', color='red', label='events')
    plt.legend()
    plt.grid(color='gray', linewidth=0.5, linestyle='--')
    plt.title("Randomly occuring events in Gaussian Noise")
    plt.show()

