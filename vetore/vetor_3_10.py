import os
os.system("Cls") 

lista_valores = [] 
negativo = []
positivo = []
zero = []

QUANTIDADE_NUMEROS = 5

print(f"Solicitiando {QUANTIDADE_NUMEROS} números.")

for i in range (QUANTIDADE_NUMEROS): 

        numero = float(input(f"Digite o{i+1}º número: ")) 
        lista_valores.append(numero)
        if numero < 0:
            positivo.append(numero) 
        elif numero < 0:
            negativo.append(numero)
        else:
            zero.append(numero)

for numero in lista_valores:
    print("\n=====Resultado====")
    print(f"número negativo: {len(negativo)}")     
    print(f"número positivo: {len(positivo)}")     