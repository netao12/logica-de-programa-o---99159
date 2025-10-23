import os
os.system('cls')

from dataclasses import dataclass

@dataclass 
class pessoa:
    nome: str
    email: str
    telefone: float
    endereço: str

pessoa1 = pessoa(nome = input("Digite seu nome: "),
                 email= input("digite seu email: "),
                 telefone = float(input("Digite seu telefone:")),
                 endereço = input("Digite seu endereço:")) 

os.system("cls") 
print(f"Seu nome é:{pessoa1.nome}")
print(f"Digite é:{pessoa1.email} ")
print(f"Seu telefone:{pessoa1.telefone}")
print(f"Seu endereço:{pessoa1.endereço}") 