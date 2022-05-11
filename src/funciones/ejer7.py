def convertirdor_distancia(distancia):
    km = distancia // 100000
    m = distancia // 100
    cm = distancia % 100
    elementos = km, m, cm
    return elementos
    
def obtener_datos():
    distancia = int(input("Escriba una distancia en centímetros: "))
    if distancia == 0:
        distancia = int(input("Escriba una distancia mayor que cero: "))
    return distancia

def main():
    distancia = obtener_datos()
    tupla = convertirdor_distancia(distancia)
    resultado = "{} centímetros son ".format(distancia)
    if tupla[0] != 0:
        resultado = resultado + "{} km, ".format(tupla[0])
    if tupla[1] != 0:
        # cuando haya km, pero no haya cm, se pone "y"
        # ej: x centímetros son x km y x m.
        if tupla[0] != 0 and tupla[2] == 0:
            resultado = resultado + "y {} m, ".format(tupla[1])
        else:    
            resultado = resultado + "{} m, ".format(tupla[1])
    if tupla[2] != 0:
        # cuando haya km o haya m, se pone "y"
        # ej: x centímetros son x km, x m y x cm o x centímetros son x m y x cm.
        if tupla[0] != 0 or tupla [1] != 0:
            resultado = resultado + "y {} cm.".format(tupla[2])
        else:
            resultado = resultado + "{} cm.".format(tupla[2])
            
    print(resultado)

main()
   