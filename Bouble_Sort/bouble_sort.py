def bouble_sort(l):
    for a in range(len(l)):
        ordenado = 0
        for b in range(a + 1, len(l)):
            if l[a] > l[b]:
                l[a], l[b] = l[b], l[a]
                ordenado = 1

        if ordenado == 0:
            return l
    
def main():
    l = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(l)
    l = bouble_sort(l)
    print(l)

main()
