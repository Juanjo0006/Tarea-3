
# se solicita al usuario ingresar los carácteres y la funcion separa las letras, los números y los carácteres especiales que ingresa el usuario. 
ingreso = input("Ingrese una lista de carácteres: ")

caracter = {}
letras = 0
numeros = 0
especiales = 0
    
for caracter in ingreso: 
    if caracter.isalpha():
        letras += 1
    elif caracter.isdigit():
        numeros += 1
    else: 
        especiales +=1

#Se imprimen la cantidad de caracteres que el usuario ingresó separados y ordenados. 
print(f"Letras: {letras}")
print(f"Numeros: {numeros}")
print(f"Caracteres especiales: {especiales}")
            
    
    