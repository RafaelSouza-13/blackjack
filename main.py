from classes.blackJack import BlackJack
from classes.jogador import Jogador

bl = BlackJack()
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
  elif(op == '4'):
    if(len(bl) < 2):
      print('Para iniciar o jogo é nescessario no mínimo 2 jogadores')
      continue
    else:
      break
  else:
    print('Opção inválida')
