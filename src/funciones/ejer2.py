
def comparador_multiplos(num1, num2):
    if num1 >= num2 and num1 % num2 == 0:
        print(num1, "es múltiplo de", num2)
    elif num1 < num2 and num2 % num1 == 0:
        print(num2, "es múltiplo de", num1)
    else:
        if num1 > num2:
            print(num1,"no es múltiplo de", num2)
        else:
            print(num2, "no es múltiplo de", num1)
    return True

def obtener_datos():
    while True:
        num1 = int(input("Escriba un número: "))
        num2 = int(input("Escriba otro número: "))
        if num1 <= 0 or num2 <= 0:
            print("Este programa no admite valores negativos o nulos.")
        else: 
            break
    return num1, num2

def main():
    num1, num2 = obtener_datos()
    comparador_multiplos(num1, num2)

main()