from classes.blackJack import BlackJack
from classes.jogador import Jogador
from classes.baralho import Baralho

bl = BlackJack()
baralho = Baralho()
while(True):
  BlackJack.menu_inicial()
  op = input('Opção: ')
  if(op == '1'):
    if(len(bl) < 4):
      nome =  input("Digite seu nome: ")
      idade = input("Digite sua idade: ")
      apelido = input("Digite seu apelido: ")
      try:
        jogador = Jogador(nome, idade, apelido)
      except NameError as e:
        print(f'Não foi possível adicionar um jogador: {e}')
      except ValueError as e:
        print(f'Não foi possível adicionar um jogador: {e}')
      else:
        print(f'Jogador {jogador.apelido} adicionado')
        bl.adicionar_jogador(jogador)
    else:
      print('O jogo só permite no máximo 4 jogadores')
  elif(op == '2'):
    if(len(bl) == 0):
      print('A lista de jogadores está vazia')
      continue
    bl.exibir_jogadores()
    apelido = input('Digite o apelido do jogador que deseja remover: ')
    jogador_removido = bl.remover_jogador(apelido)
    if(jogador_removido):
      print(f'O jogador {jogador_removido} foi removido')
    else:
      print('Jogador não encontrado')
  elif(op == '3'):
    bl.exibir_jogadores()
  elif(op == '0'):
    if(len(bl) < 2):
      print('Para iniciar o jogo é nescessario no mínimo 2 jogadores')
      break
    else:
      print('Iniciando o jogo...')
      break
  else:
    print('Opção inválida')

while(not bl.encerrar_jogo()):
  for jogador in bl:
    while(True):
      op2 = '0'
      print('------------------------------')
      print(f'O jogador {jogador.apelido} esta jogando')
      print('Para pedir uma cartas digite - 1')
      print('Para passar a vez digite - 2')
      print('Para visualizar as suas cartas e pontos - 3')
      print('------------------------------')
      print('\n')
      op = input('Opção: ')
      if(op == '1'):
        jogador.solicitar_carta(baralho.seleciona_carta())
        while(True):
          print('------------------------------')
          print('Para visualizar as suas cartas e pontos - 1')
          print('Finalizar a vez - 2')
          print('------------------------------')
          print('\n')
          op2 = input('Opção: ')
          if(op2 == '1'):
            jogador.exibe_cartas_pontos()
          elif(op2 == '2'):
            break
          else:
            print('Opção inválida')
      elif(op == '2'):
        jogador.passar_vez()
        break
      elif(op == '3'):
        jogador.exibe_cartas_pontos()
      else:
        print('Opção inválida')
      if(op2 == '2'):
        op2 = 0
        break
bl.exibe_resultado()
