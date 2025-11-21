import os
os.system("CLS")

from dataclasses import dataclass

@dataclass
class Paciente:
    nome: str
    idade: int
    peso: float
    altura: float
    cpf: str

    def exibir_dados(self):
        print(f"Nome: {self.nome} | Idade: {self.idade} | Peso: {self.peso} | Altura: {self.altura} | CPF: {self.cpf}")


lista_de_pacientes = []
QUANTIDADE_DE_PACIENTES = 2

for i in range(QUANTIDADE_DE_PACIENTES):
    paciente = Paciente(
        nome=input("Digite seu nome: "),
        idade=int(input("Digite sua idade: ")),
        peso=float(input("Digite seu peso: ")),
        altura=float(input("Digite sua altura: ")),
        cpf=str(input("Digite seu cpf: "))
    )
    lista_de_pacientes.append(paciente)
    print()

nome_do_arquivo = "dados_pacientes.csv"

# Salvando de forma correta
with open(nome_do_arquivo, "a") as arquivo_pacientes:
    for paciente in lista_de_pacientes:
        arquivo_pacientes.write(
            f"{paciente.nome},{paciente.idade},{paciente.peso},{paciente.altura},{paciente.cpf}\n"
        )

print("Dados salvos com sucesso.")

# Lendo de volta
print("\nExibindo todos os pacientes:\n")
try:
    with open(nome_do_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(f"- {linha.strip()}")
except FileNotFoundError:
    print("O arquivo não foi encontrado.")