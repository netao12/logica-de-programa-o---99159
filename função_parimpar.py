import os
os.system("Cls") 

pares = 0
impares = 0 
numero = 0
quantidade_numeros = 5 

print(f"Solicitando {quantidade_numeros} números.")
for i in range(5):
    def numeral (pares, impares , numero):
        print(f"digite um número {numero}") 
        numero = float(input("Digite um número: "))
        if numero % 2 == 0:
                pares += 1
        else: 
                impares += 1 

    numeral(pares, impares, numero) 
    for i in range:
        print(f"A quantidade de pares foram: {pares}") 
        print(f"A quantidade de impares foram: {impares}") 

