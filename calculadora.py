# funções para as operações básicas
def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y 

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro: Divisão por 0!"
    return x / y

# menu de opções
print("Selecione a operação: ")
print("1 - Soma")
print("2 -Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

# entrada de dados do usuário
opcao = input("Digite a opção (1/2/3/4): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))


# verificar operação e exibir resultado
if opcao == "1":
    print(f"{num1} + {num2} = {soma (num1, num2)}")
elif opcao == "2":
    print(f"{num1} - {num2} = {subtracao (num1, num2)}")
elif opcao == "3":
    print(f"{num1} * {num2} = {multiplicacao (num1, num2)}")
elif opcao == "4":
    print(f"{num1} / {num2} = {divisao (num1, num2)}")
else:
    print("Opção inválida!")