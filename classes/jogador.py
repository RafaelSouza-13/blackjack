from classes.pessoa import Pessoa

class Jogador(Pessoa):
  def __init__(self, nome, idade, apelido):
    self._apelido = self._valida_apelido(apelido)
    self._pontos = 0
    self._cartas = []
    self._encerrar = False
    super().__init__(nome, idade)
  
  @property
  def apelido(self):
    return self._apelido
  
  @property
  def pontos(self):
    return self._pontos
  
  @property
  def encerrar(self):
    return self._encerrar

  def solicitar_carta(self, carta):
    carta = self._verifica_as(carta)
    self._pontos += carta
    self._cartas.append(carta)
    self._encerrar = False
    print(f'Carta retirada: {carta}')
  
  def _verifica_as(self, carta):
    if(carta == 1):
      print('Voce retirou um Ás, pode escolher dois valores, 1 ou 11')
      escolha = input('Digite 11 ou 1: ')
      while(True):
        if(escolha == '1'):
          print('Valor 1 escolhido para o ás')
          return 1
        elif(escolha == '11'):
          print('Valor 11 escolhido para o ás')
          return 11
        else:
          print('Valor invalido')
    return carta
  
  def passar_vez(self):
    self._encerrar = True
    
  def exibe_cartas_pontos(self):
    print(f'Cartas retiradas: {self._cartas}')
    print(f'total de pontos {self.pontos}')
  
  def _valida_apelido(self, apelido):
    apelido = apelido.lower().strip()
    if(apelido == "" or apelido == None):
      raise NameError('Não é aceito entrada em branco em apelido')
    return apelido.title()
    
  def __str__(self) -> str:
    return f'{self.apelido}'