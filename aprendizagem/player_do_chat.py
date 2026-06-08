import pygame
import os
import asyncio
import tkinter as tk
from tkinter import messagebox
from shazamio import Shazam # A biblioteca "mágica"

# Inicialização padrão
pygame.mixer.init()
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
playlist = [f for f in os.listdir(diretorio_atual) if f.endswith(".mp3")]

# Função assíncrona para o Shazam (ele precisa de internet)
async def identificar_shazam(caminho_arquivo):
    shazam = Shazam()
    out = await shazam.recognize_song(caminho_arquivo)
    if out.get('track'):
        return out['track']['share']['subject']
    return "Não consegui reconhecer essa..."

def acionar_shazam():
    try:
        selecionada = lista_box.get(lista_box.curselection())
        caminho = os.path.join(diretorio_atual, selecionada)
        
        status_label.config(text="Analisando ondas sonoras...", fg="#3498db")
        janela.update()
        
        # Roda a busca sem travar a janela
        resultado = asyncio.run(identificar_shazam(caminho))
        
        messagebox.showinfo("Shazam Identificou!", f"Música: {resultado}")
        status_label.config(text=f"Identificado: {resultado}", fg="#00FF00")
    except Exception as e:
        messagebox.showerror("Erro", "Selecione a música na lista primeiro!")

# --- Sua Interface Customizada ---
janela = tk.Tk()
janela.title("Python Player - Edição Shazam")
janela.geometry("450x550")
janela.configure(bg="#051937") # Azul escuro estilo Shazam

tk.Label(janela, text="JUKEBOX INTELIGENTE", font=("Impact", 20), bg="#051937", fg="#0081cf").pack(pady=15)

lista_box = tk.Listbox(janela, width=45, height=8, bg="#004d7a", fg="white", font=("Consolas", 10))
for musica in playlist:
    lista_box.insert(tk.END, musica)
lista_box.pack(pady=10)

status_label = tk.Label(janela, text="Pronto para identificar", bg="#051937", fg="#a8eb12", font=("Arial", 10, "italic"))
status_label.pack(pady=5)

# Botão Shazam (O Diferencial)
btn_shazam = tk.Button(janela, text="🔎 IDENTIFICAR MÚSICA", command=acionar_shazam, bg="#0081cf", fg="white", font=("Arial", 10, "bold"), height=2)
btn_shazam.pack(pady=10, fill="x", padx=40)

# Controles Básicos
frame_controles = tk.Frame(janela, bg="#051937")
frame_controles.pack(pady=10)

tk.Button(frame_controles, text="▶ PLAY", width=12, command=lambda: [pygame.mixer.music.load(os.path.join(diretorio_atual, lista_box.get(lista_box.curselection()))), pygame.mixer.music.play()], bg="#00afb9", fg="white").grid(row=0, column=0, padx=5)
tk.Button(frame_controles, text="⏹ STOP", width=12, command=pygame.mixer.music.stop, bg="#f07167", fg="white").grid(row=0, column=1, padx=5)

janela.mainloop()