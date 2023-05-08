
potencia = None

while True: 
    print("""Operaciones disponibles: 
          
          1) Sumar n cantidad de números
          2) Restar dos números
          3) Multiplicar n cantidad de números
          4) Dividir dos números
          5) Calcular el factorial de un número
          6) Elevar a la potencia un número
          7) Reiniciar
          8) Apagar""")
    
    Opcion = int(input("Escriba el número de la operación que desea realizar: "))
    
#SUMA
    if Opcion == 1:
        
#se realiza la solicitud de n cantidad de números
    
        n=int(input("Ingrese la cantidad de números que desea sumar:"))

        suma = 0
    
        for i in range(n):
                numero = int(input("Ingrese el numero" + str(i+1) + ": "))
                suma += numero
        
        print("El total de la suma es : ", suma)

#se crea un documento de texto para que contenga el registro de las operaciones que se realizan
        with open("RegistrodeOperaciones.txt", "a") as f:
                f.write("La suma de " + str(n) + "es : " + str(suma) + "\n")
        


#RESTA
    if Opcion == 2:
        
        numero1 = 0
        numero2 = 0
        
#se pide al usuario ingresar los valores
        numero1 = int(input("Ingrese el primer número: "))
        numero2 = int(input("Ingrese el segundo número: "))
    
        resta = numero1 - numero2
        print("La resta de", numero1, "y", numero2, "es", resta)
    
#Se escribe sobre el mismo documento 

        with open("RegistrodeOperaciones.txt", "a") as f:
                f.write("La resta de " + str(numero1) + " y " + str(numero2) + " es " + str(resta) + "\n")



#MULTIPLICACION 
    if Opcion == 3:
    
#se realiza la solicitud de n cantidad de números
    
        n=int(input("Ingrese la cantidad de números que desea multiplicar:"))

        multiplicacion = 1
    
        for i in range(n):
                numero = int(input("Ingrese el numero" + str(i+1) + ": "))
                multiplicacion *= numero
        
        print("El total de la multiplicación es : ", multiplicacion)
    
#Se escribe en el archivo operaciones
        
        with open("RegistrodeOperaciones.txt", "a") as f:
                f.write("El resultado de la multiplicación es: " + str(multiplicacion) + "\n")
        
#DIVISION 
    if Opcion == 4:
    
        numero1 = 0
        numero2 = 0
#se pide al usuario ingresar los valores
    
        numero1 = int(input("Ingrese el primer número: "))
        numero2 = int(input("Ingrese el segundo número: "))
    
        division = numero1 / numero2
        print("La división de", numero1, "y", numero2, "es", division)
    
#Se escribe en el archivo operaciones

        with open("RegistrodeOperaciones.txt", "a") as f:
                f.write("La division de " + str(numero1) + " y " + str(numero2) + " es " + str(division) + "\n")

#FACTORIAL
   
    if Opcion == 5:
        
    
#se realiza la solicitud del número
    
        n=int(input("Ingrese un número:"))
    
        factorial = 1
    
#Iteración
        for i in range(1, n+1): 
                factorial *= i
        
 #Se imprime el resultado 
        print ("El factorial de ",  n, "es ", factorial)

        with open("RegistrodeOperaciones.txt", "a") as f:
                f.write("El factorial de " + str(n) + "es : " + str(factorial) + "\n")

#POTENCIA 

    if Opcion == 6:


#se pide al usuario ingresar los valores
    
        numero1 = int(input("Ingrese el primer número: "))
        numero2 = int(input("Ingrese el segundo número: "))
    
        potencia = numero1 ** numero2
        
        print("La Potencia de", numero1, "y", numero2, "es", potencia)
    
    
    with open("RegistrodeOperaciones.txt", "a") as f:
        if potencia is not None: 
                f.write("La potencia da como resultado: " + str(potencia) + "\n")
        
# REINICIAR

    if Opcion == 7:
        continue
                
#APAGAR
    if Opcion == 8:
        break
