import math

def area_tri(base, altura):
    area_trian = (base * altura) / 2 
    return area_trian

def area_cir(radio):
    area_circu = math.pi * (radio**2)
    return area_circu


def obtener_datos(figura):
    if figura == "a" or figura == "triángulo":
        base = float(input("Escriba la base: "))
        altura = float(input("Escriba la altura: "))
        return base, altura
    elif figura == "b" or figura == "círculo":
        radio = float(input(" Escriba el radio: "))
        return radio

def main():
    figura = input("Elija una figura geométrica:\na)Triángulo\nb)Círculo\n¿Cuál quiere calcular?: ")
    figura = figura.lower()
    if figura == "a" or figura == "triángulo":
        base, altura = obtener_datos(figura)
        area_trian = area_tri(base, altura)
        print("Un triángulo de base", base, "y altura", altura, "tiene un área de", area_trian)
    else:
        radio = obtener_datos(figura)
        area_circu = area_cir(radio)
        print("Un círculo de radio", radio, "tiene un área de", area_circu)

    
    
main()
