class Node:
	def __init__(self, val, esq=None, dir=None):
		self.val = val
		self.esq = esq
		self.dir = dir

	def __str__(self):
		return str(self.val)

def print_node(node):
	print(node, end=" ")

def arvore_vazia(arv):
	return not arv

def pre_ordem(arv):
	if not arvore_vazia(arv):
		print_node(arv)
		pre_ordem(arv.esq)
		pre_ordem(arv.dir)

def simetrica(arv):
	if not arvore_vazia(arv):
		simetrica(arv.esq)
		print_node(arv)
		simetrica(arv.dir)

def pos_ordem(arv):
	if not arvore_vazia(arv):
		pos_ordem(arv.esq)
		pos_ordem(arv.dir)
		print_node(arv)

def insere(arv, key):
	if arvore_vazia(arv):
		return Node(key)
	if key < arv.val:
		arv.esq = insere(arv.esq, key)
	else:
		arv.dir = insere(arv.dir, key)
	return arv

def busca(arv, valor):
	if arvore_vazia(arv) or arv.val == valor:
			return arv
	
	if valor < arv.val:
			return busca(arv.esq, valor)
	
	return busca(arv.dir, valor)


def remove(arv, valor):
    if arvore_vazia(arv):
        return arv
    
    # Procurando o valor a ser removido
    if valor < arv.val:
        arv.esq = remove(arv.esq, valor)
    elif valor > arv.val:
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
        arv.val = min_node.val
        arv.dir = remove(arv.dir, min_node.val)
    
    return arv

arvore = None
valores = [1, 3, 4, 6, 0, 10, 11, 9, 5, 7]
for valor in valores:
    arvore = insere(arvore, valor)

print("\nSimétrico:")
simetrica(arvore)  
print("\nPré-ordem:")
pre_ordem(arvore)
print("\nPós-ordem:")
pos_ordem(arvore)
arvore = remove(arvore, 10)
print("\nSimétrico pós remoção:")
simetrica(arvore)  

valor_buscar = 5
print("\nBusca por:",  valor_buscar)
a = busca(arvore, valor_buscar)
if a != None:
	print(valor_buscar, "foi encontrado!")
else:
	print(valor_buscar, "nao foi encontrado!")
