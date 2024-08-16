# Lista usando laço for
print (" ")
print ("Lista de lojas")
print (" ")

lojas = ["Santo André", "São Bernardo", "SCS", "Mauá"]

#listar usando laço com índice
for i, loja in enumerate(lojas, 1):
    print(f"{i} - {loja}")