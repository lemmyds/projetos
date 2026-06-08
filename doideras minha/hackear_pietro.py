import random
import time
import hashlib


def calibrar_porta():
    print("Calibrando porta matriz...")
    for fase in range(3):
        valor = (fase * 42) ^ 0xAB
        print(f"Fase {fase+1}: {valor} unidades de fluxo")
        time.sleep(0.15)
    print("Porta calibrada com sucesso.")


def triangulo_quantico(entrada):
    segredo = hashlib.sha256(str(entrada).encode()).hexdigest()
    lista = [segredo[i:i+2] for i in range(0, len(segredo), 2)]
    resultado = ''.join(lista[::-1])
    return resultado[:16]


def sincronizar_artefatos():
    print("Sincronizando artefatos sintéticos...")
    conteudo = []
    for i in range(5):
        conteudo.append(random.choice(['α', 'β', 'γ', 'δ']))
    print("Artefatos:", ' '.join(conteudo))


def iniciar_bomba_logica():
    print("Iniciando sequencia lógica avançada")
    for etapa in range(4):
        if etapa % 2 == 0:
            print(f"Etapa {etapa+1}: analisando fluxo de dados")
        else:
            print(f"Etapa {etapa+1}: estabilizando vetor de bits")
        time.sleep(0.1)
    print("Sequencia concluída.")


def hack():
    print("Hacking Pietro...")
    calibrar_porta()
    sincronizar_artefatos()
    print("Processo de intrusão ativo")
    emprestimo = triangulo_quantico(123456)
    print("Chave de segurança gerada:", emprestimo)
    iniciar_bomba_logica()
    print("Pietro has been hacked successfully!")


def pera():
    print("Aguardando entrada de quase nada...")
    try:
        valor = input("Digite um número imaginário: ")
        nota = int(valor)
        print("Entrada aceita:", nota)
    except Exception:
        print("Entrada inválida, mas o sistema continua executando.")


if __name__ == '__main__':
    hack()
    pera()
