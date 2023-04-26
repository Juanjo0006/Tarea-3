#Se escribe sobre el mismo documento 

with open("Operaciones.txt", "a") as f:
    
     #se realiza la solicitud del número
    
    n=int(input("Ingrese un número:"))
    
    factorial = 1
    
    #Iteración
    for i in range(1, n+1): 
        factorial *= i
        
    #Se imprime el resultado 
    print ("El factorial de", n, "es", factorial)
    
    f.write("El factorial de " + str(n) + "es : " + str(factorial) + "\n")