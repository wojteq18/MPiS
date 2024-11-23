import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Wczytanie danych z pliku `pi_aprox.txt` i odpowiednie nazwanie kolumn
data = pd.read_csv("/home/vostok/codes/MPiS/Lista1/pi_aprox/pi_aprox.txt", sep=",", names=["attempt", "points", "estimate"], skiprows=1)

# Sprawdzenie struktury danych
print(data.head())  # Wyświetla pierwsze kilka wierszy
print(data.columns)  # Wyświetla listę kolumn

# Grupowanie danych po liczbie punktów i obliczanie średnich wartości przybliżeń liczby pi
mean_pi_values = data.groupby("points")["estimate"].mean()
points = np.array(mean_pi_values.index)      # Konwersja do numpy array
mean_values = np.array(mean_pi_values.values)  # Konwersja do numpy array

# Tworzenie wykresu
plt.figure(figsize=(10, 6))

# Wszystkie punkty jako wykres punktowy
plt.scatter(data["points"], data["estimate"], color='blue', s=5, alpha=0.5, label="Punkty")

# Linia średnich wartości
#plt.plot(points, mean_values, color='green', linewidth=2, label="Średnia")

# Czerwone punkty dla średnich wartości dla każdej liczby punktów
plt.scatter(points, mean_values, color='red', s=50, zorder=5, label="Średnie co liczba punktów")

# Dodanie linii poziomej dla rzeczywistej wartości liczby pi
plt.axhline(y=np.pi, color='orange', linestyle='--', linewidth=1.5, label="π")

# Dodanie etykiet i tytułu
plt.xlabel("Liczba punktów")
plt.ylabel("Oszacowanie liczby π")
plt.title("Wykres oszacowania liczby π dla k = 50")
plt.legend()
plt.grid(True)
plt.show()
