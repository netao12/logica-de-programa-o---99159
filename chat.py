# Lista para armazenar os participantes
participantes = []

# Pergunta quantos participantes serão cadastrados
qtd = int(input("Quantos participantes deseja cadastrar? "))

for i in range(qtd):
    print(f"\n--- Cadastro do participante {i+1} ---")

    # Cadastro das informações básicas
    nome = input("Nome: ")
    idade = int(input("Idade: "))

    estudante = input("É estudante? (s/n): ").lower() == "s"
    convite_vip = input("Possui convite VIP? (s/n): ").lower() == "s"

    print("\nTipos de ingresso disponíveis:")
    print("1 - Pista")
    print("2 - Camarote")
    print("3 - VIP")
    print("4 - Meia-entrada")

    tipo_ingresso_num = int(input("Escolha o número do ingresso: "))

    # Usando match case para traduzir o número em tipo de ingresso
    match tipo_ingresso_num:
        case 1:
            tipo_ingresso = "Pista"
        case 2:
            tipo_ingresso = "Camarote"
        case 3:
            tipo_ingresso = "VIP"
        case 4:
            tipo_ingresso = "Meia-entrada"
        case _:
            tipo_ingresso = "Inválido"

    # Regras de acesso
    acesso_liberado = (
        (tipo_ingresso == "Meia-entrada" and estudante) or
        (tipo_ingresso == "VIP") or
        (convite_vip)
    )

    # Armazena os dados em um dicionário
    participante = {
        "nome": nome,
        "idade": idade,
        "estudante": estudante,
        "convite_vip": convite_vip,
        "tipo_ingresso": tipo_ingresso,
        "acesso": "Liberado ✅" if acesso_liberado else "Negado ❌"
    }

    # Adiciona à lista principal
    participantes.append(participante)


# --- Saída final ---
print("\n===== Resumo dos Participantes =====")
for p in participantes:
    print(f"\nNome: {p['nome']}")
    print(f"Idade: {p['idade']}")
    print(f"Ingresso: {p['tipo_ingresso']}")
    print(f"Acesso: {p['acesso']}") 