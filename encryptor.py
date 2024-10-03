import base64
from cryptography.fernet import Fernet
import hashlib

# transforma de texto de usuario a hash permitido para fernet
def generar_clave_personalizada(clave_usuario):
    clave_hash = hashlib.sha256(clave_usuario.encode()).digest()  # hasheo 32 bits
    clave_fernet = base64.urlsafe_b64encode(clave_hash)  # codificar base64
    return clave_fernet

# encriptado
def encriptar_texto(texto, clave):
    fernet = Fernet(clave)
    texto_encriptado = fernet.encrypt(texto.encode())
    return texto_encriptado

# desencriptado
def desencriptar_texto(texto_encriptado, clave):
    fernet = Fernet(clave)
    texto_desencriptado = fernet.decrypt(texto_encriptado).decode() 
    return texto_desencriptado

if __name__ == "__main__":
    # clave introducida por el usuario
    clave_usuario = input("Introduzca su llave de encriptacion: ")

    # hasheo con sha256 y base64
    clave = generar_clave_personalizada(clave_usuario)

    # opción para encriptar o desencriptar
    opcion = input("¿Desea (e)ncriptar o (d)esencriptar? ").lower()

    if opcion == 'e':
        # texto introducido por el usuario para encriptar
        texto_usuario = input("Introduce el mensaje que quieras encriptar: ")

        # encriptado
        texto_encriptado = encriptar_texto(texto_usuario, clave)
        print(f"Texto encriptado: {texto_encriptado.decode()}")  # Convertir a cadena para mostrar

    elif opcion == 'd':
        # texto encriptado introducido por el usuario para desencriptar
        texto_encriptado = input("Introduce el texto encriptado (sin prefijo b'...'): ")

        try:
            # Convertir el texto encriptado a bytes utilizando base64
            texto_encriptado_bytes = texto_encriptado.encode()  # Convertir de cadena a bytes
            # Desencriptar el texto
            texto_desencriptado = desencriptar_texto(texto_encriptado_bytes, clave)
            print(f"Texto desencriptado: {texto_desencriptado}")
        except Exception as e:
            print(f"Error al desencriptar: {e}")

    else:
        print("Opción no válida. Por favor, elija 'e' para encriptar o 'd' para desencriptar.")

    input("\nPresione una tecla para salir.")
