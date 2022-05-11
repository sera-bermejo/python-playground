def obtener_datos():
    valores = int(input("¿Cuántos valores va a introducir?: "))
    while valores <= 0:
        valores = int(input("¡Imposible!\nVuelva a decir cuántos valores va a introducir: "))
        
    return valores

def numeros_negativos(veces):
    num_negativos = []
    for n in range(1, veces+1):
        num = int(input(f"Escriba el número {str(n)}: "))
        if num < 0:
            num_negativos.append(num)
    return num_negativos

def main():
    datos = obtener_datos()
    cantidad = numeros_negativos(datos)
    print(f"Ha escrito {len(cantidad)} número negativos.")

main()
