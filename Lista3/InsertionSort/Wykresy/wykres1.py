import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Pobranie ścieżki do pliku od użytkownika
file_path = input("Podaj ścieżkę do pliku .txt z danymi: ")

# Pobranie tytułu od użytkownika
plot_title = input("Podaj tytuł wykresu: ")

try:
    # Wczytanie danych z pliku .txt
    data = pd.read_csv(file_path, sep=",", names=["n", "value"], skiprows=0)

    # Sprawdzenie, czy dane zostały wczytane poprawnie
    print(data.head())  # Debug: pierwsze 5 wierszy

    # Obliczenie średniej wartości dla każdego n
    mean_values = data.groupby("n")["value"].mean()
    mean_points = mean_values.index  # Wartości unikalne n
    mean_estimates = mean_values.values  # Średnie wartości

    # Zapytanie użytkownika o wybór opcji
    print("Wybierz opcję:")
    print("1 - Rysuj wykres średnich wartości (czerwony wykres) i dokładnych wartości (niebieskie kropki)")
    print("2 - Podziel dane przez funkcję i narysuj wykres")
    option = int(input("Wprowadź numer opcji: "))

    if option == 1:
        # Opcja 1: Rysowanie wykresu średnich wartości i dokładnych wartości
        plt.figure(figsize=(10, 6))
        plt.scatter(data["n"], data["value"], color='blue', label="Wartości", alpha=0.6)
        plt.plot(mean_points, mean_estimates, color='red', marker='o', label="Średnia")

    elif option == 2:
        # Opcja 2: Dzielenie danych przez funkcję
        print("Wybierz funkcję do podzielenia danych:")
        print("1 - f1 = n")
        print("2 - f2 = n^2")
        func_option = int(input("Wprowadź numer funkcji: "))

        if func_option == 1:
            # Funkcja 1: n
            data["modified_value"] = data["value"] / data["n"]
        elif func_option == 2:
            # Funkcja 2: n^2
            data["modified_value"] = data["value"] / (data["n"] ** 2)
        else:
            raise ValueError("Nieprawidłowy wybór funkcji")

        # Obliczenie średnich wartości zmodyfikowanych danych
        modified_mean_values = data.groupby("n")["modified_value"].mean()
        modified_mean_points = modified_mean_values.index
        modified_mean_estimates = modified_mean_values.values

        plt.figure(figsize=(10, 6))
        plt.scatter(data["n"], data["modified_value"], color='blue', label="Wartości", alpha=0.6)
        plt.plot(modified_mean_points, modified_mean_estimates, color='red', marker='o', label="Średnia zmodyfikowana")

    else:
        raise ValueError("Nieprawidłowy wybór opcji")

    # Dodanie etykiet i tytułu
    plt.xlabel("n")
    #plt.ylabel("Wartość")
    plt.title(plot_title)
    plt.legend()
    plt.grid(True)

    # Wyświetlenie wykresu
    plt.show()

except Exception as e:
    print("Wystąpił błąd:", e)
