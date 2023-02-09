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
    plt.scatter(event_indices, np.ones_like(event_indices) * waveform[event_indices], marker='x', color='red', label='events')
    plt.legend()
    plt.grid(color='gray', linewidth=0.5, linestyle='--')
    plt.title("Randomly occuring events in Gaussian Noise")
    plt.show()


# compare the parameters
def plot_comparison():
    fig, axs = plt.subplots(2, 2)
    waveform, event_indices = genwaveform(A=1, noisetype="Gaussian")
    axs[0, 0].plot(waveform)
    axs[0, 0].scatter(event_indices, np.ones_like(event_indices) * waveform[event_indices], marker='x', color='red', label='events')
    axs[0, 0].set_title('A=1, noisetype=Gaussian')

    waveform, event_indices = genwaveform(A=100, noisetype="Gaussian")
    axs[0, 1].plot(waveform, 'tab:orange')
    axs[0, 1].scatter(event_indices, np.ones_like(event_indices) * waveform[event_indices], marker='x', color='red', label='events')
    axs[0, 1].set_title('A=100, noisetype=Gaussian')


    waveform, event_indices = genwaveform(A=1, noisetype="uniform")
    axs[1, 0].plot(waveform, 'tab:green')
    axs[1, 0].scatter(event_indices, np.ones_like(event_indices) * waveform[event_indices], marker='x', color='red', label='events')
    axs[1, 0].set_title('A=1, noisetype=uniform')

    waveform, event_indices = genwaveform(A=100, noisetype="uniform")
    axs[1, 1].plot(waveform, 'tab:red')
    axs[1, 1].scatter(event_indices, np.ones_like(event_indices) * waveform[event_indices], marker='x', color='red', label='events')
    axs[1, 1].set_title('A=100, noisetype=uniform')
    fig.tight_layout()
    plt.show()



# going to have this return an array of indexes instead for now, will be more useful
def detect_indices(si, y, theta):
    tp, fn, fp, tn = [], [], [], []
    ele = 0
    while ele < len(y):
        # if element index is a signal
        if ele in si:
            if y[ele] >= theta:
                # then the element should be greater than theta i.e. true positive
                tp.append(ele)
            else:
                # if not then it is a false negative
                fn.append(ele)

        # if the element is not a signal            
        else:
            if y[ele] >= theta:
                # if this is greater than or equal to theta but it is not a signal it is a false positive
                fp.append(ele)
            else:
                # otherwise it is a true negative
                tn.append(ele)
        ele += 1
    return tp, fn, fp, tn


def detectioncounts(si, y, theta):
    tp, fn, fp, tn = detect_indices(si, y, theta)
    return len(tp), len(fn), len(fp), len(tn)


def plot_detection_types(si, y, theta, title="Graph with detection types"):
    tp, fn, fp, tn = detect_indices(si, y, theta)
    plt.plot(y)
    plt.axhline(theta, c="red", label = f'threshold = {theta}')

    # plot the tp, fp, and fn
    plotted = []
    for i in tp:
        label = "True Positives"
        if label not in plotted:
            plt.scatter(i, y[i], c="blue", marker="o", label="True Positives")
            plotted.append(label)
        else:
            plt.scatter(i, y[i], c="blue", marker="o")
    
    for i in fp:
        label = "False Positives"
        if label not in plotted:
            plt.scatter(i, y[i], c="green", marker="^", label="False Positives")
            plotted.append(label)
        else:
            plt.scatter(i, y[i], c="green", marker="^")
    
    for i in fn:
        label = "False Negatives"
        if label not in plotted:
            plt.scatter(i, y[i], c="orange", marker="s", label="False Negatives")
            plotted.append(label)
        else:
            plt.scatter(i, y[i], c="orange", marker="s")

    plt.legend()
    plt.title(title)
    plt.show()

