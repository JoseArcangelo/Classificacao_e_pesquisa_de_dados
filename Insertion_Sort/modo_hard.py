class Lista:
    def __init__(self, info=None, ante=None):
        self.info = info
        self.prox = None
        self.ante = ante

def insere_lista(lista, valor):
    novo = Lista(valor)
    novo.prox = lista
    if lista is not None:
        lista.ante = novo
    return novo

def lista_imprime(lista):
    atual = lista
    while atual is not None:
        print(atual.info)
        atual = atual.prox

def insertion_sort(lst):
    if lst is None or lst.prox is None:
        return lst  
    
    atual = lst.prox  
    while atual is not None:

        atual2 = atual.ante  
        while atual2 is not None and atual2.info > atual.info:
            
            atual2.info, atual.info = atual.info, atual2.info
            atual = atual2  
            atual2 = atual2.ante  
            
        atual = atual.prox  
    
    return lst  
    
lista = None
lista = insere_lista(lista, 4)
lista = insere_lista(lista, 3)
lista = insere_lista(lista, 2)
lista = insere_lista(lista, 0)
lista = insere_lista(lista, 90)
lista = insere_lista(lista, 100)

lista_imprime(lista)

lista = insertion_sort(lista)

print("\n::Ordenada::")
lista_imprime(lista)
lista = insertion_sort(lista)

print("\n::Ordenada::")
lista_imprime(lista)
