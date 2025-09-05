a = 10
proposicao1 = (a > 1)
proposicao2 = (a == 5)

resultado = proposicao1 and proposicao2
print(resultado,"\n\n\n")

# Se você rodar esse programa, vai te gerar o resultado False.
# Isso porque para gerar o operador lógico True, você precisa
#satisfazer às todas às condições ou seja, tanto à "proposicao1"
#como à "proposicao2" tem que ser verdadeiras, para o resultado
#da expressão lógica ser True (verdadeira).

salario = 937
idade = 20

condicao_um = (salario > 1000)
#                  False
condicao_dois = (idade > 18)
#                   True
condicao_tres = (salario > 1000 and idade > 18)
#                    (False      e      True) = False
