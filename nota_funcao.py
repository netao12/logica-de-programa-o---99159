import os
os.system("Cls")

QUANTIDADE_NOTAS = 3
notas = []

while len(notas) < QUANTIDADE_NOTAS:
    nota = float(input(f"Digite a {len(notas) + 1}ª nota (0 a 10): "))
    if 0 <= nota <= 10:
        notas.append(nota)
    else:
        print("Nota inválida! Digite um valor entre 0 e 10.")

def calcular_media(lista_notas):
    return sum(lista_notas) / len(lista_notas)

media = calcular_media(notas)

print("\nNotas digitadas:", notas)
print(f"Sua média é: {media:.2f}")