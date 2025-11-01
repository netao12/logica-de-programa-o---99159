import os
os.system("Cls") 

lista_numeros = []

print("Solicitando números") 
for i in range (5):
    numero = int(input("Digite um número: ")) 
    if numero < 0:
        numero = 0
    lista_numeros.append(numero) 

print("\nExibindo resultado") 
for i, numero in enumerate (lista_numeros, start=1): 
    print(f"{i}º número: {numero}") 