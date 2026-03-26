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

