
import os 
os.system ("cls") 

print("""
Código \t prato \t\t\t valor
    1 \t Picanha \t\t R$ 25,00
    2 \t Lasanha \t\t R$ 20,00
    3 \t Strogonoff \t\t R$ 18,00
    4 \t Bife Acebolado \t R$ 15,00
    5 \t Pão com ovo \t\t R$ 5,00
""")

codigo = int(input("Digite o código do prato desejado: ")) 

match codigo:
    case 1:
        print("Você escolheu; Picanha no valor R$25,00, Boa Refeição!")
    case 2:
        print("Você escolheu; Lasanha no valor R$20,00, Boa Refeição!")
    case 3:
        print("Você escolheu; Strogonoff no valor R$18,00, Boa Refeição!")
    case 4:
        print("Você escolheu; Bife Acebolado no valor R$15,00, Boa Refeição!")
    case 5:
        print("Você escolheu; Pão com ovo no valor R$5,00, Boa Refeição!") 
    case _:
        print("Opção invalidada") 
        
