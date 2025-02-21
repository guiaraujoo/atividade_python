quilometragem_inicial = int(input("Diga sua quilometragem inicial: "))
quilometragem_final = int(input("Diga sua quilometragem final: "))
litros_cunsumidos = float(input("Diga quantos litros de gasolina você usou: "))
preco_combustivel = float(input("Diga o preço do combustível: "))

distancia_percorrida = quilometragem_final - quilometragem_inicial

valor_total_gasto = litros_cunsumidos * preco_combustivel

consumo_medio_km = distancia_percorrida / litros_cunsumidos

print("Você percorreu", distancia_percorrida, "quilometros.")

print("O valor total gasto foi", valor_total_gasto, "reais.")

print("O consumo médio do carro foi", consumo_medio_km, "km/l.")