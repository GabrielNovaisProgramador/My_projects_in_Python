''' Abaixo criei um programa que solicita ao usuário, o valor de um produto
e quantos produtos ele quer comprar. Através do que ele passar ao programa
o programa retorna o valor de quanto ele vai pagar.'''

valor_unitario = float(input("Informe o valor do produto que você "
                             "quer comprar: "))
quantidade = int(input("Informe a quantidade de quantos produtos desse "
                       "você quer: "))
print(f"O total da compra é: R${valor_unitario * quantidade}")
