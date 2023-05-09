lista = input("Ingrese una lista separada por comas: ").split(",")
caracter = input("Ingrese un carácter a eliminar: ")

while caracter in lista:
    lista.remove(caracter)
