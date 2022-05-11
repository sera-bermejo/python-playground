def comparador_numeros(num1,num2):
    if num1 > num2:
        print("Menor:", num2, "Mayor:", num1)
    elif num1 < num2:
        print("Menor:", num1, "Mayor:", num2 )
    else:
        print("Los dos números son iguales")
    
def obtener_datos():
    num1 = float(input("Escriba un número: "))
    num2 = float(input("Escriba otro número: "))
    return num1, num2

def main():
    num1, num2 = obtener_datos()
    comparador_numeros(num1, num2)



main()