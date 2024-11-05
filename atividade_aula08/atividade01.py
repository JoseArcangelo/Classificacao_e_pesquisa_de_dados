def busca_binaria_interpolacao(lista, elemento):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:  
        meio = int(inicio + ((fim - inicio) * (elemento - lista[inicio])) / (lista[fim] - lista[inicio]))

        if meio < inicio or meio > fim:  
            return -1

        if lista[meio] == elemento:
            return meio  
        
        return -1

def busca_binaria_iterativa(lista, elemento):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2  

        if lista[meio] == elemento:
            return meio  
        elif lista[meio] < elemento:
            inicio = meio + 1  
        else:
            fim = meio - 1 
    return -1 

def busca_binaria_recursiva(lista, elemento, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1

    if inicio > fim:
        return -1  

    meio = (inicio + fim) // 2  

    if lista[meio] == elemento:
        return meio  
    elif lista[meio] < elemento:
        return busca_binaria_recursiva(lista, elemento, meio + 1, fim)
    else:
        return busca_binaria_recursiva(lista, elemento, inicio, meio - 1)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
print(busca_binaria_iterativa(l, 5))
print(busca_binaria_recursiva(l, 8))
print(busca_binaria_interpolacao(l, 7))
