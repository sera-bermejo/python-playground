

numero= int(input('Diga un número entero: '))
n= 2
while n != numero:

    if numero%n == 0:
        print("no es un número primo", n, "es un divisor")
        break
    n=n+1

if n == numero:
    print("Es un número primo")
   