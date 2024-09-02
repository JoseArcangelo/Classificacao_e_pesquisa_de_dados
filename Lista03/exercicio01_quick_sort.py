def particiona(lst, inicio, fim):
    pivo = inicio
    esq = inicio + 1
    dir = fim
    
    while esq <= dir:
        while esq <= fim and lst[esq] <= lst[pivo]:
            esq += 1
        while lst[dir] > lst[pivo]:
            dir -= 1
        if esq < dir:
            lst[esq], lst[dir] = lst[dir], lst[esq]
    
    lst[dir], lst[pivo] = lst[pivo], lst[dir]
    return dir

def quick_sort(lst, inicio, fim):
    if inicio < fim:
        pivo_index = particiona(lst, inicio, fim)
        quick_sort(lst, inicio, pivo_index - 1)
        quick_sort(lst, pivo_index + 1, fim)

def main():
    l = [40, 20, 10, 30, 60, 50, 7, 80, 100]
    quick_sort(l, 0, len(l) - 1)
    print(l)

main()
