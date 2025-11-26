import os
from dataclasses import dataclass

os.system("cls" if os.name == "nt" else "clear")


@dataclass
class Funcionario:
    nome: str
    data_admissao: float
    matricula: float
    endereco: str

    def exibir_dados(self):
        print(f"nome: {self.nome}\n"
              f"data_admissao: {self.data_admissao}\n"
              f"matricula: {self.matricula}\n"
              f"endereco: {self.endereco}\n")


# Cadastro
lista_funcionario = []
QUANTIDADE_FUNCIONARIO = 3

for i in range(QUANTIDADE_FUNCIONARIO):
    func = Funcionario(
        nome=input("Digite seu nome: "),
        data_admissao=float(input("Digite a Data de Admissão: ")),
        matricula=float(input("Digite sua Matrícula: ")),
        endereco=input("Digite seu Endereço: ")
    )
    lista_funcionario.append(func)
    print()

# Salvando CSV
nome_do_arquivo = "dados_funcionario.csv"

with open(nome_do_arquivo, "a", encoding="utf-8") as arquivo_funcionario:
    for func in lista_funcionario:
        arquivo_funcionario.write(f"{func.nome},{func.data_admissao},{func.matricula},{func.endereco}\n")

print("\nDados salvos com sucesso.\n")

# Leitura do CSV
print("Exibindo todos os funcionários:\n")
lista = []

try:
    with open(nome_do_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, data_admissao, matricula, endereco = linha.strip().split(",")
            func = Funcionario(
                nome=nome,
                data_admissao=float(data_admissao),
                matricula=float(matricula),
                endereco=endereco
            )
            lista.append(func)

    for func in lista:
        func.exibir_dados()

except FileNotFoundError:
    print("Erro: arquivo não encontrado.") 

from dataclasses import dataclass


#   CLASSE CLIENTE
# =========================
@dataclass
class Cliente:
    nome: str
    data_de_nascimento: str
    endereco: str

    def exibir_dados(self):
        print(f"Nome: {self.nome}\n"
              f"Data de Nascimento: {self.data_de_nascimento}\n"
              f"Endereço: {self.endereco}\n")

#   CADASTRO DE CLIENTES
# =========================
lista_clientes = []
QUANTIDADE_CLIENTES = 3

for i in range(QUANTIDADE_CLIENTES):
    print(f"\nCadastro do cliente {i+1}:")
    cliente = Cliente(
        nome=input("Digite o nome do cliente: "),
        data_de_nascimento=input("Digite a data de nascimento (DD/MM/AAAA): "),
        endereco=input("Digite o endereço: ")
    )
    lista_clientes.append(cliente)
    print()


#   SALVANDO EM CSV
# =========================
nome_arquivo_clientes = "dados_clientes.csv"

with open(nome_arquivo_clientes, "a", encoding="utf-8") as arquivo:
    for cliente in lista_clientes:
        arquivo.write(f"{cliente.nome},{cliente.data_de_nascimento},{cliente.endereco}\n")

print("\nDados dos clientes salvos com sucesso!\n")

#   LEITURA DO CSV
print("Exibindo todos os clientes cadastrados:\n")

lista_lida = []

try:
    with open(nome_arquivo_clientes, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, data_nasc, endereco = linha.strip().split(",")
            cliente = Cliente(
                nome=nome,
                data_de_nascimento=data_nasc,
                endereco=endereco
            )
            lista_lida.append(cliente)

    for cliente in lista_lida:
        cliente.exibir_dados()

except FileNotFoundError:
    print("Erro: arquivo de clientes não encontrado.")