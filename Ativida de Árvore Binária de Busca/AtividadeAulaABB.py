class Node:
    def __init__(self, product, esq=None, dir=None):
        self.product = product 
        self.esq = esq
        self.dir = dir

    def __str__(self):
        return str(self.product['id'])  

def print_node(node):
    print(node, end=" ")

def arvore_vazia(arv):
    return not arv

def insere(arv, product):
    if arvore_vazia(arv):
        return Node(product)
    if product['id'] < arv.product['id']:
        arv.esq = insere(arv.esq, product)
    else:
        arv.dir = insere(arv.dir, product)
    return arv

def busca(arv, valor):
    if arvore_vazia(arv) or arv.product['id'] == valor:
        return arv
    
    if valor < arv.product['id']:
        return busca(arv.esq, valor)
    
    return busca(arv.dir, valor)

def remove(arv, valor):
    if arvore_vazia(arv):
        return arv
    
    # Procurando o valor a ser removido
    if valor < arv.product['id']:
        arv.esq = remove(arv.esq, valor)
    elif valor > arv.product['id']:
        arv.dir = remove(arv.dir, valor)
    else:
        # Caso 1: Nó folha (sem filhos)
        if arv.esq is None and arv.dir is None:
            return None
        
        # Caso 2: Nó com apenas um filho
        if arv.esq is None:
            return arv.dir
        elif arv.dir is None:
            return arv.esq
        
        # Caso 3: Nó com dois filhos
        min_node = arv.dir
        while min_node.esq:
            min_node = min_node.esq
        arv.product = min_node.product
        arv.dir = remove(arv.dir, min_node.product['id'])
    
    return arv

arvore = None
produtos = [
    {'id': 1, 'nome': 'Produto A', 'descricao': 'Descrição do Produto A', 'preco': 10.0},
    {'id': 3, 'nome': 'Produto B', 'descricao': 'Descrição do Produto B', 'preco': 20.0},
    {'id': 4, 'nome': 'Produto C', 'descricao': 'Descrição do Produto C', 'preco': 30.0},
    {'id': 6, 'nome': 'Produto D', 'descricao': 'Descrição do Produto D', 'preco': 40.0},
    {'id': 0, 'nome': 'Produto E', 'descricao': 'Descrição do Produto E', 'preco': 5.0},
    {'id': 10, 'nome': 'Produto F', 'descricao': 'Descrição do Produto F', 'preco': 100.0},
    {'id': 11, 'nome': 'Produto G', 'descricao': 'Descrição do Produto G', 'preco': 110.0},
    {'id': 9, 'nome': 'Produto H', 'descricao': 'Descrição do Produto H', 'preco': 90.0},
    {'id': 5, 'nome': 'Produto I', 'descricao': 'Descrição do Produto I', 'preco': 50.0},
    {'id': 7, 'nome': 'Produto J', 'descricao': 'Descrição do Produto J', 'preco': 70.0},
]

for produto in produtos:
  arvore = insere(arvore, produto)

while(True):
    id = 100 
    print("1- Adicionar produto", "\n2- Remover produto", "\n3- Buscar produto", "\n4- Sair")
    opc = int(input("Informe uma opcao: "))
    if opc == 1:
        nome = str(input("Informe o nome do produto: "))
        descricao = str(input("Informe uma descricao: "))
        preco = float(input("Informe o preco do produto: "))
        produto = {'id': id, 'nome': nome, 'descricao': descricao, 'preco': preco}
        arvore = insere(arvore, produto)
        id+= 1

    elif opc == 2:
      id_produto = int(input("Informe o id do produto a ser removido: "))    
      arvore = remove(arvore, id_produto)

    elif opc == 3:
        id_busca = int(input("Informe o id do produto a ser buscado: "))
        produto_encontrado = busca(arvore, id_busca)
        if produto_encontrado:
            print(f"\nProduto encontrado: {produto_encontrado.product}")
        else:
            print(f"\nProduto com ID {id_busca} não foi encontrado!")

    elif opc == 4:
        print("Saindo...")
        break
    else:
      print("Valor invalido!")
