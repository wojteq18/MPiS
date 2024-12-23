import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Pobranie ścieżki do pliku od użytkownika
file_path = input("Podaj ścieżkę do pliku .txt z danymi: ")

# Pobranie tytułu od użytkownika
plot_title = input("Podaj tytuł wykresu: ")

try:
    # Wczytanie danych z pliku .txt
    data = pd.read_csv(file_path, sep=" ", names=["n", "attempts"], skiprows=0)

    # Sprawdzenie, czy dane zostały wczytane poprawnie
    print(data.head())  # Wyświetla pierwsze 5 wierszy danych jako debug

    # Obliczenie średniej wartości dla każdego n
    mean_values = data.groupby("n")["attempts"].mean().reset_index()

    # Rysowanie wykresu
    plt.figure(figsize=(10, 6))

    # Dodanie niebieskich kropek dla każdej próby
    plt.scatter(data["n"], data["attempts"], color='blue', alpha=0.6, label="Dokładne próby")

    # Dodanie czerwonych kropek dla średnich wartości
    plt.scatter(mean_values["n"], mean_values["attempts"], color='red', s=100, label="Średnia")

    # Ustawienia osi X i Y
    plt.xscale("linear")
    plt.xlabel("n (x 10^3)")
    plt.ylabel("")  # Pusta etykieta osi Y
    plt.title(plot_title)
    plt.legend()
    plt.grid(True)

    # Wyświetlenie wykresu
    plt.show()

except Exception as e:
    print("Wystąpił błąd:", e)
