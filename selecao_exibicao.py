email = "devpython@gmail.com"
indice = email.index(".com")
print(indice)# Vai imprimir à posição 15

indice = email.index("@gmail")
print(indice)# Será impresso à posição 9 do nosso gmail.

indice = email.index("@")
print(indice)# Vai imprimir à posição 9 que se encontra no gmail.

"Outro exemplo com email"

email = "felipeteixeira@gmail.com"
indice_arroba = email.index("@")
usuario = email[0:indice_arroba]
print("O nome de usuário é:",usuario)
# Será impresso então "O nome de usuário é felipeteixeira"

email = "evaldowolkers@gmail.com"
indice_arroba = email.index("@")
indice_ponto = email.index(".")
provedor = email [indice_arroba+1:indice_ponto]
print("O nome do provedor é: ",provedor)
# Será impresso "O nome do provedor é: gmail

email = "joaosilva@gmail.com"
usuario, dominio = email.split("@")
print("Usuário:", usuario)
print("Domínio:", dominio)

"Será impresso da seguinte forma então." \
"Usuário: joao.silva"
"Domínio: gmail.com"

'''Agora que temos o domínio separado podemos procurar o "." para
identificá-lo e separar o provedor'''

email = "joaosilva@gmail.com"
usuario, dominio = email.split("@")
indice_ponto = dominio.index(".")
provedor = dominio[0:indice_ponto]
print("O usuario é:",usuario)
print("O dominio é:",dominio)
