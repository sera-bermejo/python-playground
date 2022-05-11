def obtener_datos():
    num = int(input("Escriba un número entero mayor que cero: "))
    while num <= 0:
        num = int(input("¡Le he pedido un número entero mayor que cero!\nEscriba, por favor se lo pido, un número mayor: "))
    return num

def factoriales(numero):
    resultado = numero
    for n in range(numero-1, 1, -1):
        resultado *= n 
        
    return resultado

def main():
    numerito = obtener_datos()
    resulta = factoriales(numerito)
    print("El factorial de", numerito, "es", resulta)

main()
