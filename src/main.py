def main():
    print("¡Hola! Este es el inicio del proyecto de recuperación de contraseña.")

if __name__ == "__main__":
    main()

# Función que valida si un correo tiene formato básico válido
def es_correo_valido(correo):
    # Verifica que el correo tenga un '@' y un punto después del '@'
    if "@" in correo and "." in correo.split("@")[-1]:
        return True
    else:
        return False

# Función que valida si la contraseña cumple con los requisitos mínimos
def es_contrasena_valida(contrasena):
    # Verifica longitud mínima 8 caracteres
    if len(contrasena) < 8:
        return False
    # Verifica que tenga al menos una letra
    tiene_letra = any(c.isalpha() for c in contrasena)
    # Verifica que tenga al menos un número
    tiene_numero = any(c.isdigit() for c in contrasena)
    return tiene_letra and tiene_numero

def main():
    print("🔐 Recuperación de contraseña")

    # Pide al usuario que ingrese su correo y valida el formato
    correo = input("Ingresa tu correo: ")
    while not es_correo_valido(correo):
        print("Correo no válido. Intenta de nuevo.")
        correo = input("Ingresa tu correo: ")

    print(f"Enviando código de verificación a {correo}...")

    # Código fijo para validar (en la vida real se enviaría un código dinámico)
    codigo_verificacion = "6204"  

    intentos = 3  # Número de intentos permitidos para ingresar el código
    while intentos > 0:
        codigo_ingresado = input("Introduce el código que recibiste: ")
        if codigo_ingresado == codigo_verificacion:
            # Si el código es correcto, pide la nueva contraseña
            nueva_contrasena = input("Ingresa tu nueva contraseña: ")
            # Valida que la contraseña cumpla los requisitos mínimos
            while not es_contrasena_valida(nueva_contrasena):
                print("Contraseña no válida. Debe tener al menos 8 caracteres, una letra y un número.")
                nueva_contrasena = input("Ingresa tu nueva contraseña: ")
            print("✅ Contraseña cambiada con éxito.")
            break
        else:
            intentos -= 1
            if intentos > 0:
                print(f"Código incorrecto. Te quedan {intentos} intentos.")
            else:
                print("Se agotaron los intentos. Intenta más tarde.")

if __name__ == "__main__":
    main()
