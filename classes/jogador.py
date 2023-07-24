from classes.pessoa import Pessoa


class Jogador(Pessoa):
  def __init__(self, nome, idade, apelido):
    super().__init__(nome, idade)