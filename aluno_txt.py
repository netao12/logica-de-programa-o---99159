from dataclasses import dataclass
import os
os.system("Cls") 

@dataclass
class Aluno:
    nome: str
    idade: int
    telefone: float
    email: str

QUANTIDADE_ALUNOS = 2 
lista_alunos = [] 

print("Solicitando dados do aluno.") 
for i in range(QUANTIDADE_ALUNOS):
    os.system("cls")
    aluno = Aluno(
        nome = input("Digite seu nome: "),
        idade=int(input("Digite sua idade: ")),
        telefone=float(input("Digite seu telefone: ")),
        email=input("Digite seu email: ")
    )
    lista_alunos.append(aluno)

print()
print("Salvado dados.")
arquivo = "dados_aluno.txt"

with open(arquivo, "a") as arquivo_alunos:
    for aluno in lista_alunos:
        arquivo_alunos.write(f"====Dados Aluno===\n{aluno.nome}\n{aluno.idade}\n{aluno.telefone}\n{aluno.email}\n")
    print("Salvo com sucesso!") 