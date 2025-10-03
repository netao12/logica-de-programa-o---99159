import os 
os.system("Cls") 

numero = int(input("Digite o número: ")) 

def tabuada (numero): 
    if numero:
        for i in range(1, 10+1 , 1):
            resultado = numero * i
            print(f'{numero} x {i} = {resultado}') 

print(f"O resultado é: {numero}")
tabuada(numero) 