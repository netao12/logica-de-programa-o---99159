import os 
os.system("Cls") 

login_correto = "netinhopressao@gmail.com" 
senha_correto = "neto123" 

tentativas = 1

for i in range(3):
    while True: 
        if tentativas >= 3:
            break 
        print(f"\nTentativa: {tentativas+1}")
        login = str(input("Digite o login: "))
        senha = str(input("Digite a senha: "))

        if login == login_correto and senha == senha_correto:
            print("Pode entrar aí no serviço")
            break
        else:
            print("Senha e login incorreto! Burro")
            tentativas += 1
        