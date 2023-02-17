import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

def randtimes(N, t1, t2):
    return np.random.uniform(t1, t2, N)


def plotflash(N, t1, t2):
    x = randtimes(N, t1, t2)
    y = np.ones(N)
    plt.stem(x, y, markerfmt=' ')
    plt.title(f'Plot of {N} random times from [{t1}, {t2})')
    plt.show()


def randintervals(N, l, t1):
    y = [t1]
    indx = 1
    t_x = t1
    while indx < N:
        t_x = t_x + np.random.exponential(1/l)
        y.append(t_x)
        indx += 1
    return np.array(y)


def plotrandintervals(N, l, t1):
    x = randintervals(N, l, t1)
    print(N, len(x))
    y = np.ones(N)
    plt.stem(x, y, markerfmt=' ')
    plt.title(f'Plot of {N} random times starting at {t1} at a rate of {l}')
    plt.show()


def poisson_pmf(N, l, T):
    return poisson.pmf(N, l * T)


def plot_poisson_pmf(N, l, T):
    x = np.arange(0, N, 1)
    y = poisson_pmf(x, l, T)
    plt.bar(x,y)
    plt.xlabel('N')
    plt.ylabel('Probability of detecting photon')
    plt.title(f'PDF of {N} events at rate {l} and time interval {T}')
    plt.show()


def detectionprob(K, l=40, T=0.1):
    i = 0
    cdf = 0
    while i < K:
        cdf += poisson_pmf(i, l, T)
        i += 1
    return cdf


def plotdetectionprob(K, l=40, T=0.1):
    x = np.arange(0, K, 1)
    y = []
    for i in x:
        y.append(detectionprob(i, l, T))
    y = np.array(y)
    plt.bar(x,y)
    plt.xlabel('N')
    plt.ylabel('Probability of detecting photon')
    plt.title(f'CDF of {K-1} events at rate {l} and time interval {T}')
    plt.show()

plotdetectionprob(10)