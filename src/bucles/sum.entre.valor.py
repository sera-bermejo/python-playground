def obtener_datos():
    numero1 = int(input("Escriba un número entero positivo: "))
    while numero1 <= 0:
        numero1 = int(input("Le he pedido un número entero positivo!\nEscriba otra vez un número: "))
    numero2 = int(input(f"Escriba un número entero mayor que {str(numero1)}: "))
    while numero2 <= numero1:
        numero2 = int(input(f"¡Le he pedido un número entero mayor que {str(numero1)}!: "))    
    
    return numero1, numero2

def suma_entre_valores(num1, num2):
    valores = []
    for n in range(num1, num2+1):
        valores.append(n)
        valores_sumados = sum(valores)
    return valores_sumados

def suma_vista(numer1, numer2, valores):
    for i, n in enumerate(range(numer1, numer2+1)):
        if i == 0:
            print(n, end= "")
        else:
            print(" +",n, end= "")

    print(" =", valores)


def main():
    one, two = obtener_datos()
    res = suma_entre_valores(one, two)
    print(f"La suma desde {str(one)} hasta {str(two)} es {str(res)}.") 
    suma_vista(one, two, res)
main()