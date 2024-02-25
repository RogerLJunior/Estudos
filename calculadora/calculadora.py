def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero"

def calcular(operacao, a, b):
    if operacao == "+":
        return adicao(a, b)
    elif operacao == "-":
        return subtracao(a, b)
    elif operacao == "*":
        return multiplicacao(a, b)
    elif operacao == "/":
        return divisao(a, b)
    else:
        return "Operação inválida"

def main():
    while True:
        print("Escolha a operação:")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")

        escolha = input("Digite o número da operação desejada: ")

        if escolha == "5":
            print("Encerrando a calculadora.")
            break

        if escolha not in ["1", "2", "3", "4"]:
            print("Escolha inválida. Tente novamente.")
            continue

        operacao = ""
        if escolha == "1":
            operacao = "+"
        elif escolha == "2":
            operacao = "-"
        elif escolha == "3":
            operacao = "*"
        elif escolha == "4":
            operacao = "/"

        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))

        resultado = calcular(operacao, a, b)
        print(f"Resultado: {resultado}\n")
