import os
os.system('cls')

from dataclasses import dataclass

# CLASSE PESSOA 
@dataclass 
class pessoa:
    nome: str
    email: str
    telefone: int
    endereço: str

# SOLICITANDO RESULTADO
print('===========\033[33mSOLICITANDO INFORMAÇÕES\033[0m===========\n')
pessoa1 = pessoa(nome = input('\033[37mDigite seu nome\033[0m: '), 
                 email = input('\033[37mDigite seu email\033[0m: '), 
                 telefone = int(input('\033[37mDigite seu telefone\033[0m: ')), 
                 endereço = input('\033[37mDigite seu endereço\033[0m: '))

# MOSTRANDO RESULTADOS
os.system('cls')
print(f'Seu nome é \033[34m{pessoa1.nome}\033[0m')
print(f'Sua email é \033[35m{pessoa1.email}\033[0m')
print(f'Seu telefone é \033[36m{pessoa1.telefone}\033[0m')
print(f'Sua endereço é \033[31m{pessoa1.endereço}\033[0m')