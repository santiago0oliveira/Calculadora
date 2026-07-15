"""" crie um progrma que:
solicita ao usuario uma operação (adição, subtração,
 multiplicação, divisão) e dois numeros.
 execute a operação e exiba o resultado.
 isso deve ser repetido até que o usuario digite um a opção de "saida" como operação
 """

def operacao(op, a, b):
    if op == '1':
        return a + b
    elif op == '2':
        return a - b
    elif op == '3':
        return a * b
    elif op == '4':
        if b != 0:
            return a / b
        else:
            return "Erro: Divisão por zero"
    else:
        return "Operação inválida"

while True:
    print("\n Escolha uma operação: ")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    print("\n")

    opcao = input("Digite o número da operação (1 - 5): ")

    if opcao == '5':
        print("Encerrando o programa. ")
        print("\n")
        break
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        resultado = operacao(opcao, num1, num2)
        print(f"\nO resultado da operação é: {resultado}")
        print("\n")
    except ValueError:
        print("Erro: Digite um número válido. ")
        print("\n")



 