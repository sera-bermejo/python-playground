def obtener_datos():
    contra = input("Escriba su contraseña: ")
    return contra

def confirmar(contra):
    intentos = 0 
    while intentos < 3:
        intentos = intentos + 1
        confir_contra = input("Escriba de nuevo su contraseña: ")
        if confir_contra == contra:
            print("Contraseña confirmada. ¡Hasta la vista!")
            break
        if confir_contra != contra and intentos <= 2:
            print("Las contraseñas no coinciden. Inténtelo de nuevo.")
        elif confir_contra != contra and intentos == 3:
            print("Lo siento, no ha confirmado su contraseña. ¡Hasta la vista!")
       

def main():
    contra = obtener_datos()
    print("Tiene 3 intentos para confirmar su contraseña.")
    confirmar(contra)

main()
