
#Lista para guardar los datos
lista_notas = []   

# Solicitar al usuario cuantas notas va ingresar
cantidad_notas = float(input("Ingrese la cantidad de notas a evaluar: "))

# ingresa la cantidad de notas indicadas por el usuario
for i in range(int(cantidad_notas)):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    lista_notas.append(nota) #va agregando notas a la lista


print("Nota mayor:", max(lista_notas)) #indica la nota mayor de la lista
print("Nota menor:", min(lista_notas)) #indica la nota menos de la lista
print("Promedio de notas:", f"{sum(lista_notas) / len(lista_notas):.2f}") #sacar el promedio de las notas

for i in range(len(lista_notas)): #revisa cada nota de la lista una a una
    if lista_notas[i] < 3.0:  #busca que la nota sea menos a 3.0
        lista_notas[i] = 3.0 #si la nota es menor a 3.0 la cambia dandole el valor de 3.0

#indica la nota mayor, menor, promedio y cantidad de notas actualizadas
print("Notas actualizadas:", lista_notas)
print("Promedio de notas actualizado:", f"{sum(lista_notas) / len(lista_notas):.2f}")
print("Cantidad de notas actualizadas:", len(lista_notas))