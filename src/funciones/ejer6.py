import math

def calculo_areas(elementos):
    if len(elementos) == 2:
        area_tri = (elementos[0] * elementos[1]) / 2 
        return area_tri
    elif len(elementos) == 1:
        area_cir = math.pi * (elementos[0]**2)
        return area_cir


def obtener_datos():
    figura = input("Elija una figura geométrica:\na)Triángulo\nb)Círculo\n¿Cuál quiere calcular?: ")
    figura = figura.lower()
    if figura == "a" or figura == "triángulo":
        base = float(input("Escriba la base: "))
        altura = float(input("Escriba la altura: "))
        return (base, altura)
    elif figura == "b" or figura == "círculo":
        radio = float(input(" Escriba el radio: "))
        return [radio]

def main():
    elementos_figura = obtener_datos()
    area = calculo_areas(elementos_figura)
    if len(elementos_figura) == 2:
        print("Un triángulo de base", elementos_figura[0],"y altura", elementos_figura[1], "tiene un área de", area ) 
    else:
        print("Un círculo de radio", elementos_figura[0], "tiene un área de", area)
    
main()
