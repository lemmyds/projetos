import tkinter as tk
from tkinter import messagebox
import webbrowser
import subprocess
import time


def calcular(operacao):
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())

        if operacao == 'adição':
            resultado = num1 + num2
        elif operacao == 'subtração':
            resultado = num1 - num2
        elif operacao == 'multiplicação':
            resultado = num1 * num2
        elif operacao == 'divisão':
            if num2 == 0:
                messagebox.showerror('Erro', 'Não é possível dividir por zero.')
                return
            resultado = num1 / num2

        resultado_label.config(text=f'Resultado: {resultado}')

        if resultado == 67:
            messagebox.showwarning('Aviso', 'Resultado #$ detectado. O VS Code fechara quando você clicar em OK.')
            janela.after(1, lambda: subprocess.run(['taskkill', '/f', '/im', 'Code.exe']))

    except ValueError:
        messagebox.showerror('Erro', 'Digite números válidos.')


def abrir_calculadora_online():
    webbrowser.open('https://www.calculadoraonline.com.br/basica')


janela = tk.Tk()
janela.title('Calculadora Insana')
janela.geometry('420x520')
janela.resizable(False, False)
janela.configure(bg='#1e1e2f')

# Título
titulo = tk.Label(
    janela,
    text='Calculadora Insana',
    font=('Arial', 22, 'bold'),
    bg='#1e1e2f',
    fg='#ffffff'
)
titulo.pack(pady=20)

# Frame principal
frame = tk.Frame(janela, bg='#2a2a40', bd=0)
frame.pack(padx=20, pady=10, fill='both', expand=True)

# Entradas
entrada1 = tk.Entry(frame, font=('Arial', 16), justify='center', bd=0, bg='#f0f0f0')
entrada1.pack(pady=15, ipadx=10, ipady=10)

entrada2 = tk.Entry(frame, font=('Arial', 16), justify='center', bd=0, bg='#f0f0f0')
entrada2.pack(pady=15, ipadx=10, ipady=10)

# Frame dos botões
botoes_frame = tk.Frame(frame, bg='#2a2a40')
botoes_frame.pack(pady=20)

estilo_botao = {
    'font': ('Arial', 13, 'bold'),
    'width': 12,
    'height': 2,
    'bd': 0,
    'cursor': 'hand2'
}

btn_add = tk.Button(botoes_frame, text='Adição', bg='#4caf50', fg='white', command=lambda: calcular('adição'), **estilo_botao)
btn_add.grid(row=0, column=0, padx=8, pady=8)

btn_sub = tk.Button(botoes_frame, text='Subtração', bg='#f44336', fg='white', command=lambda: calcular('subtração'), **estilo_botao)
btn_sub.grid(row=0, column=1, padx=8, pady=8)

btn_mul = tk.Button(botoes_frame, text='Multiplicação', bg='#2196f3', fg='white', command=lambda: calcular('multiplicação'), **estilo_botao)
btn_mul.grid(row=1, column=0, padx=8, pady=8)

btn_div = tk.Button(botoes_frame, text='Divisão', bg='#ff9800', fg='white', command=lambda: calcular('divisão'), **estilo_botao)
btn_div.grid(row=1, column=1, padx=8, pady=8)

# Resultado
resultado_label = tk.Label(
    frame,
    text='Resultado: ',
    font=('Arial', 18, 'bold'),
    bg='#2a2a40',
    fg='#ffffff'
)
resultado_label.pack(pady=20)

# Botão extra
btn_online = tk.Button(
    janela,
    text='Calculadora Online',
    command=abrir_calculadora_online,
    font=('Arial', 12, 'bold'),
    bg='#9c27b0',
    fg='white',
    bd=0,
    cursor='hand2',
    padx=20,
    pady=10
)
btn_online.pack(pady=15)

janela.mainloop()