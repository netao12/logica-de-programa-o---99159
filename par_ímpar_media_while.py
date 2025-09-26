import os
os.system("Cls") 

pares = 0
ímpares = 0 
soma_pares = 0 
soma_geral = 0 
contador_geral = 0 

while True:

        numero = int(input("Digite o numero: ")) 
        if numero >= 0:
            contador_geral += 1
            soma_geral += numero 
            if numero % 2 == 0:
                pares += 1
                soma_pares += numero
            else: 
                ímpares += 1 
        if numero == 0:
            break
#Calculando. 
#operação ternária.
media_pares = soma_pares / pares if pares != 0 else 0
media_geral = soma_geral / contador_geral if contador_geral != 0 else 0

#Exibindo resultados .
print(f"\nQuantidade de pares: {pares}")
print(f"\nQuantidade de ímpares: {ímpares}")
print(f"Média de números pares: {media_pares}")
print(f"Média Geral: {media_geral}")
        
              
        