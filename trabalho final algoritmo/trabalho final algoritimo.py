class tproduto:
    codigo = 0
    nome = ''
    preco = 0.00
    estoque = 0
    precoTotal = 0.00
    qtdCompra = 0

def mensagemBonita(sessao):
    print("\n", sessao, "\n", "-" * 40)
    
def mensagem(msg):
    print("\n", "-" * len(msg), "\n", msg, "\n", "-" * len(msg), "\n")

def consultarProduto(pr, p): #pr=produto p=consultarProduto
  for i in range (len(pr)):
    if pr[i].codigo == p:
      return i
  return -1

def cadProduto():  # FUNÇÃO PARA CADASTRAR NOVOS PRODUTOS
    produto = tproduto()
    cod = int(input("Código: "))
    while consultarProduto(produtos, cod) != -1:
        print("Código ja está sendo utilizado")
        cod = int(input("insira um novo código: "))
    produto.codigo = cod
    produto.nome = input("Nome: ")
    produto.preco = float(input('Preço: '))
    produto.estoque = int(input('Estoque: '))
    return produto

def mostrarOsProduto(p):
    print('%5d %-16s %.2f %5d' % (p.codigo, p.nome, p.preco, p.estoque))

def atualizarOsPreco(n, codigo, pre, ):  # UPP=ATUALIZAR PREÇO
    pos = consultarProduto(n, codigo, )
    if pos != -1:
        n[pos].preco = pre

def updateEstoque(p, codigo, est, ):  # PARA ATUALIZAR O ESTOQUE
    pos = consultarProduto(p, codigo)
    if pos != -1:
        p[pos].estoque = est

def listProduto(lprodutos):  # LISTAR OS PRODUTOS
    mensagem("COD. PRODUTO\t\tPREÇO\tESTOQUE")
    for i in range(len(lprodutos)):
        mostrarOsProduto(lprodutos[i])

def carrinhoDeCompras(compra):
  print("\nCupom fiscal\n")
  print("| Código | Nome             | Quantidade | Preço | Preço Total |")
  print("|-----------------------------------------------------------------------|")
  for i in range(len(compra)):
    print("| {:>6} | {:<16} | {:>10} | {:>13.2f}  | {:>11.2f} |".format(compra[i].codigo, compra[i].nome, compra[i].qtdCompra, compra[i].preco, compra[i].precoTotal))
    print("|-----------------------------------------------------------------------|")
#Registrar compra
def valorTotal(compra):
  valorTotal = 0.00
  for i in range (len(compra)):
    valorTotal += compra[i].precoTotal
  print("|  {:>56}".format("Total |"), "{:>11.2f} |".format(valorTotal))

def registrarCompra(produto, codigoProcurado):
  #Valida se existe o produto
  posicao = consultarProduto(produto, codigoProcurado)
  if posicao != -1:
    print("Nome do produto: " , produto[posicao].nome)
    qtdAComprar = int(input("Digite a quantidade de produtos para comprar: "))
    if qtdAComprar > produto[posicao].estoque:
      print("Estoque insuficiente! A quantidade disponível para compra é: ", produto[posicao].qtdEstoque)
      return -1
    else:
      #Compra do produto
      CFe = tproduto()
      CFe.codigo = produto[posicao].codigo
      CFe.nome = produto[posicao].nome
      CFe.qtdCompra = qtdAComprar
      CFe.preco = produto[posicao].preco
      CFe.precoTotal = (qtdAComprar * produto[posicao].preco)
      #Atualiza o valor do estoque
      produto[posicao].estoque -= qtdAComprar
      return CFe
  else:
    print("Produto não encontrado.")
    return -1


def menu():  # MENU PARA OPERADOR DE ESTOQUE CADASTRAR NOVOS PRODUTOS E PREÇOS
    mensagemBonita("OPÇÕES")
    print('\t1- CADASTRAR')
    print('\t2- LISTA DE PRODUTOS JA CADASTRADOS')
    print('\t3- BUSCAR POR PRODUTOS CADASTRADOS')
    print('\t4- ATUALIZAR PREÇO E ITENS DO ESTOQUE')
    print('\t5- REGISTAR COMPRAS')
    print('\t0- SAIR')
    opção = int(input("\t"))
    return opção

# programa principal
comprasA=[]
produtos=[]
while True:
    opção = menu()
    if opção == 0:
        break
    if opção == 1:
        pr = cadProduto()
        produtos.append(pr)
    if opção == 2:
        listProduto(produtos)
    if opção == 3:
        p = int(input('Código: '))
        pos = consultarProduto(produtos, p)
        if pos == -1:
            print("Código não encontrado!")
        else:
            mostrarOsProduto(produtos[pos])
    if opção == 4:
        codigo = int(input('Código: '))
        preco = float(input('Novo Preço: '))
        estoque = int(input("Novo estoque: "))
        atualizarOsPreco(produtos, codigo, preco, )
        updateEstoque(produtos, codigo, estoque)
    if opção == 5:
        print("\nRealizando a compra")
        while True:
            codigoProcurado = int(input("Digite o código do produto: "))
            codigoProdutoComprado = registrarCompra(produtos, codigoProcurado) 
            if codigoProdutoComprado != -1:
                produtos.append(codigoProdutoComprado)
                carrinhoDeCompras(produtos)
                valorTotal(produtos)
                continuarCompra = input("\nDeseja continuar comprando? Digite S - Sim / N - Não: ").lower()
                if continuarCompra == 'n':
                    break