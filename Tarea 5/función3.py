# Paso 1: Se solicita la lista de caracteres al usuario
lista_caracteres = list(input("Ingrese la lista de caracteres: "))

# Paso 2: Imprimir la lista original
print("La lista inicial es:", lista_caracteres)

# Paso 3: Solicitar el caracter a eliminar
caracter_a_eliminar = input("Ingrese el caracter a eliminar: ")

# Paso 4: Eliminar las ocurrencias del caracter en la lista utilizando filter() y lambda
nueva_lista = list(filter(lambda c: c != caracter_a_eliminar, lista_caracteres))

# Paso 5: Imprimir la nueva lista resultante
print("La nueva lista sin el caracter eliminado es:", nueva_lista)