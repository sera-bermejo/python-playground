def crear_lista():
    lista = []
    cantidad = int(input("Diga cuántas palabras tiene la lista: "))
    for n in range(1, cantidad+1):
        palabra = input(f"Diga la palabra {str(n)}: ")
        lista.append(palabra)
    return lista

def lista_inversa(lista):
    lista_al_reves = lista[::-1]
    return lista_al_reves

def main():
    listado = crear_lista()
    print("La lista creada es:", listado)
    al_reves = lista_inversa(listado)
    print("La lista inversa es:", al_reves)

main()