numero= int(input("Escriba un número entero positivo: "))
while numero < 0:
    numero=int(input("¡Le he pedido un número entero positivo!\n Diga otro número entero positivo: "))

numero2 = int(input(f"Diga otro número mayor que {str(numero)}: "))
while numero2 < numero:
    numero2 = int(input(f"¡Le he pedido un número mayor que {str(numero)}!:"))
sumatorio= 0

for n in range (numero, numero2+1):
    sumatorio = sumatorio + n

print("La suma desde", numero, "hasta", numero2, "es", sumatorio)   
  
for i,n in enumerate(range(numero, numero2+1)):
    if i == 0:
        print(n, end= "")
    else:
        print(" +",n, end= "")

print(" =", sumatorio)

