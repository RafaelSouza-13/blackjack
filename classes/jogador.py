import random
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

  def solicitar_carta(self):
    valor_carta = random.randint(1, 13)
    self._pontos += valor_carta
    self._cartas.append(valor_carta)
    self._encerrar = False
    return valor_carta
  
  def passar_vez(self):
    self._encerrar = True
    
  def exibe_cartas_pontos(self):
    print(self._cartas)
    print(self.pontos)
  
  def _valida_apelido(self, apelido):
    apelido = apelido.lower().strip()
    if(apelido == "" or apelido == None):
      raise NameError('Não é aceito entrada em branco em apelido')
    return apelido.title()
    
  def __str__(self) -> str:
    return f'{self.apelido}'