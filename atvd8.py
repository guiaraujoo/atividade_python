preco_combustivel = 2.59

km_incial = int(input("Qual a quilometragem no inicio do dia? "))

km_final = int(input("Qual a quilometragem no final do dia? "))

litros_gasto = int(input("Quantos litros de combustivel foram gastos? "))

valor_recebido_passageiros = float(input("Qual o valor recebido pelos passageiros? "))

media_consumo = (km_final - km_incial) / litros_gasto

lucro_dia = valor_recebido_passageiros - (preco_combustivel * litros_gasto)

print("A média de consumo do carro foi de: {:.2f}".format (media_consumo), "km/l")

print("O lucro do dia foi de", lucro_dia, "reais")
