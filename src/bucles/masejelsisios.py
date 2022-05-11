valores= int(input("¿Cuántos valores va a introducir?: "))
if valores < 0:
    valores= int(input("¡Imposible!\nVuelva a introducir los valores: "))

lista= []
for n in range(1, valores+1):
    numero= int(input(f"Escriba el número {n}: "))
    lista.append(numero)

menor= lista[0]
mayor = lista[0]

for e in lista:
    if e < menor:
        menor = e 
    if e > mayor:
        mayor = e

        

suma= sum(lista)
media = (suma)/(valores)

  


print("El número más pequeño es: ", menor)
print("El número más grande es: ", mayor)
print("La media de todos los números es: ", media)
