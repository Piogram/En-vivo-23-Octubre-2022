#Literal a)
def encripta(entero):
    cadena = str(entero) # "1254"
    n1 = str((int(cadena[0]) + 7) % 10)
    n2 = str((int(cadena[1]) + 7) % 10)
    n3 = str((int(cadena[2]) + 7) % 10)
    n4 = str((int(cadena[3]) + 7) % 10)
    respuesta = int(n3 + n4 + n1 + n2)
    return respuesta # 2189
    
# literal b)
clave = int(input("Ingrese su clave: "))
encriptacion = encripta(clave)
print("encriptación:", encriptacion)
