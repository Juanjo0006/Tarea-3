#Se ingresa una cantidad de números 
n = int(input("Ingrese la cantidad de números que desea sumar: "))

#Se ingresan la lista de números que se desean sumar 
numeros = list(map(lambda i: int(input(f"Ingrese el número {i+1}: ")), range(n)))

suma = sum(numeros)

#Imprimir el total
print("El total de la suma es:", suma)