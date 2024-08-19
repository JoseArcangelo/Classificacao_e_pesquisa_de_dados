def selection_sort(l):
  for a in range(len(l)):
    posicao_menor = a
    for b in range(a + 1, len(l)):
      if l[b] < l[posicao_menor]:
        posicao_menor = b

    if posicao_menor != a:
      l[a], l[posicao_menor] = l[posicao_menor], l[a]
    
  return l
    
def main():
  l = [4, 1, 5, 7, 2, 3]  #desordenados aleatorios
  # l = [1, 2, 3, 4, 5, 6]  #ordenados
  # l = [6, 5, 4, 3, 2, 1]  #ordenados na ordem inversa
  # l = [4, 1, 1, 5, 2, 5]  #elementos duplicados
  l = selection_sort(l)
  print(l)

main()
