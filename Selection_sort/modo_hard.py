class Lista:
    def __init__(self, info=None):
      self.info = info
      self.prox = None

def insere_lista(lista, valor):
    novo = Lista(valor)
    novo.prox = lista
    return novo

def lista_imprime(lista):
    atual = lista
    while atual is not None:
        print(atual.info)
        atual = atual.prox


def selection_sort(lst):
    atual = lst
    while atual is not None:
        
      atual2 = atual.prox
      menor_valor = atual
      while atual2 is not None:
        if atual2.info < menor_valor.info:
            menor_valor = atual2
        atual2 = atual2.prox
    
      if menor_valor != atual:
        atual.info, menor_valor.info = menor_valor.info, atual.info

      atual = atual.prox
    return lst

lst = None
lst = insere_lista(lst, 4)
lst = insere_lista(lst, 3)
lst = insere_lista(lst, 2)
lst = insere_lista(lst, 2)
lst = insere_lista(lst, 90)
lst = insere_lista(lst, 100)

lista_imprime(lst)
lst = selection_sort(lst)
print("\nordenado:")
lista_imprime(lst)
