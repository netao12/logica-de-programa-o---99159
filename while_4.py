import os 
os.system("Cls") 

QUANTIDADE_NOTAS = 2 
soma = 0
 
for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = int(input(f"Digite a {i+1}ª nota: ")) 
        if nota >= 0 and nota <= 10:
            break
        soma = soma + nota


media = soma / QUANTIDADE_NOTAS

print(f"Média: {media}")