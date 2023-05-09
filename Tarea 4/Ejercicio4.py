def lista_tupla():
    
    entrada = input("Ingrese los números separados por coma: ")
    
    lista_valores = entrada.split()
    tupla_valores = tuple(lista_valores)

    print("La lista de valores es: ", lista_valores)
    print("La tupla de valores es: ", tupla_valores)