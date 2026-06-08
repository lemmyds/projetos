

def menu():
    print('CALCULADORA')
    print('Escreva o valor abaixo o que você deseja')
    print('[1] Adição')
    print('[2] Subtração')
    print('[3] Multiplicação')
    print('[4] Divisão')

def pegar_numero():
    while True:
        try:
            return float(input('Digite um numero:'))
        except ValueError:
            print('Esse valor n e possivel')
def adicao(a, b):
    return a + b

def subtracao(a, b):

    return a - b
def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "A divisão de zero e invalida"
    return a / b
while True:
    menu()

    try:
        opcao = int(input("Qual numero dejesa?: "))
    except ValueError:
        print('Esse valor n e possivel')
        continue
    if opcao == 1:
        num1 = pegar_numero()
        num2 = pegar_numero()
        print(adicao(num1, num2))
    elif opcao == 2:
        num1 = pegar_numero()
        num2 = pegar_numero()
        print(subtracao(num1, num2))
    elif opcao == 3:
        num1 = pegar_numero()
        num2 = pegar_numero()
        print(multiplicacao(num1, num2))
    elif opcao == 4:
        num1 = pegar_numero()
        num2 = pegar_numero()
        print(divisao(num1, num2))
    else:
        print('Opção invalida')

    while True:
        perg1 = input('Você deseja continuar a usar a calculadora? ').strip().lower()
        if perg1 in ["s", "sim", "y", "yes"]:
            break
        elif perg1 in ["n", "nao", "não", "no", "nop", "not", "nope", "oh no i sorry baby"]:
            print('Até mais!')
            exit()
        else:
            print('Resposta não reconhecida. Digite sim ou não.')
