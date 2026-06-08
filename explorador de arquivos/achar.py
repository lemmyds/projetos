import os

def pesquisar():
    caminho = input('Cole o caminho da pasta: ').strip('"')
    
    # 1. Tente abrir a pasta ANTES de perguntar o tipo de busca
    try:
        arquivos = os.listdir(caminho)
    except FileNotFoundError:
        print("Caminho inválido! Verifique a pasta.")
        return

    # 2. Agora pergunta o que o usuário quer
    perg1 = input('você quer formato ou nome? ')
    
    if perg1 == 'formato':
        extensao = input('Qual formato (ex: .txt, .py)? ')
        encontrou = False
        for item in arquivos:
            if item.endswith(extensao):
                print(f"Achei: {item}")
                encontrou = True
        if not encontrou:
            print("Infelizmente não achamos nenhum arquivo com esse formato.")

    else: # Opção de busca por nome
        termo_busca = input('O que você quer procurar no nome do arquivo? ').lower()
        encontrou = False
        for item in arquivos:
            if termo_busca in item.lower():
                print(f"Encontrei: {item}")
                encontrou = True
        
        if not encontrou:
            print("Nenhum arquivo encontrado com esse nome.")

pesquisar()