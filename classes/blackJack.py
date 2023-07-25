class BlackJack:
  def __init__(self):
    self._lista_jogadores = []
  
  def adicionar_jogador(self, jogador):
    self._lista_jogadores.append(jogador)
  
  def remover_jogador(self, apelido):
    for jogador in self._lista_jogadores:
      if(jogador.apelido.lower() == apelido.lower()):
        return self._lista_jogadores.pop()
    return False

  def encerrar_jogo(self):
    for jogador in self._lista_jogadores:
      if(jogador.encerrar == False):
        return False
    return True
  
  def _resultado(self):
    maior = 0
    lista = []
    for jogador in self._lista_jogadores:
      if(jogador.pontos > maior and jogador.pontos <= 21):
        maior = jogador.pontos
        lista.clear()
        lista.append(jogador)
      elif(jogador.pontos == maior):
        lista.append(jogador)
    return lista

  def exibe_resultado(self):
    lista = self._resultado()
    print('Resultado da partida')
    if(len(lista) == 0):
      print('Não houve ganhador')
      print('Todos os jogadores ultrapassaram 21 pontos')
      for jogador in self._lista_jogadores:
        print(f'Jogador {jogador}: {jogador.pontos} - 21 pontos')
    elif(len(lista) == 1):
      if(lista[0].pontos == 21):
        print(f'O jogador {lista[0]} ganhou com blackjack')
      else:
        print(f'O jogador {lista[0]} ganhou com {lista[0].pontos} - 21 pontos')
    else:
      print('Empate entre os jogadores: ')
      for jogador in lista:
        if(jogador.pontos == 21):
          print(f'Jogador {jogador}: Blackjack')
        else:
          print(f'Jogador {jogador}: {jogador.pontos} - 21 pontos')
    print('fim do jogo...')
      

  def exibir_jogadores(self):
    for index, jogadores in enumerate(self._lista_jogadores):
      print(f'Jogador {index + 1}: {jogadores}')
  
  def __getitem__(self, index):
    return self._lista_jogadores[index]
  
  def __len__(self):
    return len(self._lista_jogadores)

  @classmethod
  def menu_inicial(cls):
    print('\n')
    print('No minimo 2 jogadores e no maximo 4')
    print('------------------------------')
    print('Para adicionar um jogador digite - 1')
    print('Para remover um jogador digite - 2')
    print('Para visualizar os jogadores cadastrados digite - 3')
    print('Para jogar digite - 0')
    print('------------------------------')
    print('\n')
  