#Zadanie 2

#Napisz program, który:
#Dla liczb z zakresu od 0 do 100, wyświetli te, które są podzielne przez 5.
#W następnym wierszu wyświetli te liczby podniesione do potęgi 3.

numbers = []
for i in range(1, 101):
    if i % 5 == 0:
        numbers.append(i)

print("Liczby z zakresu od 1 do 100 podzielne przez 5 to:", numbers)
cube = [number ** 3 for number in numbers]
print(f"Liczby z listy wyżej podniesione do potęgi trzeciej to {cube}")