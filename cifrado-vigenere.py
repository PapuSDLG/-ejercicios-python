#Cifrado de Vigenere
abecedario = "abcdefghijklmnñopqrstuvwxyz"
clave = input("Escriba la clave para el cifrado: ")
cifrado = input("Escriba la palabra a cifrar: ")
nuevaPalabra = ""

#Posicion Clave
claveLista = []
posicionClave = 0
for j in clave.lower():
    posicionClave = abecedario.find(j)
    claveLista.append(posicionClave)
contadorClaveLista = len(claveLista) 

#Posicion Cifrado
contador = 0
for letra in cifrado.lower():
    # Si encuentra un espacio o caracter especial que lo agregue y no lo cifre
    if not letra.isalpha():
        nuevaPalabra += letra
        continue
    #El contador no debe pasar el numero de longitud de claveLista
    #Para no causar error de indice
    if contador > contadorClaveLista - 1:
        contador = 0
    posicionCifrado = abecedario.find(letra) # Posicion de las letras del cifrado
    formulaVigenere = (posicionCifrado + int(claveLista[contador])) % 27 # Letra cifrada
    nuevaLetra = abecedario[formulaVigenere] # Reemplazar la letra inicial por la cifrada
    nuevaPalabra += nuevaLetra
    contador += 1
print(nuevaPalabra)