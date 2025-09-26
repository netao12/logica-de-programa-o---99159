import os 
os.system ("Cls")

# Definindo variávies
total_familia = 0
media_salarial = 0
media_filhos = 0
maior_salario = 0
menor_salario = 0 
quantidade_filhos = 0
soma_filhos = 0
while True:
    os.system("cls")
    print("""
Código   |   Descrição
   1     | Adicionar familia 
   2     | Exibir resultados e Sair
""")

    opcao = int(input("Digite a opção desejada: "))
    match opcao:
        case 1:
            # Solicitando dados.
            total_familia = int(input("Digite a quantidade de familias que responderam a pesquisa: "))
            media_filhos = int(input("Média do número de filhos: "))
            salario = float(input("Digite o valor salário: "))

            # Média de salários.
            quantidade_filhos += media_filhos 
            soma_filhos += media_filhos

            # Maior e menor idades.
            if maior_salario < menor_salario:
                menor_salario = salario

            if salario > maior_salario:
                maior_salario = salario
            
        case 2:
            media_filhos = soma_filhos / quantidade_filhos if quantidade_filhos != 0 else 0
               
            print("\n= Exibindo resultados =")
            print(f"Média de filhos: {media_filhos}")
            print(f"Menor salario: {menor_salario}")
            print(f"Maior salario: {maior_salario}")
            input("Pressione enter para continuar...")
        