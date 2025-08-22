import os 
os.system("cls")

primeiro_numero = float(input("Digite o primeiro numero: "))
segundo_numero = float(input("Digite o segundo numero: "))

if primeiro_numero > segundo_numero:
     print ("primeiro numero maior que o segundo")
else:
    print ("segundo numero maior que o primeiro")
   
if primeiro_numero == segundo_numero: 
    print("numeros iguais")
else: 
    print("não são iguais") 

soma = primeiro_numero + segundo_numero
subtração = primeiro_numero - segundo_numero
multiplicação = primeiro_numero * segundo_numero
divisão = primeiro_numero / segundo_numero


print(f"Soma = {soma}")
print(f"Subtração = {subtração}")
print(f"Multiplicação = {multiplicação}")
print(f"Divisão = {divisão}")