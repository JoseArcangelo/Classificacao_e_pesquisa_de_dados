class MotorBuscaJogos:
  def __init__ (self):
    self.catalogo_jogos = ArvoreJogos()
    self.generos = HashGeneros()

class Jogo:
  def __init__ (self, jogo_id, titulo, desenvolvedor, preco, genero):
    self.jogo_id = jogo_id
    self.titulo = titulo
    self.desenvolvedor = desenvolvedor
    self.preco = preco
    self.genero = genero

class NoJogo:
  def __init__ (self, jogo):
    self.jogo = jogo
    self.esq = None
    self.dir = None

class ArvoreJogos:
  def __init__ (self):
    self.raiz = None
  
  def inserir(self, jogo):
    no_atual = self.raiz
    if no_atual is None:  
      self.raiz = NoJogo(jogo)
      return

    while True:
      if jogo.preco < no_atual.jogo.preco:  
        if no_atual.esq is None:
          no_atual.esq = NoJogo(jogo)
          break
        else:
          no_atual = no_atual.esq
      else:  
          if no_atual.dir is None:
            no_atual.dir = NoJogo(jogo)
            break
          else:
            no_atual = no_atual.dir
  
  def buscar_por_preco(self, preco):
    no_atual = self.raiz
    jogos_encontrados = [] 
    
    while no_atual is not None:
        if no_atual.jogo.preco == preco:
            jogos_encontrados.append(no_atual.jogo.titulo)  
        
        if preco < no_atual.jogo.preco:
            no_atual = no_atual.esq
        else:
            no_atual = no_atual.dir

    if jogos_encontrados:
        for titulo in jogos_encontrados:
            print(titulo)
    else:
        print("::NENHUM JOGO FOI ENCONTRADO COM O PRECO INFORMADO!::")
    

  def busca_por_faixa_preco(self, preco_minimo, preco_maximo):
    no_atual = self.raiz
    ids_percorridos = []

    def percorrer_arvore(no):
      if no is None:
          return
      
      if preco_minimo <= no.jogo.preco <= preco_maximo and no.jogo.jogo_id not in ids_percorridos:
          print(no.jogo.titulo) 
          ids_percorridos.append(no.jogo.jogo_id)
      
      if preco_minimo < no.jogo.preco:
          percorrer_arvore(no.esq)  
      if preco_maximo > no.jogo.preco:
          percorrer_arvore(no.dir)  

    percorrer_arvore(no_atual)
    
class HashGeneros:
  def __init__ (self):
    self.m = 23
    self.genero_para_jogos = {i: [] for i in range(self.m)}

  def funcao_hash(self, genero):
    h = 0
    for i in genero:
        h += ord(i)  
    return h % self.m
  
  def inserir_por_genero(self, jogo):
      indice = self.funcao_hash(jogo.genero)

      self.genero_para_jogos[indice].append(jogo)

  def obter_jogos(self, genero):
      indice = self.funcao_hash(genero)
      for i in range(len(self.genero_para_jogos[indice])):
        if self.genero_para_jogos[indice][i].genero == genero:
          print(self.genero_para_jogos[indice][i].titulo)

def em_ordem(no):
  if no is not None:
    em_ordem(no.esq)  
    print(no.jogo.titulo, ", PRECO:", no.jogo.preco, ", ID:", no.jogo.jogo_id, "\n")  
    em_ordem(no.dir) 

def imprimir_tabela_hash(tabela):
    for indice, jogos in tabela.items():
        print(f"Índice {indice}:")
        if jogos:
            for jogo in jogos:
                print(f"  - {jogo.titulo} ({jogo.genero})")
        else:
            print("  Nenhum jogo")
        print()

def main():
  catalogo = MotorBuscaJogos()
  list_jogos = [
    [1, "The Legend of Zelda: Breath of the Wild", "Nintendo", 59.99, "rpg"],
    [2, "Minecraft", "Mojang Studios", 29.99, "construcao"],
    [3, "Grand Theft Auto V", "Rockstar Games", 39.99, "acao"],
    [4, "The Witcher 3: Wild Hunt", "CD Projekt Red", 49.99, "rpg"],
    [5, "Fortnite", "Epic Games", 0.00, "acao"],
    [6, "Red Dead Redemption 2", "Rockstar Games", 59.99, "aventura"],
    [7, "Call of Duty: Modern Warfare II", "Activision", 69.99, "tiro"],
    [8, "Among Us", "Innersloth", 4.99, "multiplayer"],
    [9, "Cyberpunk 2077", "CD Projekt Red", 59.99, "rpg"],
    [10, "League of Legends", "Riot Games", 0.00, "moba"],
    [11, "Valorant", "Riot Games", 0.00, "fps"],
    [12, "Apex Legends", "Respawn Entertainment", 0.00, "battle royale"],
    [13, "Elden Ring", "FromSoftware", 59.99, "rpg"],
    [14, "Overwatch 2", "Blizzard Entertainment", 0.00, "fps"],
    [15, "Stardew Valley", "ConcernedApe", 14.99, "simulacao"],
    [16, "Hollow Knight", "Team Cherry", 14.99, "aventura"],
    [17, "Animal Crossing: New Horizons", "Nintendo", 59.99, "simulacao"],
    [18, "Fall Guys", "Mediatonic", 0.00, "multiplayer"],
    [19, "Dark Souls III", "FromSoftware", 39.99, "rpg"],
    [20, "Sekiro: Shadows Die Twice", "FromSoftware", 59.99, "rpg"],
    [21, "Resident Evil Village", "Capcom", 59.99, "terror"],
    [22, "FIFA 23", "EA Sports", 59.99, "esporte"],
    [23, "The Sims 4", "Electronic Arts", 0.00, "simulacao"],
    [24, "Terraria", "Re-Logic", 9.99, "aventura"],
    [25, "PUBG: Battlegrounds", "Krafton", 29.99, "battle royale"],
    [26, "Genshin Impact", "miHoYo", 0.00, "rpg"],
    [27, "Hades", "Supergiant Games", 24.99, "acao"],
    [28, "Celeste", "Maddy Makes Games", 19.99, "plataforma"],
    [29, "Forza Horizon 5", "Playground Games", 59.99, "corrida"],
    [30, "Minecraft Dungeons", "Mojang Studios", 19.99, "aventura"],
    [31, "Dead by Daylight", "Behaviour Interactive", 19.99, "terror"],
    [32, "The Elder Scrolls V: Skyrim", "Bethesda", 39.99, "rpg"],
    [33, "Rocket League", "Psyonix", 19.99, "acao"],
    [34, "Diablo III", "Blizzard Entertainment", 39.99, "rpg"],
    [35, "Valorant", "Riot Games", 0.00, "fps"],
    [36, "Doom Eternal", "id Software", 59.99, "fps"],
    [37, "Fallout 4", "Bethesda", 29.99, "rpg"],
    [38, "Hitman 3", "IO Interactive", 59.99, "acao"],
    [39, "League of Legends", "Riot Games", 0.00, "moba"],
    [40, "Minecraft", "Mojang Studios", 29.99, "construcao"],
    [41, "Grand Theft Auto V", "Rockstar Games", 39.99, "acao"],
    [42, "The Witcher 3: Wild Hunt", "CD Projekt Red", 49.99, "rpg"],
    [43, "FIFA 23", "EA Sports", 59.99, "esporte"],
    [44, "Apex Legends", "Respawn Entertainment", 0.00, "battle royale"],
    [45, "Overwatch 2", "Blizzard Entertainment", 0.00, "fps"],
    [46, "Valorant", "Riot Games", 0.00, "fps"],
    [47, "Among Us", "Innersloth", 4.99, "multiplayer"],
    [48, "Call of Duty: Warzone", "Activision", 0.00, "battle royale"],
    [49, "Borderlands 3", "Gearbox Software", 59.99, "acao"],
    [50, "The Sims 4", "Electronic Arts", 0.00, "simulacao"],
    [51, "Red Dead Redemption 2", "Rockstar Games", 59.99, "aventura"],
    [52, "Dying Light 2", "Techland", 59.99, "acao"],
    [53, "No Man's Sky", "Hello Games", 59.99, "exploracao"],
    [54, "World of Warcraft", "Blizzard Entertainment", 0.00, "mmorpg"],
    [55, "League of Legends", "Riot Games", 0.00, "moba"],
    [56, "Minecraft", "Mojang Studios", 29.99, "construcao"],
    [57, "Valorant", "Riot Games", 0.00, "fps"],
    [58, "Tetris Effect", "Monstars Inc.", 39.99, "puzzle"],
    [59, "Monster Hunter: World", "Capcom", 39.99, "acao"],
    [60, "Minecraft Dungeons", "Mojang Studios", 19.99, "aventura"],
    [61, "The Elder Scrolls V: Skyrim", "Bethesda", 39.99, "rpg"],
    [62, "Rocket League", "Psyonix", 19.99, "acao"],
    [63, "Dead by Daylight", "Behaviour Interactive", 19.99, "terror"],
    [64, "Dark Souls III", "FromSoftware", 39.99, "rpg"],
    [65, "Hollow Knight", "Team Cherry", 14.99, "aventura"],
    [66, "Sekiro: Shadows Die Twice", "FromSoftware", 59.99, "rpg"],
    [67, "Forza Horizon 5", "Playground Games", 59.99, "corrida"],
    [68, "Animal Crossing: New Horizons", "Nintendo", 59.99, "simulacao"],
    [69, "Rocket League", "Psyonix", 19.99, "acao"],
    [70, "Minecraft", "Mojang Studios", 29.99, "construcao"],
    [71, "Cyberpunk 2077", "CD Projekt Red", 59.99, "rpg"],
    [72, "The Sims 4", "Electronic Arts", 0.00, "simulacao"],
    [73, "Stardew Valley", "ConcernedApe", 14.99, "simulacao"],
    [74, "Genshin Impact", "miHoYo", 0.00, "rpg"]
  ]

  for jogo in list_jogos:
    j = Jogo(jogo[0], jogo[1], jogo[2], jogo[3], jogo[4])
    catalogo.catalogo_jogos.inserir(j)
    catalogo.generos.inserir_por_genero(j)
  
  id = 100
  opc = 0
  while opc != 5:
    print("\n1- ADICIONAR JOGO ", "\n2- BUSCAR JOGO POR PRECO", "\n3- BUSCAR JOGOS PRO FAIXA DE PRECO", "\n4- LISTAR TODOS OS JOGOS EM ORDEM DE PRECO","\n5- BUSCAR JOGO POR GENERO", "\n6- SAIR")
    opc = int(input("Informe a opcao desejada: "))

    if opc == 1:
      print("\n")
      nome_jogo = str(input("Informe o titulo do jogo: "))
      desenvolvedor = str(input("Informe o desenvolvedor: "))
      preco = float(input("Informe o preco do jogo: "))
      genero = str(input("Informe o genero: "))
      novo_jogo = Jogo(id, nome_jogo, desenvolvedor, preco, genero)
      catalogo.catalogo_jogos.inserir(novo_jogo)
      id += 1
      print("::JOGO ADICIONADO COM SUCESSO!::")
    
    elif opc == 2:
      print("\n")
      preco_buscar = float(input("Informe o preco que deseja pesquisar: R$"))
      catalogo.catalogo_jogos.buscar_por_preco(preco_buscar)
      print("::JOGO ENCONTRADO::")
      

    elif opc == 3:
      print("\n")
      preco_minimo = float(input("Infome o valor minimo: R$"))
      preco_maximo = float(input("Informe o valor maximo: R$"))
      print("::LISTA DE JOGOS ENTRE R$", preco_minimo, "E R$", preco_maximo, "::")
      catalogo.catalogo_jogos.busca_por_faixa_preco(preco_minimo, preco_maximo)
    
    elif opc == 4:
      print("\n::LISTA DE JOGOS::")
      em_ordem(catalogo.catalogo_jogos.raiz)

    elif opc == 5:
      genero_busca = str(input("Informe o genero que deseja buscar: "))
      print("\n::JOGOS DO GENERO", genero_busca, "::")
      catalogo.generos.obter_jogos(genero_busca)

    elif opc == 6:
      print("Saindo...")
      break  

    else:
      print("::OPCAO INVALIDA!::")
main()
