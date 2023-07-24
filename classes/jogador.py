from classes.pessoa import Pessoa


class Jogador(Pessoa):
  def __init__(self, nome, idade, apelido):
    self._apelido = self.valida_apelido(apelido)
    self.pontos = 0
    super().__init__(nome, idade)
  
  @property
  def apelido(self):
    return self._apelido
  
  def valida_apelido(self, apelido):
    if(apelido == "" or apelido == None):
      raise NameError('Não é aceito entrada em branco em apelido')
    else:
      apelido = apelido.lower().strip()
      return apelido.title()
    
  def __str__(self) -> str:
    return f'{self.apelido}'