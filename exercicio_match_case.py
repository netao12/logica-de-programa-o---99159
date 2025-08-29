import os
os.system("cls") 

primeiro_numero = float(input("Digite o primeiro numero: "))
segundo_numero = float(input("Digite o segundo numero: "))

operação = str(input("digite qual operaçao você deseja: +, -, /, *"))


soma  = primeiro_numero + segundo_numero 
subtração = primeiro_numero - segundo_numero
multiplicação = primeiro_numero * segundo_numero
divisão = primeiro_numero / segundo_numero

match operação:
    case "+":
        print(f"{soma}")
    case "-":
        print(f"{subtração}")
    case "*": 
        print(f"{multiplicação}")
    case "/":
        print(f"{divisão}") 
    case _:
        print("Opção inválidada")
    

