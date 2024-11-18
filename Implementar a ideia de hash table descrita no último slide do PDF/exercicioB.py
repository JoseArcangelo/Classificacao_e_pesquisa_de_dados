class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class TabelaHash:
    def __init__(self, m):
        self.m = m
        self.tabela = [None] * m

    def funcao_hash(self, chave):
        return chave % self.m

    def inserir(self, chave):
        indice = self.funcao_hash(chave)
        novo = No(chave)
        if not self.tabela[indice]:
            self.tabela[indice] = novo
        else:
            atual = self.tabela[indice]
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo

    def buscar(self, chave):
        indice = self.funcao_hash(chave)
        atual = self.tabela[indice]
        while atual:
            if atual.valor == chave:
                return True
            atual = atual.proximo
        return False

    def exibir(self):
        for i, no in enumerate(self.tabela):
            print(f"Índice {i}: ", end="")
            atual = no
            while atual:
                print(f"{atual.valor} -> ", end="")
                atual = atual.proximo
            print("None")

tabela = TabelaHash(7)
tabela.inserir(15)
tabela.inserir(25)
tabela.inserir(10)
tabela.exibir()
