def busca_iterativa(lst, valor):
  for i in lst:
    if (i == valor):
      return valor
  return False

def busca_recursiva(lst, valor):
    if not lst:
        return False
    if lst[0] == valor:
        return valor
    return busca_recursiva(lst[1:], valor)


def main():
  lst = [1, 2, 3, 4, 5, 6, 7, 8]
  print(busca_iterativa(lst, 5))
  print(busca_recursiva(lst, 2))

main()
