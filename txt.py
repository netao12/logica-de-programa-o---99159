import os
os.system("Cls") 

# texto que desejo salvar
texto = input("Digite seu nome: ")

# Definir nome do arquivo para salvar
nome_arquivo = "exemplo.txt" 

# Comando para salvar.
with open(nome_arquivo, "a") as meu_arquivo:
    meu_arquivo.write(f"{texto}\n")
    print("Salvo com sucesso!") 