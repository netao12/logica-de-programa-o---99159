import os
os.system("Cls") 

lista_notas = [] 


for i in range (2):
    nota = float(input("Digite a nota: "))
    lista_notas.append(nota)

media = sum(lista_notas) / len(lista_notas)
if media>= 7:
        print("Aprovadinhuuu") 
else: 
        print("Reprovadinhuuuuu") 


print("\nExibindo resultado") 
print(f"Resultado: {media:.2f}") 