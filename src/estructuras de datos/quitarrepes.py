def lista_primera():
    lista_one = []
    cantidad = int(input("Diga cuántas palabras tiene la lista: "))
    for n in range(1, cantidad+1):
        palabra = input(f"Diga la palabra {str(n)}: ")
        lista_one.append(palabra)
    return lista_one

def nueva_lista(lista_uno):
    lista_nueva = []
    for e in lista_uno:
        if e not in lista_nueva:
            lista_nueva.append(e)
    return lista_nueva

def main():
    primera_lista = lista_primera()
    print("La lista creada es:", primera_lista)
    nueva = nueva_lista(primera_lista)
    print("La lista sin repeticiones es:", nueva)

main()

