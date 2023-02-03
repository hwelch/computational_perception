import matplotlib.pyplot as plt
import numpy as np


def erb(f):
    return 24.7 * ((4.37 * f) / 1000 + 1)

def get_b(f):
    return (1.019 * erb(f))

def gammatone_norm(n = 4, f = 200, phi = 0, fs = 10000):
    b = get_b(f)
    t = np.arange(0, 5, 1/fs)
    gamma = t ** (n - 1) * np.exp(-2 * np.pi * b * t) * np.cos(2 * np.pi * f * t + phi)
    return np.linalg.norm(gamma)

def gammatone(t, n = 4, f = 200, phi = 0, fs = 10000):
    b = get_b(f)
    a = gammatone_norm(n, f, phi, fs)

    return a * (t ** (n - 1)) * np.exp(-2 * np.pi * b * t) * np.cos(2 * np.pi * f * t + phi)


def plot_gammatone(t, n = 4, f = 200, phi = 0):
    y = gammatone(t, n, f, phi)
    plt.plot(t, y)

    plt.title(f'gammatone function')
    plt.grid(color='gray', linestyle='-', linewidth=0.1)
    # plt.legend()
    plt.show()


t = np.arange(0, 0.05, 0.0001)
plot_gammatone(t)

print(gammatone(0.01, f=100))
