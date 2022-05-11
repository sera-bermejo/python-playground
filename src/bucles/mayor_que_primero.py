def obtener_datos():
    valores = int(input("¿Cuántos valores va a introducir?: "))
    while valores <= 0:
        valores = int(input("¡Imposible!\nDiga de nuevo cuántos valores quiere introducir: "))
        
    numero = int(input("Escriba un número: "))
    return valores, numero

def mayores_que_el_primero(cantidad, num):
    for n in range(1, cantidad):
        otro_num = int(input(f"Escriba un número más grande que {str(num)}: "))
        if otro_num < num:
            print(f"¡{str(otro_num)} no es más grande que {str(num)}!")
    return otro_num

def main():
    veces, nume = obtener_datos()
    mayores_que_el_primero(veces, nume)

    print("Gracias por su colaboración")

main()

