import pygame
import os

# Inicializa o mixer de áudio
pygame.mixer.init()
# 0.1 é bem baixinho, 1.0 é o máximo.
pygame.mixer.music.set_volume(0.5)

def tocar_musica(nome_arquivo):
    if os.path.exists(nome_arquivo):
        pygame.mixer.music.load(nome_arquivo)
        pygame.mixer.music.play()
        print(f"Tocando agora: {nome_arquivo}")
    else:
        print("Erro: O arquivo não foi encontrado na pasta!")

# --- CONFIGURAÇÃO DE CAMINHO ---
# Isso descobre a pasta onde o player.py está salvo
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
# Isso cria o caminho completo para o arquivo musica.mp3
caminho_musica = os.path.join(diretorio_atual, "musica.mp3")

# --- EXECUÇÃO ---
tocar_musica(caminho_musica)

# O input deve ser a ÚLTIMA coisa do código
input("Pressione Enter para encerrar o player...")