import matplotlib.pyplot as plt
import numpy as np

def gabor(t, a = 1, f = 1, sigma = 1, phi = 0):
    vector = np.vectorize(np.float_)
    t = vector(t)
    return a * np.exp(- (t ** 2) / (2 * sigma ** 2)) * np.cos(2 * np.pi * f * t + phi)

def plot_gabor(t, a = 1, f = 1, sigma = 1, phase = 0, type="gabor"):
    if type == "gabor":
        y = gabor(t, a, f, sigma, phase)
    elif type == "gabore" or type == "even":
        y = gabore(t, a, f, sigma)
    else:
        y = gaboro(t, a, f, sigma)
    plt.plot(t, y)
    plt.title(f'gabor function')
    plt.grid(color='gray', linestyle='-', linewidth=0.1)
    # plt.legend()
    plt.show()

def gabore(t, a = 1, f = 1, sigma = 1):
    phi = 0
    return gabor(t, a, f, sigma, phi)

def gaboro(t, a = 1, f = 1, sigma = 1):
    phi = np.pi / 2
    return gabor(t, a, f, sigma, phi)

def gabor_norm(f = 1, sigma = 1, phi = 0, fs = 100):

    t = np.arange(-6*sigma, 6*sigma, 1/fs)
    a = 1
    gab = gabor(t, a, f, sigma, phi)
    return np.linalg.norm(gab)

def gabore_norm(f = 1, sigma = 1, fs = 100):
    phi = 0
    return gabor_norm(f, sigma, phi, fs)

def gaboro_norm(f = 1, sigma = 1, fs = 100):
    phi = np.pi / 2
    return gabor_norm(f, sigma, phi, fs)


t = np.arange(-4, 4, 0.001)
plot_gabor(t)

print(gaboro(-3, f=0.0625, sigma=8))
print(gabor_norm(f=100, sigma=0.01, fs=10000))