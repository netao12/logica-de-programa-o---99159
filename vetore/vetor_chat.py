import os
os.system("CLs") 

lista_valores = [] 
negativo = []
positivo = []
zero = [] # Criamos uma lista específica para os zeros

QUANTIDADE_NUMEROS = 5

print(f"Solicitando {QUANTIDADE_NUMEROS} números.")

for i in range(QUANTIDADE_NUMEROS): 
    try:
        # Pede e converte o número para float
        numero = float(input(f"Digite o {i+1}º número: ")) 
        
        # Adiciona à lista geral
        lista_valores.append(numero)
        
        # --- A CORREÇÃO DE LÓGICA É AQUI ---
        # Se for MAIOR que 0, é positivo.
        if numero > 0:
            positivo.append(numero)
        # Se for MENOR que 0, é negativo.
        elif numero < 0:
            negativo.append(numero)
        # Se NÃO for nem maior nem menor que 0, é 0.
        else:
            zero.append(numero)
            
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        # Isso faz com que o loop repita a entrada atual
        i -= 1 

print("\n===== Resultado =====")

# 1. CORREÇÃO do print
# Você deve usar len() na *lista* 'negativo' para saber quantos elementos tem.
print(f"Quantidade de números negativos: {len(negativo)}")     
print(f"Quantidade de números positivos: {len(positivo)}")
print(f"Quantidade de zeros: {len(zero)}")