import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Funkcja do generowania wykresu
def plot_function(n, y_values, label, title):
    """Generuje wykres dla danej funkcji"""
    plt.figure(figsize=(10, 6))
    plt.plot(n, y_values, label=label, color='blue', marker='o', markersize=4)
    plt.xlabel("n")
    plt.ylabel(label)
    plt.title(title)
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
    print("12 - (d(n) - c(n))/(n ln n ln ln n)")
    choice = int(input("Wybierz numer funkcji: "))

    # Wykresy w zależności od wyboru użytkownika
    if choice == 1:
        plot_function(n, values / n, "b(n)/n", "Iloraz b(n)/n jako funkcja n")
    elif choice == 2:
        plot_function(n, values / np.sqrt(n), "b(n)/sqrt(n)", "Iloraz b(n)/sqrt(n) jako funkcja n")
    elif choice == 3:
        plot_function(n, values / n, "u(n)/n", "Iloraz u(n)/n jako funkcja n")
    elif choice == 4:
        plot_function(n, values / n, "c(n)/n", "Iloraz c(n)/n jako funkcja n")
    elif choice == 5:
        plot_function(n, values / (n * np.log(n)), "c(n)/(n ln n)", "Iloraz c(n)/(n ln n) jako funkcja n")
    elif choice == 6:
        plot_function(n, values / (n**2), "c(n)/n^2", "Iloraz c(n)/n^2 jako funkcja n")
    elif choice == 7:
        plot_function(n, values / n, "d(n)/n", "Iloraz d(n)/n jako funkcja n")
    elif choice == 8:
        plot_function(n, values / (n * np.log(n)), "d(n)/(n ln n)", "Iloraz d(n)/(n ln n) jako funkcja n")
    elif choice == 9:
        plot_function(n, values / (n**2), "d(n)/n^2", "Iloraz d(n)/n^2 jako funkcja n")
    elif choice == 10:
        c_values_path = input("Podaj ścieżkę do pliku z wartościami c(n): ")
        c_data = pd.read_csv(c_values_path, sep=" ", names=["n", "value"], skiprows=0)
        c_values = c_data["value"]
        plot_function(n, (values - c_values) / n, "(d(n) - c(n))/n", "Iloraz (d(n) - c(n))/n jako funkcja n")
    elif choice == 11:
        c_values_path = input("Podaj ścieżkę do pliku z wartościami c(n): ")
        c_data = pd.read_csv(c_values_path, sep=" ", names=["n", "value"], skiprows=0)
        c_values = c_data["value"]
        plot_function(n, (values - c_values) / (n * np.log(n)), "(d(n) - c(n))/(n ln n)", "Iloraz (d(n) - c(n))/(n ln n) jako funkcja n")
    elif choice == 12:
        c_values_path = input("Podaj ścieżkę do pliku z wartościami c(n): ")
        c_data = pd.read_csv(c_values_path, sep=" ", names=["n", "value"], skiprows=0)
        c_values = c_data["value"]
        plot_function(n, (values - c_values) / (n * np.log(n) * np.log(np.log(n))),
                      "(d(n) - c(n))/(n ln n ln ln n)", "Iloraz (d(n) - c(n))/(n ln n ln ln n) jako funkcja n")
    else:
        print("Nieprawidłowy wybór funkcji!")

except Exception as e:
    print(f"Wystąpił błąd: {e}")
