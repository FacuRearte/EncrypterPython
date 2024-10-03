import base64
from cryptography.fernet import Fernet
import hashlib

#transforma de texto de usuario a hash permitido para fernet
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

    #texto introducido por el usuario
    texto_usuario = input("Introduce el mensaje que quieras encriptar: ")

    #encriptado
    texto_encriptado = encriptar_texto(texto_usuario, clave)
    print(f"Texto encriptado: {texto_encriptado}")

    #desencriptado
    texto_desencriptado = desencriptar_texto(texto_encriptado, clave)
    print(f"Texto desencriptado: {texto_desencriptado}")

    input("\nSu hash ha sido satisfactorio, presione una tecla para salir.")