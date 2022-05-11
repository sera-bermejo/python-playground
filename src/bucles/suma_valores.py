def obtener_datos():
    valores = int(input("¿Cuántos valores va a introducir?: "))
    while valores <= 0:
        valores = int(input("¡Imposible!\nDiga de nuevo cuántos valores introducirá: "))
    return valores

def suma_valores(cantidad):
    lista_suma = []
    for n in range(1, cantidad+1):
        numeritos = float(input(f"Escriba el número {str(n)}: "))
        lista_suma.append(numeritos)
    resultado = sum(lista_suma)
    return resultado

def main():
    val = obtener_datos()
    resu = suma_valores(val)
    print(f"La suma de todos los números que ha escrito es {str(resu)}.")

main()