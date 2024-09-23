#Tentei fazer sozinho mas não funcionou, então pedi ajuda pro chatgpt. Também fiz uma pesquisa para entender melhor a lógica de ordenação externa.

import os
import heapq

def dividir_e_ordenar(arquivo_entrada, tamanho_chunk):
    """Divide um grande arquivo de entrada em partes menores (chunks) e as ordena."""
    chunks = []
    with open(arquivo_entrada, 'r') as arquivo:
        chunk_atual = []
        for linha in arquivo:
            chunk_atual.append(linha.strip())

            if len(chunk_atual) == tamanho_chunk:
                chunk_atual.sort()
                arquivo_chunk = f'chunk_{len(chunks)}.txt'
                with open(arquivo_chunk, 'w') as arquivo_temp:
                    arquivo_temp.write('\n'.join(chunk_atual))
                chunks.append(arquivo_chunk)
                chunk_atual = []

        if chunk_atual:
            chunk_atual.sort()
            arquivo_chunk = f'chunk_{len(chunks)}.txt'
            with open(arquivo_chunk, 'w') as arquivo_temp:
                arquivo_temp.write('\n'.join(chunk_atual))
            chunks.append(arquivo_chunk)

    return chunks

def mesclar_chunks_ordenados(chunks, arquivo_saida):
    """Mescla chunks ordenados em um único arquivo de saída."""
    arquivos = [open(chunk, 'r') for chunk in chunks]
    with open(arquivo_saida, 'w') as arquivo_out:
        heap = []
        for i, arquivo in enumerate(arquivos):
            linha = arquivo.readline().strip()
            if linha:
                heapq.heappush(heap, (linha, i))
        
        while heap:
            menor, indice = heapq.heappop(heap)
            arquivo_out.write(menor + '\n')

            proxima_linha = arquivos[indice].readline().strip()
            if proxima_linha:
                heapq.heappush(heap, (proxima_linha, indice))

    for arquivo in arquivos:
        arquivo.close()

    for chunk in chunks:
        os.remove(chunk)

def merge_sort_externo(arquivo_entrada, arquivo_saida, tamanho_chunk=100):
    """Executa o merge sort externo para ordenar um grande arquivo de entrada."""
    chunks = dividir_e_ordenar(arquivo_entrada, tamanho_chunk)
    mesclar_chunks_ordenados(chunks, arquivo_saida)


arquivo_entrada = 'entrada.txt'  
arquivo_saida = 'saida_ordenada.txt'
tamanho_chunk = 100 

merge_sort_externo(arquivo_entrada, arquivo_saida, tamanho_chunk)
