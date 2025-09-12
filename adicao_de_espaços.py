# No exemplo abaixo temos uma variavel que está armazenando o valor 9
# e nos comandos prints abaixo estou informando o inteiro 9 junto com
# a mensagem, onde o 9 está sendo acrescentado por zeros à esquerda,
# espaços vazios e está entre colchetes para delimitar o espaço.
aula = 9
print("Esta é à aula de número %03d" % aula)
print("Esta é à aula de número %3d" % aula)
print("Esta é à aula de número [%3d]" % aula)
print("Esta é à aula de número [%03d]" % aula)
# Repare que nessa última impressão, o programa coloca o inteiro entre colchetes
# e três casas de espaços à direita.
print("Esta é à aula de número [%-3d]" % aula)

