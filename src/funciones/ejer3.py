def comparador_tres_numeros(num1, num2, num3):
    numeros= {num1, num2, num3}
    if len(numeros) == 1:
        print("Ha escrito tres veces el mismo número.")
    elif len(numeros) == 2:
        print("Ha escrito uno de los números dos veces.")
    else:
        print("Los tres números que ha escrito son diferentes.")

def obtener_datos():
    num4 = int(input("Escriba el primer número: "))
    num5 = int(input("Escriba el segundo número:"))
    num6 = int(input("Escriba el tercer número:"))
    return num4, num5, num6

def main():
    gato, perro, oso = obtener_datos()
    comparador_tres_numeros(gato, perro, oso)

main()
