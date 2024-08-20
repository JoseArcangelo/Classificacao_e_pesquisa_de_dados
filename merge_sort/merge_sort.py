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
  while j < len[dir]:
    l.append(dir[j])
    j += 1

  print(l)
  return l


def main():
  l = [ 38, 27, 43, 3, 82, 0]
  l = merge_sort(l)

main()
