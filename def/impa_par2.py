import os
os.system("Cls") 

def valor (numero):

    if numero < 0:
        print(f"{numero} negativo")
    else:
        print(f"{numero} positvo") 

numero = int(input(f"Digite um número: "))
 
valor(numero) 
 