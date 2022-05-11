def lista_primera():
    lista_one = []
    cantidad = int(input("Diga cuántas palabras tiene la primera lista: "))
    for n in range(1, cantidad+1):
        palabra = input(f"Diga la palabra {str(n)}: ")
        lista_one.append(palabra)
    return lista_one

def lista_segunda():
    lista_two = []
    cantidad = int(input("Diga cuántas palabras tiene la segunda lista: "))
    for n in range(1, cantidad+1):
        palabra = input(f"Diga la palabra {str(n)}: ")
        lista_two.append(palabra)
    return lista_two

def sin_repetir(lista: list) -> list:

    return list(set(lista))

def en_las_dos(lista_uno, lista_dos):
    las_dos = []
    for e in lista_uno:
        if e in lista_dos:
            las_dos.append(e)
    return sin_repetir(las_dos)

def en_primera(lista_one, lista_two):
    solo_primera = []
    for e in lista_one:
        if e not in lista_two:
            solo_primera.append(e)
    return sin_repetir(solo_primera)

def en_segunda(lista1, lista2):
    solo_segunda = []
    for e in lista2:
        if e not in lista1:
            solo_segunda.append(e)
    return sin_repetir(solo_segunda)

def todas(primeri, segundi):
    todas_las_listas = []
    for e in primeri:
        todas_las_listas.append(e)
    for e in segundi:
        todas_las_listas.append(e)
    return sin_repetir(todas_las_listas)
    
def main():
    primer = lista_primera()
    print("La primera lista es:", primer)
    segun = lista_segunda()
    print("La segunda lista es:", segun)
    en_dos = en_las_dos(primer, segun)
    print("Palabras que aparecen en las dos listas:", en_dos)
    solo_una = en_primera(primer, segun)
    print("Palabras que solo aparecen en la primera lista:", solo_una)
    solo_dos = en_segunda(primer, segun)
    print("Palabras que solo aparecen en la segunda lista:", solo_dos)
    en_todas = todas(primer, segun)
    print("Todas las palabras:", en_todas)

main()