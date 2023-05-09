
# se solicita al usuario ingresar los carácteres y la funcion separa y ordena la cantida de caracteres iguales en una string
caracteres = input("Ingrese una palabra: ")
    
contador = {}
for caracter in caracteres:
    if caracter in contador:
        contador[caracter] += 1
    else:
        contador[caracter] = 1
        
# Se imprime la lista de la cantidad de caracteres del input
print(contador)