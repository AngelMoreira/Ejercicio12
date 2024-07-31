numero = int(input("Ingrese un numero: "))
numero_limite = range(1,numero +1) 

numero_entero=""


for indice in numero_limite:
    numero_entero+= str(indice)+" "
    
print(numero_entero)
