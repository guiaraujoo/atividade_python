branco = int(input("Digite o número de votos brancos: "))
nulo = int(input("Digite o número de votos nulos: "))
valido = int(input("Digite o número de votos válidos: "))

total_votos = branco + nulo + valido

porcentagem_branco = (branco / total_votos) * 100

porcentagem_nulo = (nulo / total_votos) * 100

porcentagem_valido = (valido / total_votos) * 100

print(f"Porcentagem de votos brancos: {porcentagem_branco:.2f}%")

print(f"Porcentagem de votos nulos: {porcentagem_nulo:.2f}%")

print(f"Porcentagem de votos válidos: {porcentagem_valido:.2f}%")