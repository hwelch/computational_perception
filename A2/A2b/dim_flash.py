import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

def randtimes(N, t1, t2):
    return np.random.uniform(t1, t2, N)


def plotflash(x, t1, t2):
    y = np.ones(len(x))
    plt.stem(x, y, markerfmt=' ', basefmt=' ')
    plt.title(f'Plot of {len(x)} random times from [{t1}, {t2})')
    plt.show()


def plot_exponential_distribution(l):
    x = np.linspace(0, 5/l, 1000)
    y = l * np.exp(x * -l)
    plt.plot(x,y)
    plt.title(f'Exponential distribution with rate of {l}')
    plt.show()


def randintervals(N, l=10, t1=0):
    y = [t1]
    indx = 1
    t_x = t1
    while indx < N:
        t_x = t_x + np.random.exponential(1/l)
        y.append(t_x)
        indx += 1
    return np.array(y)


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
    return 1 - cdf


def plotdetectionprob(K, l=40, T=0.1):
    x = np.arange(0, K, 1)
    y = []
    for i in x:
        y.append(detectionprob(i, l, T))
    y = np.array(y)
    plt.bar(x,y)
    plt.xlabel('N')
    plt.ylabel('Probability of detecting photon')
    plt.title(f'CDF of events at rate {l} and time interval {T}')
    plt.show()


def lightflash(l, t1=0.8, t2=2.2):
    y = [t1]
    t_x = t1
    while t_x < t2:
        t_x = t_x + np.random.exponential(1/l)
        y.append(t_x)
    return np.array(y)


def plotlightflash(l, s1=1, s2=2):
    fig, axs = plt.subplots(nrows=3, ncols=1, figsize=(6, 8))

    x1 = lightflash(l)
    y1 = np.ones(len(x1))
    axs[0].stem(x1, y1, markerfmt=' ', basefmt=' ')
    axs[0].set(title=f'Photon stream at a rate of {l} photons / msec')

    x2 = []
    for x in x1:
        if x >= s1 and x <= s2:
            x2.append(x)
    x2 = np.array(x2)
    y2 = np.ones(len(x2))
    axs[1].stem(x2, y2, markerfmt=' ', basefmt=' ')
    axs[1].set(title=f'Photons that pass through a shutter')

    x3 = np.random.choice(x2, size=int(len(x2)*0.06), replace=False)
    y3 = np.ones(len(x3))
    axs[2].stem(x3, y3, markerfmt=' ', basefmt=' ')
    axs[2].set(title=f'Photons that are finally detected.', xlabel='ms')

    for ax in axs:
        ax.set_xlim([x1[0], x1[len(x1) - 1]])

    plt.tight_layout()
    plt.show()


def probseeing(I, a=0.06, K=6):
    return 1 - poisson.cdf(K-1, I*a)


def detectioncurve(a=0.5, K=6):
    I = np.arange(0.01, 100, 0.001)
    return I, probseeing(I, a, K)


def plotdetectioncurve(a=0.5, K=6):
    assert type(a) == float and type(K) == int or len(a) == len(K)

    if type(a) == float:
        I, prob = detectioncurve(a, K)
        plt.plot(I, prob, label=f'a = {a} K = {K}')
    else:
        i = 0
        while i < len(a):
            I, prob = detectioncurve(a[i], K[i])
            plt.plot(I, prob, label=f'a = {a[i]} K = {K[i]}')
            i += 1

    plt.xscale('log')
    
    plt.xlabel("log(I)")
    plt.ylabel("Percentage of light flashes")
    plt.legend()
    plt.title("Percentage of light flashes as a function of I")
    plt.show()


def plotfit(a=3, K=3):
    I, prob = detectioncurve(0.02, 2)
    plt.plot(I, prob, label='a = 0.02 K = 2')
    I2, prob2 = detectioncurve(0.13, 12)
    plt.plot(I2, prob2, label='a = 0.13 K = 12')

    avg_photons = [24.1, 37.6, 58.6, 91.0, 141.9, 221.3]
    percents =  [0.0,  0.04, 0.18, 0.54, 0.94, 1.00]

    I, prob = detectioncurve(a, K)
    plt.plot(I, prob, label=f'a = {a} K = {K}')

    plt.scatter(avg_photons, percents)
    plt.xscale('log')
    plt.xlabel("log(I)")
    plt.ylabel("Percentage of light flashes")
    plt.legend()
    plt.title("Percentage of light flashes as a function of I")
    plt.show()

