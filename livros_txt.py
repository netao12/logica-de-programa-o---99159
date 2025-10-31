from dataclasses import dataclass
import os
os.system("Cls") 

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preco: float

QUANTIDADE_livro = 3
lista_livro = [] 

print("Solicitando dados dos livros") 
for i in range(QUANTIDADE_livro):
    os.system("cls")
    livro = Livro(
        nome = input("Digite o nome do Livro: "),
        autor=str(input("Digite o Autor: ")),
        categoria=input("Digite a Categoria: "),
        preco=float(input("Digite o Preço: ")),
    )
    
    
    lista_livro.append(livro)

print()
print("Salvado dados.")
arquivo = "dados_livro.txt"

with open(arquivo, "a") as arquivo_livros:
    for aluno in lista_livro:
        arquivo_livros.write(f"====Dados livro====\n{livro.nome}\n{livro.autor}\n{livro.categoria}\n{livro.preco}\n") 
    print("Dados salvo com sucesso")