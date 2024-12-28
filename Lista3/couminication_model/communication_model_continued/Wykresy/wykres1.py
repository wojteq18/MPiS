import pandas as pd
import matplotlib.pyplot as plt

# Pobranie ścieżki do pliku od użytkownika
file_path = input("Podaj ścieżkę do pliku .txt z danymi: ")

# Pobranie tytułu od użytkownika
plot_title = input("Podaj tytuł wykresu: ")

try:
    # Wczytanie danych z pliku .txt
    data = pd.read_csv(file_path, sep=",", names=["station", "round"], skiprows=0)

    # Sprawdzenie, czy dane zostały wczytane poprawnie
    print(data.head())  # Wyświetla pierwsze 5 wierszy danych jako debug

    # Usunięcie duplikatów na podstawie kolumny 'station'
    data = data.drop_duplicates(subset=["station"])

    # Grupowanie i liczenie liczby stacji dla każdej rundy
    round_counts = data["round"].value_counts().sort_index()

    # Rysowanie wykresu
    plt.figure(figsize=(12, 6))

    # Histogram – liczba stacji dla każdej rundy
    plt.bar(round_counts.index, round_counts.values, color='skyblue', label="Liczba stacji")

    # Ustawienia osi X i Y
    plt.xscale("linear")
    plt.yscale("linear")
    plt.xlabel("Numer rundy")
    plt.ylabel("Liczba stacji")
    plt.title(plot_title)
    plt.legend()
    plt.grid(True)

    # Wyświetlenie wykresu
    plt.show()

except Exception as e:
    print("Wystąpił błąd:", e)
