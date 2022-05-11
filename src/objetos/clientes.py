clientes = [
    {"Nombre": "Sonia", "Apellidos": "Yago Hernández", "DNI": "22222222B"},
    {"Nombre" : "Paco", "Apellidos" : "Gómez Soriano", "DNI" : "11111111A" },
    {"Nombre" : "Manuela", "Apellidos" : "Ramirez Peter", "DNI" : "33333333C"}
    ]

def buscar_cliente(clientes, dni):
    for c in clientes:
        if dni == c["DNI"]:
            print("{} {}".format (c["Nombre"], c["Apellidos"]))
            return 
    print("Cliente no encontrado")



def borrar_cliente(clientes, dni):
    for i, c in enumerate(clientes):
        if dni == c["DNI"]:
            del(clientes[i])
            print(str(c), "> BORRADO")
            return
    print("Cliente no encontrado")

borrar_cliente(clientes, "11111111A")