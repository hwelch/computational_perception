
import math
import matplotlib.pyplot as plt
import numpy as np

def sinewave(t, f = 1.0, d = 0.0):
    return np.sin(2 * math.pi * f * (t + d))


def plot_sinewave(t, f = 1.0, d = 0.0):
    y = sinewave(t, f, d)
    plt.plot(t, y)

    plt.title(f'sinewave(t: frequency=${f}, delay=${d})')
    plt.grid(color='gray', linestyle='-', linewidth=0.1)
    # plt.legend()
    plt.show()


t = np.arange(-2, 2, 0.001)
plot_sinewave(t)


print(sinewave(0.0, 5, 0.05))

def plot_twowaves():
    t = np.arange(-0.1, 1.0, 0.001)
    f = 5
    delay = 0.05

    y_solid = sinewave(t, f)
    y_dashed = sinewave(t, f, delay)

    plt.plot(t, y_solid, "-")
    plt.plot(t, y_dashed, "--")
    plt.grid(color='gray', linestyle='-', linewidth=0.1)
    plt.title(f'Two Sinewave')
    plt.show()

print(sinewave(0.0, f=5, d=0.05))