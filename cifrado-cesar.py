# Cifrado Cesar
abecedario = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
palabra = input("Ingresa una palabra: ")
nuevaPalabra = " "
for letra in palabra:
    if letra == " ":
        nuevaPalabra += " "
    else:
        nuevaPosicion = abecedario.find(letra) + 3
        nuevaLetra = abecedario[nuevaPosicion]
        nuevaPalabra += nuevaLetra
    
print("El cifrado de la palabra:", palabra)
print("", nuevaPalabra)