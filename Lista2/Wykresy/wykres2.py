import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Funkcja do generowania wykresu
def plot_function_with_mean(n, y_values, latex_formula):
    """Generuje wykres dla danej funkcji wraz ze średnią"""
    # Obliczanie średnich wartości dla każdego n
    mean_values = pd.DataFrame({"n": n, "y_values": y_values}).groupby("n").mean()
    mean_n = mean_values.index
    mean_y = mean_values["y_values"]

    # Wykres
    plt.figure(figsize=(10, 6))
    # Niebieskie punkty dla danych surowych
    plt.scatter(n, y_values, color='blue', alpha=0.7, s=10)
    # Czerwone punkty dla średniej
    plt.scatter(mean_n, mean_y, color='red', label="Średnia", zorder=5, s=50)  # Średnia oznaczona czerwonymi kropkami
    plt.xlabel("n")  # Oś X opisana jako n
    plt.title(rf"Wykres {latex_formula}")  # Dodanie słowa "Wykres" przed wzorem
    plt.legend()
    plt.grid(True)
    plt.show()

try:
    # Pobranie pliku z danymi
    file_path = input("Podaj ścieżkę do pliku z danymi (n, value): ")

    # Wczytanie danych
    data = pd.read_csv(file_path, sep=" ", names=["n", "value"], skiprows=0)
    n = data["n"]
    values = data["value"]

    # Pobranie wyboru funkcji od użytkownika
    print("\nWybierz rodzaj funkcji do wykresu:")
    print("1 - b(n)/n")
    print("2 - b(n)/sqrt(n)")
    print("3 - u(n)/n")
    print("4 - c(n)/n")
    print("5 - c(n)/(n ln n)")
    print("6 - c(n)/n^2")
    print("7 - d(n)/n")
    print("8 - d(n)/(n ln n)")
    print("9 - d(n)/n^2")
    print("10 - (d(n) - c(n))/n")
    print("11 - (d(n) - c(n))/(n ln n)")
    print("12 - (d(n) - c(n))/(n ln ln n)")
    choice = int(input("Wybierz numer funkcji: "))

    # Wykresy w zależności od wyboru użytkownika
    if choice == 1:
        plot_function_with_mean(n, values / n, r"$\frac{b(n)}{n}$")
    elif choice == 2:
        plot_function_with_mean(n, values / np.sqrt(n), r"$\frac{b(n)}{\sqrt{n}}$")
    elif choice == 3:
        plot_function_with_mean(n, values / n, r"$\frac{u(n)}{n}$")
    elif choice == 4:
        plot_function_with_mean(n, values / n, r"$\frac{c(n)}{n}$")
    elif choice == 5:
        plot_function_with_mean(n, values / (n * np.log(n)), r"$\frac{c(n)}{n \ln n}$")
    elif choice == 6:
        plot_function_with_mean(n, values / (n**2), r"$\frac{c(n)}{n^2}$")
    elif choice == 7:
        plot_function_with_mean(n, values / n, r"$\frac{d(n)}{n}$")
    elif choice == 8:
        plot_function_with_mean(n, values / (n * np.log(n)), r"$\frac{d(n)}{n \ln n}$")
    elif choice == 9:
        plot_function_with_mean(n, values / (n**2), r"$\frac{d(n)}{n^2}$")
    elif choice == 10:
        # Wczytanie danych i obliczenie (d(n) - c(n)) / n
        plot_function_with_mean(n, values / n, r"$\frac{d(n) - c(n)}{n}$")
    elif choice == 11:
        # Wczytanie danych i obliczenie (d(n) - c(n)) / (n ln n)
        plot_function_with_mean(n, values / (n * np.log(n)), r"$\frac{d(n) - c(n)}{n \ln n}$")
    elif choice == 12:
        # Wczytanie danych i obliczenie (d(n) - c(n)) / (n ln ln n)
        plot_function_with_mean(n, values / (n * np.log(np.log(n))), r"$\frac{d(n) - c(n)}{n \ln \ln n}$")
    else:
        print("Nieprawidłowy wybór funkcji!")

except Exception as e:
    print(f"Wystąpił błąd: {e}")