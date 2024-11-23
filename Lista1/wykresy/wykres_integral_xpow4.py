import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#wczytywanie danych
data = pd.read_csv("/home/vostok/codes/MPiS/Lista1/integral_xpow4/integral_xpow4.txt", sep=",", names=["attempt", "points", "estimate"], skiprows = 1)

#grupowanie danych po liczbie punktow i obliczanie srednich wartosci przyblizen calki
mean_integral_values = data.groupby("points")["estimate"].mean()
points = np.array(mean_integral_values.index)
mean_values = np.array(mean_integral_values.values)

#tworzenie wykresu
plt.figure(figsize=(10, 6))

plt.scatter(data["points"], data["estimate"], color='blue', s=5, alpha=0.5, label="punkty")

#Linia srednich wartosci
#plt.plot(points, mean_values, color='green', linewidth=2, label='Srednia')

#czerwone punkty dla srednich wartosci dla kazdej liczby punktow
plt.scatter(points, mean_values, color='red', s=50, zorder=5, label="Srednie wartosc")

#dodanie linii poziomej dla rzeczywistej wartosci calki = 12
plt.axhline(y=0.2, color='orange', linestyle='--', linewidth=1.5, label="y = 0.2")

# Dodanie etykiet i tytułu
plt.xlabel("Liczba punktów")
plt.ylabel("Oszacowanie calki")
plt.title("Wykres oszacowania calki $\\int_0^1 4x(1 - x)^3 dx$ dla k = 50")
plt.legend()
plt.grid(True)
plt.show()
