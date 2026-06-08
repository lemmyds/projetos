import tkinter as tk
import json
import os

# --- CORES E CONFIGURAÇÕES ---
C_FUNDO = "#020202"
C_CYAN  = "#00f0ff"
C_GOLD  = "#ffd600"
C_RED   = "#ff2d2d"
C_STAMINA = "#26e600"
C_OFF   = "#1a1a1a"
SAVE_FILE = "zelda_save.json"

class PlacarZeldaUpgradeAjustado:
    def __init__(self, root):
        self.root = root
        self.root.title("SHEIKAH SYSTEM - STAMINA FIX")
        self.root.geometry("900x780")
        self.root.configure(bg=C_FUNDO)

        self.dados = {
            "coracoes": 6,
            "vigor": 1,
            "vigor_pedacos": 0, 
            "shrines": 0,
            "orbes": 0,
            "bestas": [False] * 4
        }
        
        self.carregar_jogo()
        self.setup_ui()
        self.render_loop()
        self.root.protocol("WM_DELETE_WINDOW", self.salvar_e_sair)

    def setup_ui(self):
        self.canvas = tk.Canvas(self.root, width=850, height=650, bg=C_FUNDO, highlightthickness=0)
        self.canvas.pack(pady=20)
        
        self.canvas.bind("<Button-1>", lambda e: self.interagir(e, "soma"))
        self.canvas.bind("<Button-3>", lambda e: self.interagir(e, "subtrai"))
        
        for key in ["<q>", "<Q>", "<e>", "<E>"]:
            self.root.bind(key, self.atalhos_teclado)

    def carregar_jogo(self):
        if os.path.exists(SAVE_FILE):
            try:
                with open(SAVE_FILE, "r") as f:
                    self.dados.update(json.load(f))
            except: pass

    def salvar_e_sair(self):
        with open(SAVE_FILE, "w") as f:
            json.dump(self.dados, f)
        self.root.destroy()

    def aumentar_vigor_unidade(self):
        """Aumenta o vigor em apenas 1/5 por vez"""
        self.dados["vigor_pedacos"] += 1
        if self.dados["vigor_pedacos"] > 5:
            if self.dados["vigor"] < 3:
                self.dados["vigor"] += 1
                self.dados["vigor_pedacos"] = 1
            else:
                self.dados["vigor_pedacos"] = 5

    def atalhos_teclado(self, event):
        key = event.keysym.lower()
        if key == 'e':
            for _ in range(10):
                if self.dados["shrines"] < 136:
                    self.dados["shrines"] += 1
                    self.dados["orbes"] += 1
        
        # Q e E continuam servindo para completar a rodela manualmente se desejar
        self.dados["vigor_pedacos"] = 5

    def interagir(self, event, op):
        x, y = event.x, event.y
        m = 1 if op == "soma" else -1

        # Shrines
        if 300 <= x <= 550 and 240 <= y <= 480:
            if op == "soma":
                if self.dados["shrines"] < 136:
                    self.dados["shrines"] += 1
                    self.dados["orbes"] += 1
            else:
                self.dados["shrines"] = max(0, self.dados["shrines"] - 1)

        # Orbes (Clique para Orar)
        elif 350 <= x <= 550 and 30 <= y <= 110:
            if op == "soma":
                if self.dados["orbes"] >= 4:
                    self.perguntar_recompensa()
                else:
                    self.dados["orbes"] += 1
            else:
                self.dados["orbes"] = max(0, self.dados["orbes"] - 1)

        # Vigor (Cliques manuais nas rodelas)
        elif 350 <= x <= 550 and 130 <= y <= 210:
            if op == "soma":
                self.aumentar_vigor_unidade()
            else:
                self.dados["vigor_pedacos"] -= 1
                if self.dados["vigor_pedacos"] < 0 and self.dados["vigor"] > 1:
                    self.dados["vigor"] -= 1
                    self.dados["vigor_pedacos"] = 5
                elif self.dados["vigor_pedacos"] < 0: self.dados["vigor_pedacos"] = 0

        # Corações
        elif 50 <= x <= 350 and 30 <= y <= 150:
            self.dados["coracoes"] = max(3, min(30, self.dados["coracoes"] + m))

        # Bestas
        elif 600 <= x <= 850 and 30 <= y <= 150:
            idx = (x - 610) // 55
            if 0 <= idx < 4: self.dados["bestas"][idx] = (op == "soma")

    def perguntar_recompensa(self):
        win = tk.Toplevel(self.root)
        win.title("ESTÁTUA DA DEUSA")
        win.geometry("300x150")
        win.configure(bg="#111")
        win.attributes("-topmost", True)
        
        tk.Label(win, text="ORAR PELO UPGRADE?\n(-4 ORBES)", fg=C_GOLD, bg="#111", font=("Impact", 12)).pack(pady=10)

        def upgrade(tipo):
            self.dados["orbes"] -= 4
            if tipo == "H": 
                self.dados["coracoes"] += 1
            else: 
                # Agora o upgrade da estátua só dá +1 unidade (1/5)
                self.aumentar_vigor_unidade()
            win.destroy()

        tk.Button(win, text="VIDA", command=lambda: upgrade("H"), bg=C_RED, fg="white", width=10).pack(side="left", padx=20)
        tk.Button(win, text="VIGOR", command=lambda: upgrade("V"), bg=C_STAMINA, fg="black", width=10).pack(side="right", padx=20)

    def render_loop(self):
        c = self.canvas
        c.delete("all")

        # Render Orbes
        c.create_text(450, 30, text="SPIRIT ORBS", fill=C_GOLD, font=("Impact", 14))
        c.create_oval(435, 50, 465, 80, fill=C_GOLD if self.dados["orbes"] >= 4 else C_OFF, outline=C_CYAN)
        c.create_text(450, 65, text=str(self.dados["orbes"]), fill="black" if self.dados["orbes"] >= 4 else "white", font=("Arial", 12, "bold"))

        # Render Vida
        c.create_text(50, 30, text="VITALITY", fill=C_RED, font=("Impact", 18), anchor="w")
        for i in range(self.dados["coracoes"]):
            row, col = divmod(i, 10)
            c.create_text(55 + col*30, 70 + row*35, text="❤", fill=C_RED, font=("Arial", 22))

        # Render Vigor
        c.create_text(450, 130, text="STAMINA", fill=C_STAMINA, font=("Impact", 14))
        for i in range(1, 4):
            x_pos = 385 + (i-1)*55
            color = C_STAMINA if i <= self.dados["vigor"] else C_OFF
            c.create_oval(x_pos, 150, x_pos+40, 190, outline=color, width=3)
            if i == self.dados["vigor"]:
                c.create_text(x_pos+20, 170, text=f"{self.dados['vigor_pedacos']}/5", fill=C_STAMINA, font=("Arial", 9, "bold"))

        # Bestas e Placar
        icons = ["🦅", "🦎", "🐘", "🐪"]
        for i, icon in enumerate(icons):
            color = C_CYAN if self.dados["bestas"][i] else C_OFF
            c.create_text(630+(i*55), 80, text=icon, fill=color, font=("Arial", 28))

        c.create_rectangle(300, 240, 550, 470, outline=C_CYAN, width=4)
        c.create_text(425, 365, text=f"{self.dados['shrines']:03}", fill=C_GOLD, font=("Consolas", 85, "bold"))

        self.root.after(100, self.render_loop)

if __name__ == "__main__":
    root = tk.Tk()
    app = PlacarZeldaUpgradeAjustado(root)
    root.mainloop()