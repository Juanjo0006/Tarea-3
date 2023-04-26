#Se escribe sobre el mismo documento 

with open("Operaciones.txt", "a") as f:

    #se pide al usuario ingresar los valores
    
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    
    potencia = numero1 ** numero2
    
    print("La Potencia de", numero1, "y", numero2, "es", potencia)
    
    f.write("La potencia de " + str(numero1) + " y " + str(numero2) + " es " + str(potencia) + "\n")