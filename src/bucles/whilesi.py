def check(c, r):
    if c==r:
        print("Contraseña confirmada. Hasta la vista!")
    return c==r
    
while True:
    contrasena = input("Escriba su contraseña: ")
    repita = input("Escriba de nuevo su contraseña: ")  
    if check(contrasena,repita):
        break
    print("Las contraseñas no coinciden. Inténtelo de nuevo.")
    repita = input("Escriba de nuevo su contraseña: ") 