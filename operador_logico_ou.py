''' Passando o funcionamento do operador lógico "ou".             '''

a = True or True
b = True or False
c = False or True
d = False or False

print("a =",a)
print("b =",b)
print("c =",c)
print("d =",d)

# ---------------------------------------------------------------------------------------- #
print("\n\n")
" Ordem de avaliação de expressão lógica : not, and e or."

#                     True or False and not True
#                       True or False and  False
#                           True or False
#                               True

salario = 937
idade = 18

'''            salario > 1000 and 20 > idade)
                  937 > 1000  and 20 > 18 
                       False  and  True
                            False                                                    '''

print(salario > 1000)
print(20 > idade)
print(False and True)