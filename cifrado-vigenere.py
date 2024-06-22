#Cifrado de Vigenere
claveLista = []
abecedario = "abcdefghijklmnñopqrstuvwxyz"
clave = input("Escriba la clave para el cifrado: ")
cifrado = input("Escriba la palabra a cifrar: ")
nuevaPalabra = " "

#Posicion Clave
posicionClave = 0
for j in clave.lower():
    posicionClave = abecedario.find(j)
    claveLista.append(posicionClave)

#Contadores 
contador = 0
contadorClaveLista = len(claveLista)

#Posicion Cifrado
for i in cifrado.lower():
    if i == " ":
        nuevaPalabra += " "
        continue
    #El contador no debe pasar el numero de longitud de claveLista
    #Para no causar error de indice
    if contador > contadorClaveLista - 1:
        contador = 0
    posicionCifrado = abecedario.find(i) # Posicion de las letras del cifrado
    formulaVigenere = (posicionCifrado + int(claveLista[contador])) % 27 # Letra cifrada
    nuevaLetra = abecedario[formulaVigenere] # Reemplazar la letra inicial por la cifrada
    nuevaPalabra += nuevaLetra
    contador += 1
print(nuevaPalabra)