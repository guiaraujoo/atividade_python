preco_abril = int(input("Qual o preço da mercadoria em abril? "))
preco_maio = int(input("Qual o preço da mercadoria em maio? "))

taxa_inflacao = (preco_maio - preco_abril) / preco_abril * 100
print("A taxa de inflação é de {:.2f}%.".format(taxa_inflacao))