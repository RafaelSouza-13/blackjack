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

  def exibir_jogadores(self):
    for index, jogadores in enumerate(self._lista_jogadores):
      print(f'Jogador {index + 1}: {jogadores}')
  
  def __getitem__(self, index):
    return self._lista_jogadores[index]
  
  def __len__(self):
    return len(self._lista_jogadores)

  @classmethod
  def menu_inicial(cls):
    print('------------------------------')
    print('No minimo 2 jogadores e no maximo 4')
    print('Para adicionar um jogador digite - 1')
    print('Para remover um jogador digite - 2')
    print('Para visualizar os jogadores cadastrados digite - 3')
    print('Para jogar digite - 4')
    print('------------------------------')
    print('\n')
  