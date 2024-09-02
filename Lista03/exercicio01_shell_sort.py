def shell_sort(lst, pulos):
    while pulos > 0:
        for i in range(pulos, len(lst)):
            valor_atual = lst[i]
            j = i
            
            while j >= pulos and lst[j - pulos] > valor_atual:
                lst[j] = lst[j - pulos]
                j -= pulos
            
            lst[j] = valor_atual
        
        pulos //= 2
    
    return lst

def main():
    l = [40, 20, 10, 30, 60, 50, 7, 80]
    l = shell_sort(l, len(l) // 2)
    print(l)

main()
