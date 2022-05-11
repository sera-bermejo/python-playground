def ecuacion(a, b):
    if a == 0 and b == 0:
        print("Todos los números son solución.")
    elif a == 0 and b != 0 :
        print("La ecuación no tiene solución.")
    else:
        print("La ecuación tiene una solución:",- b / a)
    

def obtener_datos():
    a = float(input("Escriba el valor del coeficiente a: "))
    b = float(input("Escriba el valor del coeficiente b: "))
    return a, b

def main():
    a, b = obtener_datos()
    ecuacion(a, b)

main()
