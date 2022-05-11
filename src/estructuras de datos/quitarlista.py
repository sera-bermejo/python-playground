def lista_primera():
    lista_one = []
    cantidad = int(input("Diga cuántas palabras tiene la lista: "))
    for n in range(1, cantidad+1):
        palabra = input(f"Diga la palabra {str(n)}: ")
        lista_one.append(palabra)
    return lista_one

def lista_eliminar():
    lista_eli = []
    cantidubi = int(input("Diga cuántas palabras tiene la lista de palabras a eliminar: "))
    for n in range(1, cantidubi+1):
        palabra = input(f"Diga la palabra {str(n)}: ")
        lista_eli.append(palabra)
    return lista_eli

def nueva_lista(lista_one, lista_eli):
    lista_nueva = []
    for e in lista_one:
        if e not in lista_eli:
            lista_nueva.append(e)
    return lista_nueva


def main():
    lista_uno = lista_primera()
    print("La lista creada es:", lista_uno)
    a_eliminar = lista_eliminar()
    print("La lista de palabras a eliminar es:", a_eliminar)
    nueva = nueva_lista(lista_uno, a_eliminar)
    print("La lista ahora es:", nueva)

main()
