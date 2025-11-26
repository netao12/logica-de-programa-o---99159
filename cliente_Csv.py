import os
from dataclasses import dataclass
os.system("cls") 


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