import os 
os.system("Cls") 

soma = 0 
quantidade_notas = 0

while True: 

    nota = float(input("Digite una nota: "))
    quantidade_notas += 1
    soma += nota 
    resposta = int(input("Deseja inserir mais uma nota? \nDigite: '1' se SIM! \nSe não, digite um número negativo"))
    if 0 > resposta: 
        break 

media = soma / quantidade_notas 

print(f"\nMédia: {media}")