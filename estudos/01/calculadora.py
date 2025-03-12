# Solicitar dois números ao usuário
# Float é um tipo de dados que só recebe com (.) ponto
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realizar as operações
# Soma é a variavel que vai armazenar outras duas variaveis que serão inseridas pelos usuarios
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2 if num2 != 0 else "Erro: Divisão por zero"

# Exibir os resultados
print(f"\nResultado da soma: {soma}")
print(f"Resultado da subtração: {subtracao}")
print(f"Resultado da multiplicação: {multiplicacao}")
print(f"Resultado da divisão: {divisao}")
