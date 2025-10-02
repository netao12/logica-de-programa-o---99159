import os
os.system("Cls") 

lista_numeros = []
pares = 0
impar = 0

QUANTIDADE_NUMEROS = 3 

print(f"Solicitando {QUANTIDADE_NUMEROS} números.")
for i in range(QUANTIDADE_NUMEROS):
    numero = float(input("Digite um número: "))
    if numero % 2 == 0:
        pares += 1
    else: 
        impar += 1 
    lista_numeros.append(numero) 

    print("\nMostrando todo os números") 
    for numero in lista_numeros:
        print(f"Número: {numero}")

    print(f"\nQuantidade de pares: {pares}") 
    print(f"Quantidade de ímpares: {impar}") 