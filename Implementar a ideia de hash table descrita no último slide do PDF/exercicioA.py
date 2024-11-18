class TabelaHash:
    def __init__(self, m):
        self.m = m
        self.tabela = {i: [] for i in range(m)} 

    def funcao_hash(self, chave):
        return chave % self.m

    def inserir(self, chave):
        indice = self.funcao_hash(chave)
        self.tabela[indice].append(chave)

    def buscar(self, chave):
        indice = self.funcao_hash(chave)
        return chave in self.tabela[indice]

    def exibir(self):
        for chave, valores in self.tabela.items():
            print(f"Índice {chave}: {valores}")

tabela = TabelaHash(7)
tabela.inserir(15)
tabela.inserir(25)
tabela.inserir(10)
tabela.exibir()
