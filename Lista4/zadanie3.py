import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def random_walk(n):
    #n -> liczba krokow
    x = np.zeros(n)
    for i in range(1, n):
        x[i] = x[i - 1] + np.random.choice([-1, 1], p=[0.5, 0.5])
    return x

def time_fraction(n, k):
        values = []
        for _ in range(k):
            x = random_walk(n)
            D_n = np.zeros(n)
            for i in range(n):
                D_n[i] = 1 if x[i] > 0 or x[i - 1] > 0 else 0
            L_n = np.sum(D_n)    
            P_n = L_n / n
            values.append(P_n)
        return values    
    
n_values = [100, 1000, 10000]
k = 5000

for N in n_values:
    fractions = time_fraction(N, k)
    plt.figure()
    plt.hist(fractions, bins=20, density=True, alpha=0.6, color='g')
    plt.title(f'Frakcje czasu P_N dla N = {N}')
    plt.xlabel('P_N')
    plt.grid(True)
    plt.show()