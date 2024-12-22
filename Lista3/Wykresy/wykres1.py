import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

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

    # Zapytanie użytkownika o wybór opcji
    print("Wybierz opcję:")
    print("1 - Rysuj wykres bez modyfikacji")
    print("2 - Podziel dane przez wybraną funkcję i narysuj wykres")
    option = int(input("Wprowadź numer opcji: "))

    if option == 1:
        # Opcja 1: Rysowanie wykresu bez modyfikacji
        mean_values = data.groupby("points")["estimate"].mean()
        mean_points = mean_values.index  # Wartości unikalne punktów
        mean_estimates = mean_values.values  # Średnie oszacowania

        plt.figure(figsize=(10, 6))
        plt.plot(mean_points, mean_estimates, color='red', marker='o', label="Średnia")

    elif option == 2:
        # Opcja 2: Dzielenie danych przez funkcję
        print("Wybierz funkcję do podzielenia danych:")
        print("1 - f1 = ln(n) / (ln(ln(n)))")
        print("2 - f2 = ln(ln(n)) / ln(2)")
        func_option = int(input("Wprowadź numer funkcji: "))

        if func_option == 1:
            # Funkcja 1: ln(n) / ln(ln(n))
            def f1(n):
                return np.log(n) / np.log(np.log(n))

            data["transformed_estimate"] = data.apply(lambda row: row["estimate"] / f1(row["points"]) if row["points"] > math.e else np.nan, axis=1)

        elif func_option == 2:
            # Funkcja 2: ln(ln(n)) / ln(2)
            def f2(n):
                return np.log(np.log(n)) / np.log(2)

            data["transformed_estimate"] = data.apply(lambda row: row["estimate"] / f2(row["points"]) if row["points"] > math.e else np.nan, axis=1)

        else:
            raise ValueError("Nieprawidłowy wybór funkcji")

        # Usuwanie wartości NaN
        data = data.dropna()

        mean_values = data.groupby("points")["transformed_estimate"].mean()
        mean_points = mean_values.index  # Wartości unikalne punktów
        mean_estimates = mean_values.values  # Średnie oszacowania

        plt.figure(figsize=(10, 6))
        plt.plot(mean_points, mean_estimates, color='blue', marker='o', label="Średnia (przekształcona)")

    else:
        raise ValueError("Nieprawidłowy wybór opcji")

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
