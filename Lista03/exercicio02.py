import time
import random

def bouble_sort(l):
    inicio = time.time()

    for a in range(len(l)):
        ordenado = 0
        for b in range(a + 1, len(l)):
            if l[a] > l[b]:
                l[a], l[b] = l[b], l[a]
                ordenado = 1

        if ordenado == 0:
            fim = time.time()

            print(f"TEMPO DE EXECUÇÃO: {fim - inicio:.10f} segundos")

            return l

def insert_sort(l):
    inicio = time.time()

    for i in range(1, len(l)):
        
        valor = l[i]
        a = i-1

        while a >= 0 and valor < l[a]:
            l[a + 1], l[a] = l[a], l[a + 1]
            a-=1 

    fim = time.time()
    print(f"TEMPO DE EXECUÇÃO: {fim - inicio:.10f} segundos")

    return l 

def selection_sort(l):
    inicio = time.time()

    for a in range(len(l)):
        posicao_menor = a
        for b in range(a + 1, len(l)):
            if l[b] < l[posicao_menor]:
                posicao_menor = b

    if posicao_menor != a:
        l[a], l[posicao_menor] = l[posicao_menor], l[a]

    fim = time.time()
    print(f"TEMPO DE EXECUÇÃO: {fim - inicio:.10f} segundos")

    return l

def merge_sort(l):
    if len(l) <= 1:
        return l
    meio = len(l) // 2
    esq = l[:meio]
    dir = l[meio:]

    esq = merge_sort(esq)
    dir = merge_sort(dir)
    return juntar(esq, dir)

def juntar(esq, dir):
    l = [ ]
    i= 0
    j= 0
    while i < len(esq) and j < len(dir):
        if esq[i] < dir[j]:
            l.append(esq[i])
            i += 1
        else:
            l.append(dir[j])
            j+= 1

    while i  < len(esq):
        l.append(esq[i])
        i += 1
    while j < len(dir):
        l.append(dir[j])
        j += 1

    return l

def shell_sort(lst, pulos):
    inicio = time.time()

    while pulos > 0:
        for i in range(pulos, len(lst)):
            valor_atual = lst[i]
            j = i
            
            while j >= pulos and lst[j - pulos] > valor_atual:
                lst[j] = lst[j - pulos]
                j -= pulos
            
            lst[j] = valor_atual
        
        pulos //= 2
    
    fim = time.time()
    print(f"TEMPO DE EXECUÇÃO: {fim - inicio:.10f} segundos")
    return lst

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
    l = [random.randint(1, 1000) for _ in range(2000)] ##Aleatorios
    # l = [i //2 for i in range(2000)] ##Duplicados
    # l = [i for i in range(1, 101)] ##Ordenados
    # l = [i for i in range(5000, 0, -1)] ##Inverso

    while(True):
        print("\n 1-Buble Sort" +
        "\n 2-Insert Sort" +
        "\n 3-Selection Sort" + 
        "\n 4-Merge Sort" + 
        "\n 5-Shell Sort" + 
        "\n 6-Quick Sort")
            
        opc = input("Escolha uma opção: ")
        if opc == "1":
            bouble_sort(l)

        elif opc == "2":
            insert_sort(l)

        elif opc == "3":
            selection_sort(l)

        elif opc == "4":
            inicio = time.time()
            merge_sort(l)
            fim = time.time()
            print(f"TEMPO DE EXECUÇÃO: {fim - inicio:.10f} segundos")

        elif opc == "5":
            l = shell_sort(l, len(l) // 2)

        elif opc == "6":
            inicio = time.time()
            quick_sort(l, 0, len(l) - 1)
            fim = time.time()
            print(f"TEMPO DE EXECUÇÃO: {fim - inicio:.10f} segundos")


        else:
            break
        
main()
