class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class TabelaHash:
    def __init__(self, m):
        self.m = m
        self.tabela = [None] * m

def funcao_hash(tabela, chave):
    h = 0
    for i in chave:
        h += ord(i)
    return h % tabela.m

def inserir(tabela, chave):
    indice = funcao_hash(tabela, chave)
    novo = No(chave)
    if not tabela.tabela[indice]:
        tabela.tabela[indice] = novo
    else:
        atual = tabela.tabela[indice]
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo

def buscar(tabela, chave):
    indice = funcao_hash(tabela, chave)
    atual = tabela.tabela[indice]
    while atual:
        if atual.valor == chave:
            return atual.valor
        atual = atual.proximo
    return False

def remover(tabela, chave):
    indice = funcao_hash(tabela, chave)
    atual = tabela.tabela[indice]
    anterior = None

    while atual:
        if atual.valor == chave:
            if anterior is None:
                tabela.tabela[indice] = atual.proximo
            else:
                anterior.proximo = atual.proximo
            print(f"'{chave}' removido com sucesso.")
            return
        anterior = atual
        atual = atual.proximo

    print(f"'{chave}' não encontrado na tabela.")

def exibir(tabela):
    for i, no in enumerate(tabela.tabela):
        print(f"Índice {i}: ", end="")
        atual = no
        while atual:
            print(f"{atual.valor} -> ", end="")
            atual = atual.proximo
        print("None")

tabela = TabelaHash(10)
inserir(tabela, "relatorio.pdf")
inserir(tabela, "documento.txt")
inserir(tabela, "imagem.png")

print("Tabela antes da remoção:")
exibir(tabela)

remover(tabela, "documenadsto.txt")

print("\nTabela após a remoção:")
exibir(tabela)
