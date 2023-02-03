import math
import matplotlib.pyplot as plt
import numpy as np

def compute_gaussian(x, mean, sd):
    return math.exp(-1/2 * ((x - mean) / sd)**2) / (sd * math.sqrt(2 * math.pi))


def plot_gaussian(x1, mean, sd):
    x = np.arange(mean - (4.0 * sd), mean + (4.0 * sd), 0.001)
    y = []
    for i in x:
        y.append(compute_gaussian(i, mean, sd)) 
    y = np.array(y)
    plt.plot(x, y)

    # get the plot for vertical line to x1
    y1 = compute_gaussian(x1, mean, sd)
    plt.vlines(x1, ymin=0, ymax=y1, colors="orange")
    plt.plot(x1, y1, 'go', mec="black", label = f'${x1}: ${round(y1, 3)}')

    plt.grid(color='gray', linestyle='-', linewidth=0.1)
    plt.title(f'p(x | mean=${mean}, sd=${sd})')
    plt.legend()
    plt.show()

    
plot_gaussian(1, 0, 1)
plot_gaussian(-2, -1, 0.5)
