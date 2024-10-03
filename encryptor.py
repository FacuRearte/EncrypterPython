import base64
from cryptography.fernet import Fernet
import hashlib

#transforma de texto de usuario a hash 32 bits para luego codificarlo a base64 y que lo acepte fernet
def generar_clave_personalizada(clave_usuario):
    clave_hash = hashlib.sha256(clave_usuario.encode()).digest()  #hasheo 32 bits
    clave_fernet = base64.urlsafe_b64encode(clave_hash)  #codificar base64
    return clave_fernet

#encriptado
def encriptar_texto(texto, clave):
    fernet = Fernet(clave)
    texto_encriptado = fernet.encrypt(texto.encode())
    return texto_encriptado

#desencriptado
def desencriptar_texto(texto_encriptado, clave):
    fernet = Fernet(clave)
    texto_desencriptado = fernet.decrypt(texto_encriptado).decode() 
    return texto_desencriptado

if __name__ == "__main__":
    #clave introducida por el usuario
    clave_usuario = input("Introduzca su llave de encriptacion: ")

    #hasheo con sha256 y base64

    clave = generar_clave_personalizada(clave_usuario)

    #opcion para encrypt o decrypt
    opcion = int(input("Presione '1' para encriptar o '2' para desencriptar\n"))

    if opcion == 1:
        #texto a encriptar
        texto_usuario = input("Introduce el mensaje que quieras encriptar: \n")

        #encriptado
        texto_encriptado = encriptar_texto(texto_usuario, clave)
        print(f"\nSu texto encriptado es: {texto_encriptado.decode()}\n")

    elif opcion == 2:
        #texto encriptado por el usuario
        texto_encriptado = input("Introduce el texto encriptado (sin prefijo b'...'): ")

        try:
            #convertir el texto encriptado a bytes utilizando base64
            texto_encriptado_bytes = texto_encriptado.encode()  # Convertir de cadena a bytes
            #Desencriptar los bytes con la key
            texto_desencriptado = desencriptar_texto(texto_encriptado_bytes, clave)
            print(f"\nSu texto desencriptado es: {texto_desencriptado}\n")
        except Exception as e:
            print(f"Hubo un error: {e}")

    else:
        print("Opción no válida. Por favor, elija 'e' para encriptar o 'd' para desencriptar.\n")

    print("Gracias por usar el programa, hecho por Facundo Rearte 2024")
    input("\nPresione una tecla para cerrar")
