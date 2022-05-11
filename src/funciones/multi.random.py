import random

def multi_azar():
    num1 = random.randint(2, 10)
    num2 = random.randint(2, 10)
    resultado = int(input(f"¿Cuánto es {str(num1)} x {str(num2)}?: "))
    return num1, num2, resultado

def comprobacion(n1, n2, resulta):
    resul = n1 * n2
    if resulta == resul:
        print("¡Respuesta correcta!")
    else:
        print("¡error!")

def main():
    numero1, numero2, multiplicacion = multi_azar()
    comprobacion(numero1, numero2, multiplicacion)

main()