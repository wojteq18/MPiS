import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def simulate_sn(n, k):
    # n - liczba symulacji
    # k - liczba prób

    # generujemy macierz, w której każdy wiersz to jedna symulacja
    random_variables = np.random.choice([-1, 1], p=[0.5, 0.5], size=(k, n))
    # obliczenie sumy dla każdej próby
    return np.sum(random_variables, axis=1)

def empirical_cdf(data, bins):
    # Obliczamy dystrybuantę empiryczną dla danych
    # data - wartości zmiennej losowej
    # bins - granice przedziałów dla histogramu

    hist, _ = np.histogram(data, bins=bins, density=True)  # oblicza rozkład gęstości danych w podanym przedziale
    cdf = np.cumsum(hist * np.diff(bins))  # oblicza dystrybuantę empiryczną sumując wartości
    return cdf

N_values = [5, 10, 15, 20, 25, 30, 100]
k = 1000000

for N in N_values:
    SN = simulate_sn(N, k)

    # tworzymy przedziały
    bins = np.linspace(-N, N, 2 * N + 1)

    cdf_empirical = empirical_cdf(SN, bins)

    # teoretyczne wyznaczenie dystrybuanty rozkładu normalnego
    x = 0
    sigma = np.sqrt(N)
    cdf_normal = norm.cdf(bins, loc=x, scale=sigma)

    # Wykres
    plt.figure(figsize=(8, 5))
    plt.step(bins[:-1], cdf_empirical, where='post', label=f'Dystrybuanta empiryczna (N={N})', color='blue')
    plt.plot(bins, cdf_normal, label=f'Dystrybuanta normalna (N={N})', color='red', linestyle='--')
    plt.title(f'Porównanie dystrybuanty empirycznej i normalnej dla N = {N}')
    plt.xlabel('Wartość S_N')
    plt.ylabel('Dystrybuanta')
    plt.legend()
    plt.grid(True)
    plt.show()
