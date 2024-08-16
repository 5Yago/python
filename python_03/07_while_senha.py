# Reset contador e limite de tentativas

i = 1
while i <= 3:

    user = input("Informe o usúario: ")
    senha = input("Informe a senha: ")

    # Checagem 
    if user != "Gisele" or senha != "123":
        print("Usúario ou Senha incorretos!")
        print (" ")

    else:
        print(" ")
        print(f"Bem vindo, {user}!")
        break
else:
    print("Tentativas esgotadas!")