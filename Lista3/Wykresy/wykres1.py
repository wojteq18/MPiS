import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Pobranie ścieżki do pliku od użytkownika
file_path = input("Podaj ścieżkę do pliku .txt z danymi: ")

# Pobranie tytułu od użytkownika
plot_title = input("Podaj tytuł wykresu: ")

try:
    # Wczytanie danych z pliku .txt
    data = pd.read_csv(file_path, sep=" ", names=["points", "estimate"], skiprows=0)

    # Sprawdzenie, czy dane zostały wczytane poprawnie
    print(data.head())  # Wyświetla pierwsze 5 wierszy danych jako debug

    # Zamiana danych na macierze numpy
    points = np.array(data["points"])
    estimates = np.array(data["estimate"])

    # Obliczanie średnich wartości dla każdej liczby punktów
    mean_values = data.groupby("points")["estimate"].mean()
    mean_points = mean_values.index  # Wartości unikalne punktów
    mean_estimates = mean_values.values  # Średnie oszacowania

    # Tworzenie wykresu
    plt.figure(figsize=(10, 6))

    # Wykres średnich wartości dla każdej liczby punktów (linia z kropkami)
    plt.plot(mean_points, mean_estimates, color='red', marker='o', label="Średnia")

    # Dodanie etykiet na osi X
    xticks = [10**3, 10**5, 10**6]  # Punkty na osi X
    plt.xticks(ticks=xticks, labels=[r'$10^3$', r'$10^5$', r'$10^6$'])  # Ustawienie etykiet

    # Dodanie etykiet i tytułu
    plt.xlabel("n")
    plt.title(plot_title)  # Użycie tytułu podanego przez użytkownika
    plt.legend()
    plt.grid(True)

    # Wyświetlenie wykresu
    plt.show()

except Exception as e:
    print("Wystąpił błąd:", e)
