import random

def multi_azar():
    num1 = random.randint(11, 99)
    num2 = random.randint(11, 99)
    resultado = int(input(f"¿Cuánto es {str(num1)} x {str(num2)}?: "))
    return num1, num2, resultado

def comprobacion(number1, number2, res):
    resul = number1 * number2
    if res == resul:
        print("¡Respuesta correcta!")
    elif res > resul - ((resul * 10) / 100):
        print("¡Ha fallado por menos del 10%!\nLa respuesta correcta era:", resul)
    elif res > resul -((resul * 30) / 100):
        print("¡Ha fallado por menos del 30%!\nLa respuesta correcta era:", resul)
    elif res < resul - ((resul * 30) / 100):
        print("¡Ha fallado por más del 30%!\nLa respuesta correcta era:", resul)

def main():
    numero1, numero2, resu = multi_azar()
    comprobacion(numero1, numero2, resu)

main()
