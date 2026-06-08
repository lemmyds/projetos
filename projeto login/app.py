import customtkinter as ctk

#config aparencia
ctk.set_appearance_mode("dark")
#criação das funções de funcionalidade
def validar_login():
    usuario = campo_usuario.get() 
    senha = campo_senha.get()

    #verificar se o usuario e jhonatan e a senha helmat
    if usuario == 'matheus' and senha == 'helmat':
        resultado_login.configure(text='login feito com sucesso!',
        text_color='green')
    else:
        resultado_login.configure(text='login incorreto',
        text_color='red')
#criação da janela
app = ctk.CTk()
app.title("sistema de login")
app.geometry("300x300")
#craiação dos campos
#label
label_usuario = ctk.CTkLabel(app,text="usuário")
label_usuario.pack(pady=10)
#entry
campo_usuario =ctk.CTkEntry(app,placeholder_text='Digite seu usuario')
campo_usuario.pack(pady=10)
#label
label_senha = ctk.CTkLabel(app,text="senha")
label_senha.pack(pady=10)
#entry
campo_senha =ctk.CTkEntry(app,placeholder_text='Digite seu senha',
show='*')
campo_senha.pack(pady=10)
#button
botao_login = ctk.CTkButton(app,text='login',command=validar_login)
botao_login.pack(pady=10)
#campo feedback
resultado_login = ctk.CTkLabel(app,text='')
resultado_login.pack(pady=10)

#iniciar a aplicação
app.mainloop()