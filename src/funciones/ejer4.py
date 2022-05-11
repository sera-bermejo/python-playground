def ano_bisiesto(ano):
    if ano % 4 == 0 and ano % 100 != 0:
        print("El año", ano, "es un año bisiesto porque es múltiplo de 4 sin ser múltiplo de 100.")
    elif ano % 400 == 0:
        print("El año", ano, "es un año bisiesto porque es múltiplo de 400.")
    else:
        print("El año", ano, "no es un año bisiesto.")

def obtener_datos():
    ano = int(input("Escriba un año y le diré si es bisiesto: "))
    return ano

def main():
    ano = obtener_datos()
    ano_bisiesto(ano)
    

main()