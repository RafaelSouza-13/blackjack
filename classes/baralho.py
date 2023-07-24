import random

class Baralho:
  def __init__(self):
    self._baralho = self._gera_baralho()
  
  def _gera_baralho(self):
    baralho = []
    contador = 0
    for i in range(1, 14):
      while(contador < 4):
        if(i >= 10):
          baralho.append(10)
        else:
          baralho.append(i)
        contador += 1
      contador = 0
    random.shuffle(baralho)
    return baralho

  def seleciona_carta(self):
    if(len(self._baralho ) > 0):
      return self._baralho.pop(0)
    else:
      print('O baralho chegou ao fim, gerando um novo baralho')
      self._baralho = self._gera_baralho()
      return self.seleciona_carta(self)
