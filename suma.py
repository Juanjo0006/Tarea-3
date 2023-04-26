
#se crea un documento de texto para que contenga el registro de las operaciones que se realizan

with open("Operaciones.txt", "a") as f: 
    
    #se realiza la solicitud de n cantidad de números
    
    n=int(input("Ingrese la cantidad de números que desea sumar:"))

    suma = 0
    
    for i in range(n):
        numero = int(input("Ingrese el numero" + str(i+1) + ": "))
        suma += numero
        
    print("El total de la suma es : ", suma)
    
#Se escribe en el archivo operaciones

    f.write("La suma de " + str(n) + "es : " + str(suma) + "\n")

