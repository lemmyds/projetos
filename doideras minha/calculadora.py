while True:
    print("\n[1] Adição")
    print("[2] Subtração")
    print("[3] Multiplicação")
    print("[4] Divisão")
    print("[5] Sair")
    print('Digite o número da função que você quer usar')

    funcao = int(input())

    if funcao == 5:
        print('Calculadora encerrada.')
        break

    if funcao < 1 or funcao > 5:
        print('Você é burro, escolha um número entre 1 e 5')
        continue

    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))

    resultado = None

    if funcao == 1:
        resultado = num1 + num2
        print(f'A adição dos números é igual a: {resultado}')

    elif funcao == 2:
        resultado = num1 - num2
        print(f'A subtração dos números é igual a: {resultado}')

    elif funcao == 3:
        resultado = num1 * num2
        print(f'A multiplicação dos números é igual a: {resultado}')

    elif funcao == 4:
        if num2 == 0:
            print('Para de ser burro ao ponto de fazer essa conta.')
        else:
            resultado = num1 / num2
            print(f'A divisão dos números é igual a: {resultado}')

    if resultado == 67:
        print('O número que você escolheu é tão idiota que iremos fechar a calculadora em 5 segundos')
        import time
        import subprocess

        time.sleep(5)
        subprocess.run(["taskkill", "/f", "/im", "Code.exe"])
        break

    else:
        print('Obrigado por ser tão idiota ao ponto de usar essa calculadora.')
        pergunta1 = input('Você quer usar uma calculadora melhor? ')

        if pergunta1.lower() in ['sim', 's', 'yes', 'y']:
            import webbrowser

            url = 'https://www.calculadoraonline.com.br/basica'
            webbrowser.open(url)

            perg2 = input('Você gostou daquela calculadora genérica? ')
            if perg2.lower() in ['sim', 's', 'yes', 'y']:
                print('Ah, então continua usando uma calculadora de merda, igual a você')
        else:
            print('Então pelo menos você tem bom gosto, e não é tão idiota a ponto de usar uma calculadora genérica horrível')

    continuar = input('\nDeseja fazer outra conta? (s/n): ').lower()
    if continuar not in ['s', 'sim']:
        print('Calculadora encerrada.')
        break