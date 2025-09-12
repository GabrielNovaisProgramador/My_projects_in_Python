# Neste exemplo, eu demonstrei que é possível usar o caractere "%" mais o
# tipo do valor. Exemplo: f de float ou d de inteiro para requerir
# os valores armazenados nas váriaveis por sequência.

valor_unitario = 15.70
quantidade = 5
valor_total = valor_unitario * quantidade
frase = "O produto custa R$%.2f. Eu comprei %d. " \
        "E paguei ao todo R$%.2f" % (valor_unitario,quantidade,valor_total)
print(frase)

# Alerta: O "." mais um inteiro representa o tanto de casas após à vírgula
# você quer. No programa acima eu coloquei "2f".


# Abaixo eu demonstro como faço para o programa imprimir o sinal de "%".
percent = 17.5
frase = "A taxa de juros é de %.2f%%" % percent
print(frase)