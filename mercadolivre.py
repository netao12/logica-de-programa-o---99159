import os
os.system("Cls")
 
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    email: str
    endereco: str

    def mostrar_dados_entrega(self):
        print(f"Nome: {pessoa1.nome}")
        print(f"Endereco: {pessoa1.endereco}")
    
    def mostrar_dados_email(self):
        print(f"nome:{pessoa1.nome}")
        print(f"email:{pessoa1.email}")

print("Solicitando os dados da pessoa.")

pessoa1 = Pessoa(nome=input("Digite seu nome: "),
                 email=input("Digite seu email: "),
                 endereco=input("Digite o seu endereço: "))



print("\n====Exibindo dados entrega====")

pessoa1.mostrar_dados_entrega()

print("\n====EXibindo dados email====")
pessoa1.mostrar_dados_email()
