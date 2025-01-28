import numpy as np
from scipy.stats import binom
import pandas as pd

# Parametry zadania
n_values = [100, 1000, 10000]
p = 0.5

# Wyliczamy prawą część nierówności Czebyszewa
def chebyshev_bound(n):
    mean = n * p
    var = n * p * (1 - p)
    threshold = mean / 10
    return var / threshold**2

# Obliczenia
results = []
for n in n_values:
    E_x = n / 2  # Średnia wartość (wartość oczekiwana)
    var_x = n / 4  # Wariancja
    markov_bound = 5 / 6  # Stała wartość dla Markowa
    
    # Obliczenia dla exact_a
    threshold_a = 6 / 5 * E_x
    exact_a = 1 - binom.cdf(threshold_a - 1, n, p)

    # Obliczenia dla exact_b
    threshold_b = 0.1 * E_x
    k = threshold_b  # Użycie progu jako k
    exact_b = binom.cdf(E_x + k - 1, n, p) - binom.cdf(E_x - k, n, p)

    # Czebyszew
    chebyshev_value = chebyshev_bound(n)  # Zmienna z unikalną nazwą

    # Dodanie wyników do listy
    results.append({
        "n": n,
        "Markov Bound": markov_bound,
        "Exact A": exact_a,
        "Chebyshev Bound": chebyshev_value,  # Zmienna zmieniona na chebyshev_value
        "Exact B": exact_b
    })

# Tworzenie tabeli wyników
results_df = pd.DataFrame(results)

# Wyświetlanie tabeli
print(results_df)
