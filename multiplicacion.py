#Se escribe sobre el mismo documento 

with open("Operaciones.txt", "a") as f:
    
        #se realiza la solicitud de n cantidad de números
    
    n=int(input("Ingrese la cantidad de números que desea multiplicar:"))

    multiplicacion = 1
    
    for i in range(n):
        numero = int(input("Ingrese el numero" + str(i+1) + ": "))
        multiplicacion *= numero
        
    print("El total de la multiplicación es : ", multiplicacion)
    
#Se escribe en el archivo operaciones

    f.write("La multiplicación de " + str(n) + "es : " + str(multiplicacion) + "\n")