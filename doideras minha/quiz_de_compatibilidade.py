# Base do Quiz de Compatibilidade

def iniciar_quiz():
    print("--- Calculadora de Match ---")
    score = 0

    # Pergunta 1: Interesses em comum
    resp1 = input("Vocês têm hobbies parecidos? (s/n): ").lower()
    if resp1 == 's':
        score += 25

    # Pergunta 2: Conversa
    resp2 = input("O papo flui naturalmente por horas? (s/n): ").lower()
    if resp2 == 's':
        score += 25

    # Pergunta 3: Iniciativa (Exemplo de escala 1 a 10)
    resp3 = int(input("De 1 a 10, quanto a pessoa demonstra interesse? "))
    score += (resp3 * 5) # Se for 10, ganha 50 pontos

    # Resultado Final
    print("\n--- Resultado ---")
    if score >= 80:
        print(f"Pontuação: {score}. As chances são altíssimas! Vai fundo.")
    elif score >= 50:
        print(f"Pontuação: {score}. Tem potencial, mas precisa de um empurrãozinho.")
    else:
        print(f"Pontuação: {score}. Talvez seja melhor focar na amizade por enquanto.")

# Executar o projeto
iniciar_quiz()