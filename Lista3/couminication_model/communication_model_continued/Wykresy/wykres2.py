import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Pobranie ścieżki do pliku z danymi
file_path = input("Podaj ścieżkę do pliku .txt z danymi: ")

# Prawdopodobieństwo p
p = 0.5  # zmień na odpowiednią wartość p

try:
    # Wczytanie danych
    data = pd.read_csv(file_path, sep=",", names=["station", "round"], skiprows=0)

    # Usunięcie duplikatów
    data = data.drop_duplicates(subset=["station"])

    # Maksymalna runda (Tn)
    Tn = data["round"].max()

    # Liczba stacji
    n = len(data["station"].unique())

    # Teoretyczne Tn
    Tn_theoretical = np.log(n) / np.log(1 / (1 - p))
    
    # Normalizacja empirycznego Tn
    Tn_normalized = Tn / (np.log(n) / -np.log(1 - p))
    
    # Normalizacja teoretycznego Tn
    Tn_theoretical_normalized = Tn_theoretical / (np.log(n) / -np.log(1 - p))

    # Wykres
    plt.figure(figsize=(12, 6))
    plt.scatter(np.log(n), Tn_normalized, color='blue', label="Empiryczne $T_n / T_{n, theor}$")
    
    ns = np.arange(1, n + 1)
    plt.plot(np.log(ns), np.log(ns) / np.log(1 / (1 - p)) / (np.log(ns) / -np.log(1 - p)), 
             color='red', label="Teoretyczne $T_n / T_{n, theor}$")

    plt.xlabel("$\log n$ (Liczba stacji)")
    plt.ylabel("Znormalizowane $T_n / T_{n, theor}$")
    plt.title("Znormalizowane Empiryczne vs Teoretyczne $T_n$")
    plt.legend()
    plt.grid(True)
    plt.show()

except Exception as e:
    print("Błąd:", e)
