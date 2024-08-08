peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em centimetros: "))

imc = peso / ((altura/100) ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 24.9:
    classificacao = "Peso normal"
elif 25 <= imc < 29.9:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

# Exibe o resultado
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")