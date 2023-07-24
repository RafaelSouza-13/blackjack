from classes.black_jack import BlackJack
from classes.jogador import Jogador
# from classes.black_jack import BlackJack

bl = BlackJack()
lista_jogadores = []
op = 0
while(op != 2):
  print('Para adicionar um jogador digite - 1')
  print('Para remover um jogador digite - 2')
  print('Para continuar digite - 3')
  op = input('Opção: ')
  if(op == '1'):
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
      print('Jogador adicionado')
      lista_jogadores.append(jogador)
  elif(op == '2'):
    if(len(lista_jogadores) == 0):
      print('A lista de jogadores está vazia')
      continue
    for j in lista_jogadores:
      print(j)
    remover = input('Digite o apelido do jogador que deseja remover: ')
    for j in lista_jogadores:
      print(j)
  elif(op == '3'):
    if(len(lista_jogadores) < 2):
      print('Para iniciar o jogo é nescessario no mínimo 2 jogadores')
      continue
    else:
      break
    
for j in lista_jogadores:
  print(j)