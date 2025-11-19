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
        print(f"\nNome: {self.nome}\nData de Nascimento: {self.data_de_nascimento}\nRG: {self.rg}\nCPF: {self.cpf}\n")


lista_pacientes = []
QUANTIDADE_DE_PACIENTES = 1

for i in range(QUANTIDADE_DE_PACIENTES):
    paciente = Paciente(
        nome=input("Digite seu nome: "),
        data_de_nascimento=input("Digite sua data de nascimento: "),
        rg=float(input("Digite seu RG: ")),
        cpf=float(input("Digite seu CPF: "))
    )
    lista_pacientes.append(paciente)
    print()


nome_do_arquivo = "dados_paciente.csv"

# Salvando
with open(nome_do_arquivo, "a", encoding="utf-8") as arquivo_pacientes:
    for paciente in lista_pacientes:
        arquivo_pacientes.write(f"{paciente.nome},{paciente.data_de_nascimento},{paciente.rg},{paciente.cpf}\n")

print("Dados salvos com sucesso.\n")



# -----------------------------
#     LENDO o arquivo
# -----------------------------
print("Exibindo todos os pacientes:")

lista = []

try:
    with open(nome_do_arquivo, "r", encoding="utf-8") as arquivo:
        lista_todos_pacientes = arquivo.readlines()

        for linha in lista_todos_pacientes:
            nome, data_nascimento, rg, cpf = linha.strip()
            for linha in linha.split(","):
                dados_paciente = Paciente(
                    nome=nome,
                    data_de_nascimento=data_nascimento,
                    rg=float(rg),
                    cpf=float(cpf)
                )

            lista.append(dados_paciente)

    # Exibir tudo
    for paciente in lista:
        paciente.exibir_dados()

except FileNotFoundError:
    print("Erro: arquivo não encontrado.")