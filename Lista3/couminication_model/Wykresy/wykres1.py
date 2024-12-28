import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Pobranie ścieżki do pliku od użytkownika
file_path = input("Podaj ścieżkę do pliku .txt z danymi: ")

# Pobranie tytułu od użytkownika
plot_title = input("Podaj tytuł wykresu: ")

try:
    # Wczytanie danych z pliku .txt
    data = pd.read_csv(file_path, sep=",", names=["n", "attempts"], skiprows=0)

    # Sprawdzenie, czy dane zostały wczytane poprawnie
    print(data.head())  # Wyświetla pierwsze 5 wierszy danych jako debug

    # Konwersja kolumny "n" na typ liczbowy
    data["n"] = pd.to_numeric(data["n"], errors="coerce")
    data = data[(data["n"] >= 10000) & (data["n"] <= 1000000)]  # Filtrowanie danych dla 10000 ≤ n ≤ 1000000

    # Obliczenie średniej wartości dla każdego n
    mean_values = data.groupby("n")["attempts"].mean().reset_index()

    # Modyfikacja średnich wartości - podzielenie przez log(n)
    mean_values["adjusted_mean"] = mean_values["attempts"] / np.log(mean_values["n"])

    # Rysowanie wykresu
    plt.figure(figsize=(10, 6))

    # Dodanie czerwonych kropek dla średnich wartości podzielonych przez log(n)
    plt.scatter(mean_values["n"], mean_values["adjusted_mean"], color='red', s=100, label="Średnia / log(n)")

    # Ustawienia osi X i Y
    plt.xscale("linear")
    plt.yscale("linear")
    plt.xlabel("n (x 10^3)")
    plt.ylabel("Średnia / log(n)")
    plt.title(plot_title)
    plt.legend()
    plt.grid(True)

    # Wyświetlenie wykresu
    plt.show()

except Exception as e:
    print("Wystąpił błąd:", e)
