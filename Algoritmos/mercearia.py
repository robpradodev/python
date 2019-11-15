#-*-coding:utf8;-*-
#qpy:3
#qpy:console

compras = []
preco = []
produto = []
qt = []

opcao = True

while opcao == True:
    for i in range(0, 100):
        qt.append(int(input("Digite a quantidade")))
        produto.append(input("Digite o nome do produto"))
        preco.append(float(input("Digite o preço unitário")))
        linha = " ", qt[i], " - ", produto[i], " ", preco[i]
        compras.append(linha)

        adicionar = input("Adicionar mais produto(s) ao carrinho? s/n")
    
        if adicionar == 'n':
            opcao = False
        else:
            if adicionar == 's':
                opcao = True

print ("Quantidade - Produto - Preço")
for produto in compras:
    print (compras[produto])
