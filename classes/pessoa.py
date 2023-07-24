class Pessoa:
  def __init__(self, nome, idade):
    self._nome = self._valida_nome(nome)
    self._idade = self._valida_idade(idade)
  
  @property
  def idade(self):
      return self._idade
    
  @property
  def nome(self):
    return self._nome
  
  def _valida_nome(self, nome):
    nome = nome.lower().strip()
    if(nome == '' or nome == None or len(nome) < 3):
      raise NameError('Não é permitida a entrada de nomes vazios ou menores que tres caracteres')
    else:
      return nome.title()
  
  def _valida_idade(self, idade):
    try:
      idade = int(idade)
    except ValueError:
      raise ValueError('Para a idade somente a entrada de números é aceita!')
    else:
      if(idade < 18):
        raise ValueError('Não é permitido o registro de menores de idade')
      else:
        return idade
