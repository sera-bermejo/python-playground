valores=int(input("¿Cuántos valores va a introducir?: "))

contador_pares= 0


for v in range (1,valores +1):
    num= int(input(f"Diga el valor de {v}: "))
    if num % 2 == 0:
        contador_pares= contador_pares+1 
  

print("ha escrito", contador_pares, "números pares y", valores-contador_pares, "números impares")
print("Gracias por su colaboración")