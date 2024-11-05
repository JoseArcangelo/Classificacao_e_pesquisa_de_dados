import math
import time

def busca_por_salto(lista, elemento):
    tamanho = len(lista)
    salto = int(math.sqrt(tamanho))
    anterior = 0

    while lista[min(salto, tamanho) - 1] < elemento:
        anterior = salto
        salto += int(math.sqrt(tamanho))
        if anterior >= tamanho:
            return False

    for i in range(anterior, min(salto, tamanho)):
        if lista[i] == elemento:
            return True  

    return False 

# OBS: Tive um pouco de dificuldade com esse algoritimo, entao pesquise sua implementacao e busquei entender, mas após a aula entendi melhor.
def busca_fibonacci(lista, elemento):
    tamanho = len(lista)
    
    fib_menos_dois = 0
    fib_menos_um = 1
    fib_m = fib_menos_dois + fib_menos_um

    while fib_m < tamanho:
        fib_menos_dois = fib_menos_um
        fib_menos_um = fib_m
        fib_m = fib_menos_dois + fib_menos_um

    deslocamento = -1

    while fib_m > 1:
        i = min(deslocamento + fib_menos_dois, tamanho - 1)

        if lista[i] < elemento:
            fib_m = fib_menos_um
            fib_menos_um = fib_menos_dois
            fib_menos_dois = fib_m - fib_menos_um
            deslocamento = i
        elif lista[i] > elemento:
            fib_m = fib_menos_dois
            fib_menos_um -= fib_menos_dois
            fib_menos_dois = fib_m - fib_menos_um
        else:
            return True  

    if fib_menos_um and lista[deslocamento + 1] == elemento:
        return True  

    return False  

lista_ordenada = list(range(1, 10001))

inicio_tempo_salto = time.time()
resultado_salto = busca_por_salto(lista_ordenada, 9999) 
fim_tempo_salto = time.time()
tempo_salto = fim_tempo_salto - inicio_tempo_salto

inicio_tempo_fibonacci = time.time()
resultado_fibonacci = busca_fibonacci(lista_ordenada, 9999) 
fim_tempo_fibonacci = time.time()
tempo_fibonacci = fim_tempo_fibonacci - inicio_tempo_fibonacci

print(f"Resultado da busca por salto: {resultado_salto}, Tempo: {tempo_salto:.100f} segundos")
print(f"Resultado da busca Fibonacci: {resultado_fibonacci}, Tempo: {tempo_fibonacci:.100f} segundos")

# 3- 
# a)  Fibonacci pode ter ligeiramente menos comparações do que a busca por salto pois usa a sequência de Fibonacci para determinar os índices, o que é mais eficiente em alguns casos.

# b) Busca por salto: listas grandes e ordenadas quando a busca binária não é aplicável.
# Busca Fibonacci: listas ordenadas quando é vantajoso minimizar o número de comparações.

# c) Ambos os métodos requerem que a lista esteja ordenada para funcionar corretamente. Em listas não ordenadas, nem a busca por salto nem a busca Fibonacci seriam eficazes.
