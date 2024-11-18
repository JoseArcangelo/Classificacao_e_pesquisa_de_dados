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
    # chave = str(chave)
    for i in chave:
        h+= ord(i) 
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

# exibir(tabela)
resultado = buscar(tabela, "relatorio.pdf")
print(resultado)
