import os
from dataclasses import dataclass
os.system("cls")



@dataclass

class Paciente:
    nome: str
    data_de_nascimento: str
    rg: float
    cpf: float
    def exibir_dados(self):
        print(f"Nome: {self.nome}\n\n Data de Nascimento: {self.data_de_nascimento}\n\n RG:{self.rg}\n\n CPF:{self.cpf}")

lista_pacientes = []
QUANTIDADE_DE_PACIENTES = 2

for i in range(QUANTIDADE_DE_PACIENTES):
    paciente = Paciente(
        nome= input("Digite seu nome: "),
        data_de_nascimento= str(input("Digite Sua Idade de Nascimeno: ")),
        rg= float(input("Digite Seu RG:")),
        cpf= float(input("Digite seu cpf: ")),
    )
    lista_pacientes.append(paciente)
    print()

nome_do_arquivo = "dados_paciente.csv"
with open(nome_do_arquivo, "a", encoding="utf-8") as arquivo_pacientes:
    for paciente in lista_pacientes:
        arquivo_pacientes.write(f"{paciente.nome}, {paciente.data_de_nascimento}, {paciente.rg}, {paciente.cpf}\n")
        print()
        print("Dados salvos com sucesso.")

# print("\nExibindo lista de pacientes: \n")

# for paciente in lista_pacientes:
#     paciente.exibir_dados()

print("\Exibindo todos os pacientes: ")
lista = []
try:
    # "r" - Read - leitura
    with open(nome_do_arquivo, "r", encoding="utf-8") as arquivo:
        lista_todos_pacientes = arquivo.readlines()
        for paciente in lista_todos_pacientes: 
            nome, data_de_nascimento, rg, cpf = paciente.strip().split(",")
            dados_paciente = Paciente(nome=nome, data_de_nascimento=str, rg=float, cpf=float(cpf))
            lista.append(dados_paciente)
    for paciente in lista:
        paciente.exibir_dados()
except FileNotFoundError:

    print("Erro, arquivo não encontrado")