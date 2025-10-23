import os
os.system("Cls")
 
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    email: str
    endereco: str

    def mostrar_dados_entrega(self):
        print(f"Nome: {self.nome}")
        print(f"Endereco: {self.endereco}")
        print(f"Email: {self.email}") 
    
    def mostrar_dados_email(self):
        print(f"nome:{self.nome}")

    def mostrar_dados_entrega(self):
        print(f"Nome: {self.nome}")
        print(f"Endereco: {self.endereco}")
        print(f"Email: {self.email}") 
    
    def mostrar_dados_email(self):
        print(f"nome:{self.nome}")
    

print("Solicitando os dados da pessoa.")

pessoa1 = Pessoa(nome=input("Digite seu nome: "),
                 email=input("Digite seu email: "),
                 endereco=input("Digite o seu endereço: "))
pessoa2 = Pessoa(nome=input("Digite seu nome: "),
                 email=input("Digite seu email: "),
                 endereco=input("Digite o seu endereço: "))



print("\n====Exibindo dados email====")

pessoa1.mostrar_dados_entrega()

pessoa2.mostrar_dados_entrega()

print("\n====EXibindo dados nome====")
pessoa1.mostrar_dados_email()

pessoa2.mostrar_dados_email()
