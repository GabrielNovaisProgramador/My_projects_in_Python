'''Abaixo você vai digitar o seu nome completo. E o programa vai
escrever uma confirmação com o seu nome.'''

nome_completo = input("Informe seu nome completo: ")
print(f"Seu nome é {nome_completo}")

'''Abaixo você informa qual é a linguagem de programação atual que você está
aprendendo para o programa te confirmar.'''

resposta = input("Informe à resposta correta: \n"
                 "Qual linguagem você está aprendendo agora?\n"
                 "a) Python\n"
                 "b) Java\n"
                 "Resposta: ")
print("Sua resposta foi:",resposta)

'''Abaixo você informa um número inteiro, e através do seu número o programa
vai somar com 10 e vai retornar uma confimação com à soma correta.'''

numero = int(input("Informe um número inteiro: "))
soma = 10 + numero
print(f"10 + {numero} é",soma)

'''Abaixo só muda que você informa ao programa um número decimal para ele
 realizar à soma e te retornar o valor com uma mensagem.'''

numero = float(input("Informe um número com decimal: "))
soma = 4.5 + numero
print(f"A soma de 4.5 + {numero} é",soma)
