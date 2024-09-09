def heap_sort_max(a):
    for k in range(len(a) // 2 - 1, -1, -1):
        max_heapify(a, k, len(a))

    for n in range(len(a) - 1, 0, -1):
        # a[0], a[n] = a[n], a[0]
        max_heapify(a, 0, n)


def max_heapify(a, i, n):
    maior = i
    l = 2 * i + 1  
    r = 2 * i + 2 

    if l < n and a[l] > a[maior]:
        maior = l

    if r < n and a[r] > a[maior]:
        maior = r

    if maior != i:
        a[i], a[maior] = a[maior], a[i]
        max_heapify(a, maior, n)

def remove(a): 
    a[0], a[-1] = a[-1], a[0]
    a.pop()

    heap_sort_max(a)
    return a

def insert(a, valor):
    a.append(valor)
    heap_sort_max(a)
    return a

a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
heap_sort_max(a)
print("Array ordenado (Max Heap):", a)
print("\nRemovendo o valor: ", a[0])
a = remove(a)
print(a)

print("\nAdicionando um novo valor: ", 20)
a = insert(a, 20)
print(a)
