import os
os.system ("cls") 

nome = str(input("Digite seu nome: "))

idade = int(input("Digite sua idade: "))

estudante = str(input("Você é estudante (s/n): ")).lower () == "s"

Vip = str(input("Você possui convite vip (s/n): ")).lower () == "s" 


print(""" 
======== Tipos de Ingressos ========
             1 - Pista 
             2 - Camarote
             3 - VIP
             4 - Meia-entrada
""")

ingresso = int(input("Digite o código do Ingresso desejado: ")) 

match ingresso:
    case 1: 
         ingresso = "Pista"
    case 2:
        ingresso = "Camarote"
    case 3:
        ingresso = "VIP"
    case 4: 
        ingresso = "Meia-entrada" 

acesso_liberado = (

    (ingresso == "Meia-entrada" and estudante) or
    (ingresso == "VIP" ) or
    (Vip)
) 

resultado = {
"nome": nome,
"idade": idade,
"estudante": estudante,
"Vip": Vip,
"ingresso":ingresso,
"acesso": "Liberado ✅" if acesso_liberado else "Negado ❌"

} 
print("\n===== Resumo da compra =====")
for p in ingresso:
    print(f"\nNome: {p['nome']}")
    print(f"Idade: {p['idade']}")
    print(f"Ingresso: {p['ingresso']}")
    print(f"Acesso: {p['acesso']}") 