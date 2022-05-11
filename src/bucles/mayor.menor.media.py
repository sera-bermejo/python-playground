def obtener_datos():
    valores = int(input("¿Cuántos valores va a introducir?: "))
    while valores <= 0:
        valores = int(input("¡Imposible!\n¿Cuántos valores va a introducir?: "))
    lista = []
    for n in range(1, valores+1):
        num = float(input(f"Escriba el número {str(n)}: "))
        lista.append(num)
    return valores, lista

def el_mayor(numeros):
    aux = numeros[0]
    for n in numeros:
        if n > aux:
            aux = n
    num_mayor = aux
    return num_mayor

def el_menor(listado):
    aux = listado[0]
    for n in listado:
        if n < aux:
            aux = n
    num_menor = aux
    return num_menor

def media_aritmetica(lista_numeros):
    numeros_sumados = sum(lista_numeros)
    la_media = numeros_sumados / len(lista_numeros)
    return la_media 

def main():
    valor_intro, listita = obtener_datos()
    mayor = el_mayor(listita)
    menor = el_menor(listita)
    media = media_aritmetica(listita)
    print("El número más pequeño de los introducidos es", menor,"\nEl número más grande de los introducidos es", mayor,"\nLa media de los números introducidos es", media)
    
main()

