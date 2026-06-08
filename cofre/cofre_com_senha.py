import maskpass
import json
import os
import random
import string
import shutil
import time

# --- CONFIGURAÇÕES ---
TOTAL_ARQUIVOS = 1000
PASTA_DADOS = "bunker_digital_insane"
ARQUIVO_INDICE = f"{PASTA_DADOS}/index_master.json"

# --- FUNÇÕES DE SISTEMA ---

def preparar_pasta():
    if os.path.exists(PASTA_DADOS):
        shutil.rmtree(PASTA_DADOS)
    os.makedirs(PASTA_DADOS)

def salvar_no_bunker(senha, itens):
    print(f"\n📦 Fragmentando em {TOTAL_ARQUIVOS} arquivos...")
    preparar_pasta()
    nomes = [f"{i}_{''.join(random.choice(string.ascii_lowercase) for _ in range(5))}.json" for i in range(TOTAL_ARQUIVOS)]
    idx_senha = random.randint(0, TOTAL_ARQUIVOS - 1)
    arq_senha = nomes[idx_senha]
    
    with open(ARQUIVO_INDICE, "w") as f:
        json.dump({"target": arq_senha, "map": nomes}, f)

    for i, nome in enumerate(nomes):
        caminho = f"{PASTA_DADOS}/{nome}"
        if nome == arq_senha:
            conteudo = {"key": senha}
        else:
            fatia = [itens[j] for j in range(len(itens)) if j % (TOTAL_ARQUIVOS - 1) == i]
            conteudo = {"fragment": fatia if fatia else "".join(random.choice(string.ascii_letters) for _ in range(10))}
        with open(caminho, "w") as f:
            json.dump(conteudo, f)
    print("✅ Bunker trancado!")

def carregar_do_bunker():
    if os.path.exists(ARQUIVO_INDICE):
        try:
            with open(ARQUIVO_INDICE, "r") as f:
                idx = json.load(f)
            with open(f"{PASTA_DADOS}/{idx['target']}", "r") as f:
                s = json.load(f)["key"]
            lista = []
            for nome in idx['map']:
                if nome != idx['target']:
                    with open(f"{PASTA_DADOS}/{nome}", "r") as f:
                        d = json.load(f).get("fragment")
                        if isinstance(d, list): lista.extend(d)
            return s, lista
        except: return None, None
    return None, None

# --- MINIGAMES ---

def minigame_marreta():
    print("\n🔨 MARRETA: 40 GOLPES EM 5 SEGUNDOS!")
    input("PRESSIONE ENTER PARA COMEÇAR!")
    inicio = time.time()
    golpes = 0
    while golpes < 40:
        input(f"GOLPE {golpes+1}/40")
        golpes += 1
        if time.time() - inicio > 5:
            print("\n⏰ LENTO DEMAIS! O segurança te ouviu.")
            return False
    print(f"💥 BUM! Abriu em {round(time.time()-inicio, 2)}s!")
    return True

def minigame_lockpick():
    print("\n🔐 LOCKPICK: 3 PINOS")
    segredo = [random.randint(1, 9) for _ in range(3)]
    tentativas = 10
    progresso = ["?", "?", "?"]
    descoberto = [False] * 3
    while tentativas > 0 and not all(descoberto):
        print(f"Status: {progresso} | Gazua: {tentativas}")
        try:
            p = int(input("Pino (1-3): ")) - 1
            c = int(input(f"Chute pino {p+1}: "))
            if c == segredo[p]:
                progresso[p], descoberto[p] = c, True
                print("⚡ CLICK!")
            else:
                print("🔼 ALTO" if c < segredo[p] else "🔽 BAIXO")
                tentativas -= 1
        except: pass
    return all(descoberto)

# --- MENU DE ITENS ---

def gerenciar_bunker():
    global itens_guardados, senha_correta
    s_atual = list(senha_correta)[0]
    while True:
        print("\n[1] Ver [2] Add [3] Remover [4] Sair")
        op = input("> ")
        if op == "1": print(f"Itens: {itens_guardados}")
        elif op == "2":
            itens_guardados.append(input("Item: "))
            salvar_no_bunker(s_atual, itens_guardados)
        elif op == "3":
            for i, item in enumerate(itens_guardados): print(f"{i}: {item}")
            try:
                itens_guardados.pop(int(input("Remover ID: ")))
                salvar_no_bunker(s_atual, itens_guardados)
            except: print("Erro.")
        elif op == "4": break

# --- O QUE FALTAVA: A CHAMADA REAL ---

def main():
    global senha_correta, itens_guardados
    print("=== INICIANDO PROTOCOLO DEXTER ===")
    
    s_salva, l_salva = carregar_do_bunker()
    if s_salva:
        senha_correta = {s_salva}
        itens_guardados = l_salva
    else:
        print("Bunker vazio!")
        s = maskpass.askpass(prompt="Senha: ", mask="*")
        itens_guardados = ["Documento X"]
        salvar_no_bunker(s, itens_guardados)
        senha_correta = {s}

    for _ in range(3):
        ent = input('\nSenha ou "INVASAO": ')
        if ent in senha_correta:
            gerenciar_bunker()
            break
        elif ent.upper() == "INVASAO":
            print("1-Marreta | 2-Lockpick")
            venceu = minigame_marreta() if input("> ") == "1" else minigame_lockpick()
            if venceu:
                gerenciar_bunker()
                break
        else:
            print("❌ Errado.")

# EXECUTA TUDO
if __name__ == "__main__":
    main()