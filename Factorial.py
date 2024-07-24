numero = int(input("Ingrese el numero a calcular: "))
factorial = 1
for contador in (1, numero+1):
    factorial = factorial * contador
print(factorial)