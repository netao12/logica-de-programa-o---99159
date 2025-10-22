from dataclasses import dataclass

@dataclass
class Pessoa:
    nome:str
    idade:str
@dataclass
class pet:
    nome:str
    idade:str

#Exemplo de uso da classe 
pessoa1 = Pessoa("Alice", 30)
pet1 = pet("Totó", 4) 

print(f"Nome: {pessoa1.nome}, idade: {pessoa1.idade}")
print(f"Nome: {pet1.nome} \nIdade: {pet1.idade}") 