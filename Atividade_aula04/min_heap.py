def heap_sort_min(a):
    for k in range(len(a) // 2 - 1, -1, -1):
        min_heapify(a, k, len(a))

    for n in range(len(a) - 1, 0, -1):
        # a[0], a[n] = a[n], a[0]  # Troca a raiz com o último elemento
        min_heapify(a, 0, n)

def min_heapify(a, i, n):
    menor = i
    l = 2 * i + 1  
    r = 2 * i + 2  

    if l < n and a[l] < a[menor]:
        menor = l

    if r < n and a[r] < a[menor]:
        menor = r

    if menor != i:
        a[i], a[menor] = a[menor], a[i]
        min_heapify(a, menor, n)

def remove(a): 
    a[0], a[-1] = a[-1], a[0]
    a.pop()

    heap_sort_min(a)
    return a

def insert(a, valor):
    a.append(valor)
    heap_sort_min(a)
    return a

a = [12, 11, 13, 5, 6, 7]
heap_sort_min(a)
print("Array ordenado (Min Heap):", a)

print("\nRemovendo o valor: ", a[0])
a = remove(a)
print(a)

print("\nAdicionando um novo valor: ", 1)
a = insert(a, 1)
print(a)

