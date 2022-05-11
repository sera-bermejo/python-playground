def obtener_datos():
    num = int(input("Escriba un número entero mayor que cero: "))
    while num <= 0:
        num = int(input("!Le he pedido un número entero mayor que cero!"))
    return num

def es_divisor(numero):
    divisores = []
    for n in range(1, numero+1):
        if numero % n == 0:
            divisores.append(n)
    return divisores

def main():
    numero_usuario = obtener_datos()
    divisores = es_divisor(numero_usuario)
    divisores_str = str(divisores)[1:-1]
    print("Los divisores de", numero_usuario, "son", (divisores_str))

main()
    


    


