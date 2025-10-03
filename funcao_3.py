import os
os.system("Cls") 

#Função com passagem de parâmetros. 
#criando uma função. 
def saudacao(nome, idade, peso, altura):
    print(f"Olá , {nome}! Bem-Vindo(a)!")
    print(f"Sua idade é {idade} anos.") 
    print(f"Seu peso {peso} em KG")
    print(f"Sua Altura {altura} em CM")

print("Solicitando Dados.")
nome = input("Digite seu nome: ") 
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite seu altura: "))
#Chamando função.
saudacao(nome, idade, peso, altura)   