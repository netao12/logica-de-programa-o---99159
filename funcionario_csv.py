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