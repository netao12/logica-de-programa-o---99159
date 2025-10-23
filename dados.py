import os
os.system('cls')

from dataclasses import dataclass

@dataclass 
class pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

pessoa1 = pessoa(nome = input('\033[32mDigite seu nome\033[0m: '), 
                 idade = int(input('\033[32mDigite sua idade\033[0m: ')), 
                 peso = float(input('\033[32mDigite seu peso\033[0m: ')), 
                 altura = float(input('\033[32mDigite sua altura\033[0m: ')))

os.system('cls')
print(f'Seu nome é {pessoa1.nome}')
print(f'Sua idade é {pessoa1.idade} anos')
print(f'Seu peso é {pessoa1.peso} kg')
print(f'Sua altura é {pessoa1.altura} m')