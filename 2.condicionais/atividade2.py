import os 
os.system("cls") 

segunda_nota= float(input("Digite a primeira nota "))
primeira_nota= float(input("Digite a segunda nota "))

media = (primeira_nota + segunda_nota) / 2

if media >= 7: 
    resultado = "Aprovado"
else:
    resultado = "Reprovado"

print(f"Média: {media}")
print(f"Resultado: {resultado}") 
