import customtkinter as ctk
import random
import time
from tkinter import messagebox

# Configuração de Aparência do Terminal da Polícia
ctk.set_appearance_mode("Dark")

class MiamiMetroTerminal(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # --- Configuração de Tela Cheia ---
        self.title("MIAMI METRO POLICE DEPT - HOMICIDE DIVISION")
        self.attributes("-fullscreen", True)
        self.configure(fg_color="#08080a")
        
        # Variáveis de controle do jogo
        self.casos_resolvidos = 0
        self.casos_totais_necessarios = 4  # Agora precisa resolver 4 casos para vencer!
        self.tentativas_doakes = 3
        
        # Iniciar o fluxo chamando a primeira tela
        self.mostrar_tela_autenticacao()

    def limpar_tela(self):
        for widget in self.winfo_children():
            widget.destroy()
            
        # Botão global obrigatório para conseguir fechar a tela cheia
        btn_sair = ctk.CTkButton(
            self, text="❌ FECHAR TERMINAL", font=("Courier", 11, "bold"),
            fg_color="#111", border_width=1, border_color="#333", text_color="#666",
            hover_color="#8b0000", width=160, height=30, command=self.destroy
        )
        btn_sair.place(relx=0.99, rely=0.01, anchor="ne")

    # --- TELA 1: LOGIN DO TERMINAL FORENSE ---
    def mostrar_tela_autenticacao(self):
        self.limpar_tela()
        
        container = ctk.CTkFrame(self, fg_color="transparent")
        container.place(relx=0.5, rely=0.5, anchor="center")
        
        lbl_badge = ctk.CTkLabel(container, text="D. MORGAN", font=("Courier", 16, "bold"), text_color="#555")
        lbl_badge.pack()
        
        lbl_titulo = ctk.CTkLabel(container, text="FORENSIC ANALYSIS SYSTEM", font=("Impact", 42), text_color="#8b0000")
        lbl_titulo.pack(pady=10)
        
        lbl_sub = ctk.CTkLabel(container, text="SISTEMA DE MAPEAMENTO DE INFRAÇÕES — MIAMI, FL", font=("Courier", 13), text_color="#666")
        lbl_sub.pack(pady=5)
        
        self.entry_user = ctk.CTkEntry(container, width=300, height=40, placeholder_text="ID DO SARGENTO/ANALISTA", font=("Courier", 12), fg_color="#000", border_color="#333")
        self.entry_user.insert(0, "DEXTER_M")
        self.entry_user.pack(pady=15)
        
        btn_conectar = ctk.CTkButton(
            container, text="INICIALIZAR MONITORAMENTO", font=("Courier", 14, "bold"),
            fg_color="#8b0000", hover_color="#5a0000", width=300, height=45,
            command=self.mostrar_painel_principal
        )
        btn_conectar.pack(pady=10)

    # --- TELA 2: PAINEL DE CASOS DA DELEGACIA (O HUB PRINCIPAL) ---
    def mostrar_painel_principal(self):
        self.limpar_tela()
        
        # Painel Superior de Status
        status_frame = ctk.CTkFrame(self, fg_color="#0f0f12", height=60, border_width=1, border_color="#222")
        status_frame.pack(fill="x", padx=40, pady=20)
        status_frame.pack_propagate(False)
        
        lbl_status = ctk.CTkLabel(
            status_frame, 
            text=f"📊 PROGRESSO: {self.casos_resolvidos}/{self.casos_totais_necessarios} CASOS CONCLUÍDOS   |   🚨 SUSPEITA DO SARGENTO DOAKES: {4 - self.tentativas_doakes}/3",
            font=("Courier", 14, "bold"), text_color="#aaa"
        )
        lbl_status.pack(side="left", padx=20, expand=True)

        # Container Central dos Minigames Visuais
        self.main_work_area = ctk.CTkFrame(self, fg_color="#0d0d10", border_width=2, border_color="#8b0000")
        self.main_work_area.pack(padx=40, pady=10, fill="both", expand=True)
        
        if self.casos_resolvidos >= self.casos_totais_necessarios:
            self.mostrar_vitoria_total()
            return

        ctk.CTkLabel(self.main_work_area, text="⚠️ ARQUIVOS DE INVESTIGAÇÃO EM ABERTO", font=("Courier", 20, "bold"), text_color="#ef4444").pack(pady=20)
        
        grid_buttons = ctk.CTkFrame(self.main_work_area, fg_color="transparent")
        grid_buttons.pack(pady=5)

        # Caso 1: Análise Forense de Borrifos (Mecânica de Reflexo)
        btn_caso1 = ctk.CTkButton(
            grid_buttons, text="🔬 ANALISAR BORRIFOS DE SANGUE\n(Teste de Balística/Ângulo)", 
            font=("Courier", 12, "bold"), width=360, height=75, fg_color="#18181b", 
            border_width=1, border_color="#ff3333", command=self.carregar_minigame_borrifos
        )
        btn_caso1.grid(row=0, column=0, padx=20, pady=10)

        # Caso 2: Bloqueio do Scanner de Câmeras (Mecânica de Cliques e Tempo)
        btn_caso2 = ctk.CTkButton(
            grid_buttons, text="📹 DELETAR GRAVAÇÕES DO PORTO\n(Limpeza de Evidências)", 
            font=("Courier", 12, "bold"), width=360, height=75, fg_color="#18181b", 
            border_width=1, border_color="#ff3333", command=self.carregar_minigame_cameras
        )
        btn_caso2.grid(row=0, column=1, padx=20, pady=10)

        # Caso 3: Dosagem do Sedativo M99 (Mecânica de Equilíbrio Estático)
        btn_caso3 = ctk.CTkButton(
            grid_buttons, text="🧪 PREPARAR DOSAGEM DE M99\n(Estabilização de Seringa)", 
            font=("Courier", 12, "bold"), width=360, height=75, fg_color="#18181b", 
            border_width=1, border_color="#ff3333", command=self.carregar_minigame_m99
        )
        btn_caso3.grid(row=1, column=0, padx=20, pady=10)

        # Caso 4: Padrão do Assassino do Caminhão de Gelo (Mecânica de Memória/Decodificação)
        btn_caso4 = ctk.CTkButton(
            grid_buttons, text="❄️ CODEX ICE TRUCK KILLER\n(Decodificação de Sequência)", 
            font=("Courier", 12, "bold"), width=360, height=75, fg_color="#18181b", 
            border_width=1, border_color="#ff3333", command=self.carregar_minigame_icetruck
        )
        btn_caso4.grid(row=1, column=1, padx=20, pady=10)

        # Caso 5: GPS do Barco Slice of Life (Mecânica de Coordenadas em Tempo Real)
        btn_caso5 = ctk.CTkButton(
            grid_buttons, text="📍 CALIBRAR GPS DO SLICE OF LIFE\n(Navegação na Gulf Stream)", 
            font=("Courier", 12, "bold"), width=360, height=75, fg_color="#18181b", 
            border_width=1, border_color="#ff3333", command=self.carregar_minigame_gps
        )
        btn_caso5.grid(row=2, column=0, padx=20, pady=10)

        # Caso 6: Batimentos no Polígrafo (Mecânica de Blefe Sob Pressão)
        btn_caso6 = ctk.CTkButton(
            grid_buttons, text="🫀 SUPRESSÃO BIOMÉTRICA DO INTERROGATÓRIO\n(Manipulação do Polígrafo)", 
            font=("Courier", 12, "bold"), width=360, height=75, fg_color="#18181b", 
            border_width=1, border_color="#ff3333", command=self.carregar_minigame_poligrafo
        )
        btn_caso6.grid(row=2, column=1, padx=20, pady=10)

    # --- MINIGAME 1: REFLEXO DA BALÍSTICA DE SANGUE ---
    def carregar_minigame_borrifos(self):
        self.limpar_tela()
        self.game_frame = ctk.CTkFrame(self, fg_color="#0a0a0c", border_width=2, border_color="#ff3333", width=650, height=450)
        self.game_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        self.angulo_alvo = random.randint(30, 80)
        ctk.CTkLabel(self.game_frame, text="📐 CALIBRADOR DE IMPACTO STRINGING", font=("Courier", 18, "bold"), text_color="#ff3333").pack(pady=20)
        ctk.CTkLabel(self.game_frame, text=f"Alinhe os fios de projeção exatamente em: {self.angulo_alvo}°", font=("Courier", 14), text_color="#fff").pack(pady=5)
        
        self.barra_projeção = ctk.CTkProgressBar(self.game_frame, width=500, height=30, progress_color="#8b0000", fg_color="#222")
        self.barra_projeção.pack(pady=40)
        
        self.btn_travar = ctk.CTkButton(self.game_frame, text="🔒 FIXAR TRAJETÓRIA (ESPAÇO)", font=("Courier", 13, "bold"), fg_color="#ff3333", text_color="#000", height=45, command=self.analisar_resultado_borrifos)
        self.btn_travar.pack(pady=30)

        self.barra_pos = 0.0
        self.barra_vel = 0.03
        self.bind("<space>", lambda event: self.analisar_resultado_borrifos())
        self.loop_animacao_borrifos()

    def loop_animacao_borrifos(self):
        if not hasattr(self, 'barra_pos'): return
        self.barra_pos += self.barra_vel
        if self.barra_pos >= 1.0 or self.barra_pos <= 0.0:
            self.barra_vel = -self.barra_vel
        self.barra_projeção.set(self.barra_pos)
        self.after(25, self.loop_animacao_borrifos)

    def analisar_resultado_borrifos(self):
        self.unbind("<space>")
        angulo_calculado = int(self.barra_projeção.get() * 90)
        if abs(angulo_calculado - self.angulo_alvo) <= 4:
            messagebox.showinfo("CONCLUÍDO", f"Excelente. Ângulo calculado: {angulo_calculado}°. Amostra arquivada.")
            self.casos_resolvidos += 1
        else:
            messagebox.showerror("FALHA FORENSE", f"Margem de erro alta ({angulo_calculado}°). Doakes desconfiou.")
            self.tentativas_doakes -= 1
        self.checar_estado_do_jogo()

    # --- MINIGAME 2: APAGAR AS CÂMERAS SOB PRESSÃO ---
    def carregar_minigame_cameras(self):
        self.limpar_tela()
        self.cam_frame = ctk.CTkFrame(self, fg_color="#0a0a0c", border_width=2, border_color="#ff3333", width=650, height=450)
        self.cam_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        self.cliques_necessarios = 25
        self.tempo_limite = 6.0
        self.tempo_inicial = time.time()
        
        ctk.CTkLabel(self.cam_frame, text="📹 ACESSO AO MAINFRAME DA MARINA", font=("Courier", 18, "bold"), text_color="#ff3333").pack(pady=20)
        self.lbl_cronometro = ctk.CTkLabel(self.cam_frame, text="Tempo restante: 6.0s", font=("Courier", 14, "bold"), text_color="#ffcc00")
        self.lbl_cronometro.pack()
        self.lbl_contador = ctk.CTkLabel(self.cam_frame, text=f"Setores para purgar: {self.cliques_necessarios}", font=("Courier", 14))
        self.lbl_contador.pack(pady=10)
        
        self.btn_clicker = ctk.CTkButton(self.cam_frame, text="⚠️ EXPURGAR SETOR", font=("Courier", 14, "bold"), fg_color="#222", border_width=1, border_color="#ff3333", height=60, command=self.registrar_clique_camera)
        self.btn_clicker.pack(pady=40, padx=50, fill="x")
        self.loop_relogio_cameras()

    def loop_relogio_cameras(self):
        if self.cliques_necessarios <= 0: return
        passado = time.time() - self.tempo_inicial
        restante = self.tempo_limite - passado
        if restante <= 0:
            messagebox.showerror("LOG BLOQUEADO", "O sargento Doakes confiscou os HDs antes de você apagar.")
            self.tentativas_doakes -= 1
            self.checar_estado_do_jogo()
        else:
            self.lbl_cronometro.configure(text=f"Tempo restante: {restante:.1f}s")
            self.after(100, self.loop_relogio_cameras)

    def registrar_clique_camera(self):
        if self.cliques_necessarios > 0:
            self.cliques_necessarios -= 1
            self.lbl_contador.configure(text=f"Setores para purgar: {self.cliques_necessarios}")
        if self.cliques_necessarios <= 0:
            messagebox.showinfo("LOGS DESTRUÍDOS", "Vídeos deletados com sucesso.")
            self.casos_resolvidos += 1
            self.checar_estado_do_jogo()

    # --- MINIGAME 3: DOSAGEM DE SEDATIVO M99 (SLIDER EQUILÍBRIO) ---
    def carregar_minigame_m99(self):
        self.limpar_tela()
        self.m99_frame = ctk.CTkFrame(self, fg_color="#0a0a0c", border_width=2, border_color="#ff3333", width=650, height=450)
        self.m99_frame.place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(self.m99_frame, text="🧪 DOSAGEM QUÍMICA DE ETORFINA", font=("Courier", 18, "bold"), text_color="#ff3333").pack(pady=20)
        ctk.CTkLabel(self.m99_frame, text="Ajuste o dosador para conter exatamente 78% de potência.\nMenos deixará o alvo acordado, mais parará seu coração precocemente.", font=("Courier", 12), text_color="#aaa", wraplength=500).pack(pady=5)

        self.slider_m99 = ctk.CTkSlider(self.m99_frame, from_=0, to=100, number_of_steps=100, button_color="#ff3333", progress_color="#8b0000", width=450)
        self.slider_m99.set(20)
        self.slider_m99.pack(pady=35)

        self.lbl_m99_status = ctk.CTkLabel(self.m99_frame, text="Dosagem Atual: 20%", font=("Courier", 14), text_color="#ffcc00")
        self.lbl_m99_status.pack()
        self.slider_m99.configure(command=lambda v: self.lbl_m99_status.configure(text=f"Dosagem Atual: {int(float(v))}%"))

        ctk.CTkButton(self.m99_frame, text="🧪 CARREGAR SERINGA", font=("Courier", 13, "bold"), fg_color="#111", border_width=1, border_color="#ff3333", command=self.validar_m99).pack(pady=35)

    def validar_m99(self):
        dosagem = int(self.slider_m99.get())
        if 75 <= dosagem <= 81:
            messagebox.showinfo("SUCESSO", f"Dosagem perfeita em {dosagem}%. O passageiro sombrio age em silêncio.")
            self.casos_resolvidos += 1
        else:
            messagebox.showerror("ERRO QUÍMICO", f"Dosagem instável de {dosagem}%. Alvo gerou complicações médicas na mesa.")
            self.tentativas_doakes -= 1
        self.checar_estado_do_jogo()

    # --- MINIGAME 4: DECODIFICAR SEQUÊNCIA DO ICE TRUCK KILLER ---
    def carregar_minigame_icetruck(self):
        self.limpar_tela()
        self.ice_frame = ctk.CTkFrame(self, fg_color="#0a0a0c", border_width=2, border_color="#ff3333", width=650, height=450)
        self.ice_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Gerar uma chave criptográfica aleatória de letras
        self.letras_chave = [random.choice(["B", "R", "I", "A", "N"]) for _ in range(5)]
        self.codigo_secreto = "".join(self.letras_chave)

        ctk.CTkLabel(self.ice_frame, text="❄️ RECONHECIMENTO DE PADRÕES DO ASSASSINO", font=("Courier", 18, "bold"), text_color="#ff3333").pack(pady=20)
        ctk.CTkLabel(self.ice_frame, text=f"Grave e digite o padrão de resposta deixado na lâmina:\n\n{'-'.join(self.letras_chave)}", font=("Courier", 16, "bold"), text_color="#00ffcc").pack(pady=15)

        self.entry_ice = ctk.CTkEntry(self.ice_frame, placeholder_text="Digite o código decodificado", font=("Courier", 13), width=250, fg_color="#000", border_color="#333")
        self.entry_ice.pack(pady=20)

        ctk.CTkButton(self.ice_frame, text="🧬 ENVIAR RECONHECIMENTO", font=("Courier", 13, "bold"), fg_color="#111", border_width=1, border_color="#ff3333", command=self.validar_icetruck).pack(pady=25)

    def validar_icetruck(self):
        if self.entry_ice.get().upper() == self.codigo_secreto:
            messagebox.showinfo("DECODIFICADO", "Você compreendeu a mensagem subliminar do Ice Truck Killer.")
            self.casos_resolvidos += 1
        else:
            messagebox.showerror("FALHA", "Pista perdida. A Miami Metro está seguindo o rastro errado.")
            self.tentativas_doakes -= 1
        self.checar_estado_do_jogo()

    # --- MINIGAME 5: PILOTO AUTOMÁTICO DO GPS (MECÂNICA DE COORDENADA RÁPIDA) ---
    def carregar_minigame_gps(self):
        self.limpar_tela()
        self.gps_frame = ctk.CTkFrame(self, fg_color="#0a0a0c", border_width=2, border_color="#ff3333", width=650, height=450)
        self.gps_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.coordenada_alvo = random.randint(15, 85)

        ctk.CTkLabel(self.gps_frame, text="📍 NAVEGAÇÃO MARÍTIMA FORENSE", font=("Courier", 18, "bold"), text_color="#ff3333").pack(pady=20)
        ctk.CTkLabel(self.gps_frame, text=f"Defina as coordenadas da corrente Gulf Stream em: {self.coordenada_alvo}°", font=("Courier", 14), text_color="#fff").pack(pady=10)

        self.slider_gps = ctk.CTkSlider(self.gps_frame, from_=0, to=100, button_color="#ff3333", progress_color="#8b0000", width=450)
        self.slider_gps.set(0)
        self.slider_gps.pack(pady=25)

        self.lbl_gps_status = ctk.CTkLabel(self.gps_frame, text="GPS: 0° N", font=("Courier", 14), text_color="#00ffcc")
        self.lbl_gps_status.pack()
        self.slider_gps.configure(command=lambda v: self.lbl_gps_status.configure(text=f"GPS: {int(float(v))}° N"))

        ctk.CTkButton(self.gps_frame, text="🚢 LANÇAR TRAJETÓRIA", font=("Courier", 13, "bold"), fg_color="#111", border_width=1, border_color="#ff3333", command=self.validar_gps).pack(pady=30)

    def validar_gps(self):
        posicao = int(self.slider_gps.get())
        if abs(posicao - self.coordenada_alvo) <= 2:
            messagebox.showinfo("ROTA DEFINIDA", "Vetor perfeitamente alinhado. Os despejos irão afundar no oceano profundo.")
            self.casos_resolvidos += 1
        else:
            messagebox.showerror("ALERTA DE GPS", f"Erro crítico. A rota {posicao}° é muito próxima à praia. Evidências iriam boiar!")
            self.tentativas_doakes -= 1
        self.checar_estado_do_jogo()

    # --- MINIGAME 6: SUPRESSÃO BIOMÉTRICA (INTERROGATÓRIO MULTIESCOLA) ---
    def carregar_minigame_poligrafo(self):
        self.limpar_tela()
        self.pol_frame = ctk.CTkFrame(self, fg_color="#0a0a0c", border_width=2, border_color="#ff3333", width=650, height=450)
        self.pol_frame.place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(self.pol_frame, text="🫀 CONTROLE DE FREQUÊNCIA DO POLÍGRAFO", font=("Courier", 18, "bold"), text_color="#ff3333").pack(pady=20)
        ctk.CTkLabel(self.pol_frame, text="LaGuerta está te questionando diretamente sobre as lâminas extras encontradas. Escolha a resposta psicológica que amortece seus batimentos cardíacos:", font=("Courier", 13), text_color="#aaa", wraplength=500).pack(pady=10)

        # Botões de escolha estratégica
        ctk.CTkButton(self.pol_frame, text="Opção A: Mentir agressivamente e atacar Doakes", font=("Courier", 12), fg_color="#1c1c1e", border_width=1, border_color="#333", height=45, command=self.falhar_poligrafo).pack(pady=10, padx=50, fill="x")
        ctk.CTkButton(self.pol_frame, text="Opção B: Contar uma meia-verdade calma sobre perícia", font=("Courier", 12), fg_color="#1c1c1e", border_width=1, border_color="#ff3333", text_color="#ff3333", height=45, command=self.sucesso_poligrafo).pack(pady=10, padx=50, fill="x")
        ctk.CTkButton(self.pol_frame, text="Opção C: Entrar em pânico e pedir proteção jurídica", font=("Courier", 12), fg_color="#1c1c1e", border_width=1, border_color="#333", height=45, command=self.falhar_poligrafo).pack(pady=10, padx=50, fill="x")

    def sucesso_poligrafo(self):
        messagebox.showinfo("POLÍGRAFO ESTÁVEL", "Seus batimentos cardíacos permaneceram em 62 BPM. Os investigadores morderam a isca.")
        self.casos_resolvidos += 1
        self.checar_estado_do_jogo()

    def falhar_poligrafo(self):
        messagebox.showerror("PICO CARDÍACO", "Gráfico disparou para 135 BPM! O sensor de mentiras apitou e as suspeitas aumentaram.")
        self.tentativas_doakes -= 1
        self.checar_estado_do_jogo()

    # --- GERENCIAMENTO DE FLUXO E FIM DE JOGO ---
    def checar_estado_do_jogo(self):
        if self.tentativas_doakes <= 0:
            messagebox.showerror("SESSÃO SUSPENSA", "Sgt. Doakes reuniu provas contra você.\n\n'Surprise, motherf***er!' — Você foi desmascarado.")
            self.destroy()
        else:
            self.mostrar_painel_principal()

    def mostrar_vitoria_total(self):
        self.limpar_tela()
        container = ctk.CTkFrame(self, fg_color="#0a0a0c", border_width=2, border_color="#00ffcc", width=600, height=350)
        container.place(relx=0.5, rely=0.5, anchor="center")
        
        ctk.CTkLabel(container, text="SESSÃO LIMPA", font=("Impact", 36), text_color="#00ffcc").pack(pady=25)
        ctk.CTkLabel(container, text="Todos os casos foram manipulados e encerrados com sucesso.\nNenhum rastro forense restou nos sistemas da polícia de Miami.", font=("Courier", 13), text_color="#aaa", wraplength=450).pack(pady=10)
        
        ctk.CTkButton(container, text="FECHAR E SAIR", fg_color="#111", border_width=1, border_color="#00ffcc", command=self.destroy).pack(pady=35)


# --- EXECUTOR DO SISTEMA ---
if __name__ == "__main__":
    app = MiamiMetroTerminal()
    app.mainloop()