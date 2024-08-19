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

def insertion_sort(lista):
    if lista is None or lista.prox is None:
        return lista  
    
    lista_ordenada = None  

    while lista is not None:
        atual = lista  
        lista = lista.prox  
        
        if lista_ordenada is None or atual.info < lista_ordenada.info:
          
            atual.prox = lista_ordenada
            lista_ordenada = atual
        else:
            
            busca = lista_ordenada
            while busca.prox is not None and busca.prox.info < atual.info:
                busca = busca.prox
            
            atual.prox = busca.prox
            busca.prox = atual
    
    return lista_ordenada  
    
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
