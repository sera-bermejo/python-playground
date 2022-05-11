def obtener_datos():
    ahorrar = float(input("¿Cuántos euros quiere ahorrar?: "))
    return ahorrar

def ahorros(ahorrar):
    meter = []
    suma_meter = 0
    while ahorrar > suma_meter:
        meter = float(input("¿Cuántos euros quire meter en la hucha?: "))
        suma_meter += meter 
    return suma_meter

def main():  
    ahorrar = obtener_datos()
    suma = ahorros(ahorrar)
    print("Objetivo conseguido! Ha ahorrado usted", suma, "euros.")

main()