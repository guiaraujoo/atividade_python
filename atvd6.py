prestacao = int(input("Qual o total das prestações? "))
prestacao_paga = int(input("Qual a quantidade de prestações já pagas? "))
valor_prestacao = int(input("Qual o valor de cada prestação? "))

saldo_total = prestacao * valor_prestacao - prestacao_paga * valor_prestacao

falta_pagar = prestacao - prestacao_paga

print("O saldo devedor é:", saldo_total)

print("Faltam pagar:", falta_pagar, "prestações.")