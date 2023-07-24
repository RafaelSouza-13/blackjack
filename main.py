from classes.pessoa import Pessoa

nome =  input("Digite seu nome: ")
idade = input('Digite sua idade: ')
pessoa = Pessoa(nome, idade)
print(pessoa.nome)
print(pessoa.idade)