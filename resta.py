#Se escribe sobre el mismo documento 

with open("Operaciones.txt", "a") as f:
    
    #se pide al usuario ingresar los valores
    
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    
    resta = numero1 - numero2
    print("La resta de", numero1, "y", numero2, "es", resta)
    
    #Se escribe en el archivo operaciones

    f.write("La resta de " + str(numero1) + " y " + str(numero2) + " es " + str(resta) + "\n")