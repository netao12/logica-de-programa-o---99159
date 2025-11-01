import os 
os.system("Cls") 

QUANTIDADE_NOTAS = 3
soma = 0
 
for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input(f"Digite a {i+1}ª nota: ")) 
        if nota < 0 or nota > 10: 
            print("A nota inválida")
        if nota >= 7:
            print("Aprovado") 
        elif nota >= 5 and nota <= 6.9:
            print("Recu")
        else: 
            print("Reprovado")

media = soma / QUANTIDADE_NOTAS

print(f"Média: {media}") 