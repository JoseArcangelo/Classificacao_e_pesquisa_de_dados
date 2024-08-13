def insert_sort(l):
    for i in range(1, len(l)):
        
        valor = l[i]
        a = i-1

        while a >= 0 and valor < l[a]:
            l[a + 1] = l[a]
            a-=1
            print(l)
            
        l[a + 1] = valor
    return l
        

l = [4, 3, 2, 0]
# l = [1, 2, 3, 4, 5]
# l = [1, 1,1 ,2 , 3, 3, 3, 4, 4]

print(l)
l = insert_sort(l)
print(l)
