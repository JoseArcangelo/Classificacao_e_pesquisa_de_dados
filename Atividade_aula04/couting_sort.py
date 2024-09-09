def couting_sort(lst):
  maior_elemento = 0

  for i in lst:
    if i > maior_elemento:
      maior_elemento = i

  l_counter = []
  for i in range(maior_elemento):
    l_counter.append(0)
  
  l = []
  for i in lst:
    l.append(0)
    l_counter[i-1] += 1

  for i in range(1, len(l_counter)):
    l_counter[i] = l_counter[i] + l_counter[i - 1]

  for i in range(len(lst) - 1, -1, -1):
    l[l_counter[lst[i] - 1] - 1] = lst[i]
    l_counter[lst[i] - 1] -= 1
  print(l)

lst = [3, 2, 4, 7, 4, 7, 1, 2, 3]
couting_sort(lst)

