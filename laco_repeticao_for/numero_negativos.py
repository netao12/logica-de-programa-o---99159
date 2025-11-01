import os 
os.system("Cls") 

negativos = []
positivos = []

QUANTIDADE_NUMEROS = 3

print(f"Solicitiando {QUANTIDADE_NUMEROS} números.")
for i in range(QUANTIDADE_NUMEROS):
    numero = float(input(f"Digite o{i+1}º número: ")) 
    if numero > 0:
        negativos.append(numero) 
    else:
        positivos.append(numero)

print("\n=====Resultado====")
print(f"número negativo: {len(negativos)}")         
print(f"soma dos números positivos: {sum(positivos):.0f}") 
