def comparador_años(año1, año2):
    if año1 < año2:
        faltan = año2 - año1
        if faltan == 1:
            print("Para llegar al año",año2, "falta 1 año.")
        else:
            print("Para llegar al año", año2, "faltan", faltan, "años") 
    elif año1 > año2:
        han_pasado = año1 - año2
        if han_pasado == 1:
            print("Desde el año",año2, "ha pasado 1 año.")
        else:
            print("Desde el año", año2, "han pasado", han_pasado, "años")        
    else:
        print("Son el mismo año!")

def obtener_datos():
    año1 = int(input("¿En qué año estamos?: "))
    año2 = int(input("Escriba un año cualquiera: "))
    return año1, año2

def main():
    año1, año2 = obtener_datos()
    comparador_años(año1, año2)

main()
