def obtener_datos():
    numero1 = int(input("Escriba un número entero: "))
    numero2 = int(input(f"Escriba un número entero mayor o igual que {numero1}: "))
    while numero2 < numero1:
        numero2 = int(input("Le he pedido un número entero mayor o igual!"))
    return numero1, numero2


def par_o_impar(num1, num2):
    for n in range(num1,num2+1):
        if n % 2 == 0:
           print("El número", n, "es par")
        else:
            print("El número",n, "es impar")
    

def main():
    numerito1, numerito2 = obtener_datos()
    par_o_impar(numerito1, numerito2)

main()

