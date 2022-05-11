def crear_lista():
    lista = []
    cantidad = int(input("Diga cuántas palabras tiene la lista: "))
    for n in range(1, cantidad+1):
        palabra = input(f"Diga la palabra {str(n)}:")
        lista.append(palabra)
    return lista

def sustituir_palabra(listado):
    sustituir = input("Sustituir la palabra: ")
    por_cual = input("por la palabra: ")
    for index in range(len(listado)):
        if listado[index] == sustituir:
            listado[index] = por_cual
    
    nueva_lista = listado
    return nueva_lista

def main():
    listita = crear_lista()
    print("La lista creada es", listita)
    nueva = sustituir_palabra(listita)
    print("La lista ahora es:", nueva)

main()
