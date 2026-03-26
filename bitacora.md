# Ejemplo 1

```py 
lista = []

Llenar la lista con 10 datos iguales 
 for i in range(10):
    lista.append("Hola")

Llenar la lista con 3 datos ingresados por el teclado



print(lista)
```
## ejemplo 2

```py 
lista = []

for i in range(3):
    dato = input("ingrese dato: ")
    lista.append(dato)
    
print(lista)
```
### Ejemplo 3

```py
# Datos de vuelo para un avión comercial
tiempo = [0, 10, 20, 30, 40, 50, 60]  # segundos
altitud = [0, 100, 500, 1000, 1500, 2000, 2200]  # metros
velocidad = [0, 50, 100, 150, 200, 250, 300]  # km/h
estado = ["despegue", "ascenso inicial", "ascenso", "ascenso", "ascenso", "nivelación", "crucero"]

# Imprimir informe de despegue
print("INFORME DE DESPEGUE:")
for t, a, v, est in zip(tiempo, altitud, velocidad, estado):
    print(f"T+{t}s: Altitud={a}m, Velocidad={v}km/h, Fase={est}")
``` 

### Ejemplo 4 

```py 
import random

print(random.randint(2,10))

#Crear una lista con 100 numeros aleatorios entre 100 y 200 
lista = []

for i in range(100):
    lista.append(random.randint(100, 200))
    
print(lista)
mayor = max(lista)
print(f"El numero mas grande de la lista es {mayor}")

#Implementar la funcion max usando un bucle 
indice = 0
may = lista[0]

while indice < 99:
    if may < lista[indice + 1]:
        may = lista[indice + 1 ]
    indice += 1
    
print(f"el mayor calculado a mano es: {may}")

# Calcular el menor de todos

indice = 0
men = lista[0]

while indice > 99:
    if men > lista[indice - 1]:
        men =  lista[indice - 1]
    indice -= 1
    
print(f"el menor calculado a mano es: {men}")

```