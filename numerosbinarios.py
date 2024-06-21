def numeroBinario(numeroOriginal):
    lista = []
    copiaOriginal = numeroOriginal
    cantidadDosPotencia = 0
    if numeroOriginal < 0:
        print("Error: numero negativo.")
    else:
        while (copiaOriginal > 0):
            copiaOriginal //= 2
            cantidadDosPotencia += 1 
        # Orden ascendente (Potencias de Dos)
        for i in range(cantidadDosPotencia, -1, -1):
            dosPotencia = 2 ** i;
            if (numeroOriginal >= dosPotencia):
                numeroOriginal -= dosPotencia;
                lista.append(1)
            else:
                lista.append(0)
    lista.pop(0)
    return lista
numeroOriginal = int(input("Numero entero: "))
print(numeroBinario(numeroOriginal))