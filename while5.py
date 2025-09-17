import os 
os.system("Cls") 

login_correto = "netinhopressao@gmail.com" 
senha_correto = "neto123" 

while True: 
    login = str(input("Digite o login: "))
    senha = str(input("Digite a senha: "))

    if login_correto and senha_correto: 
        print("Pode entrar aí no serviço")
        break
    else:
        print("Senha e login incorreto! Burro") 
        break 