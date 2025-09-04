import os
os.system("cls")

print("""
1-Masculino
2-Feminino 
""")

sexo = int(input("Digite o Seu sexo(1 ou 2): "))
altura = float(input("Digite sua altura(em metros): "))


if sexo == 1: 
    peso_ideal = (72.7 * altura) - 58
    print(f"\nSeu peso ídeal é: {peso_ideal:.2f} kg") 


elif sexo == 2:
    peso_ideal = (62.1 * altura) - 44.7
    print(f"\nSeu peso ídeal é: {peso_ideal:.2f} kg") 


else:
    print("\nOpção inválida! Escolha 1 ou 2") 
