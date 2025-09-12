# Na impressão, eu consigo substituir os valores armazenados nas variaveis
# pelo "{}" e passando o comando format junto com o nome da variavel que contem
# o valor que eu quero que seja impresso.

nome = "José da Silva"
idade = 50
filhos = 3
frase = "{} tem {} anos de idade e tem {} filhos".format(nome,idade,filhos)
print(frase)

# Outra foma de usar o comando "format". Abaixo colocamos os "{}"
# e à posição que se encontra o conteúdo que você queira exibir na frase.

frase = "Olá, eu vou viajar de {3}".format('bicicleta','moto','trem','carro')
print(frase)