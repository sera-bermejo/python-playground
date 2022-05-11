def anadir_a_lista():
    lista = []
    cantidad = int(input("¿Cuántas palabras tiene la lista?: "))
    for n in range(1, cantidad+1):
        palabra = input(f"Diga la palabra {n}: ")
        lista.append(palabra)
    
    return lista

def encontrar_en_lista(listita):
    buscar = input("Dígame la palabra a buscar: ")
    cantidad_palabra = []
    if buscar in listita:
        cantidad_palabra = listita.count(buscar)
        print("La palabra '", buscar, "' aparece", cantidad_palabra, "veces en la lista.")

    else:
        print("La palabra '", buscar, "' no está en la lista.")
    return buscar, cantidad_palabra

def main():
    listado = anadir_a_lista()
    print("la lista creada es: ", listado)
    encontrar_en_lista(listado) 
   
main()