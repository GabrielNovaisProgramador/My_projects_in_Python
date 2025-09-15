'''Abaixo temos uma concatenação entre strings, ou seja à união de dois
textos armazenados em váriaveis diferentes e junta em uma só mensagem.'''

texto1 = "Olá, "
texto2 = "tudo bem? "
texto_concatenado = texto1 + texto2
print(texto_concatenado)

''' Abaixo você informa uma string, e o programa vai multiplicar essa string
por 10. Ou seja repetindo o texto por 10 vezes.'''

alimento = "Pão "
multiplica = alimento * 10
print(multiplica)

''' Abaixo eu usei %s que exibi às strings armazenada em alguma váriavel
e %d para número inteiros. Tanto o %s como o %d segue uma sequência de
informações armazenadas na váriavel.'''

nome = "João da Silva"
idade = 38
filhos = 2
frase = "O jogador %s tem %d anos e %d filhos." % (nome, idade, filhos)
print(frase)


