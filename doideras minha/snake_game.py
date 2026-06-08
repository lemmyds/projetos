import msvcrt
import random
import os
from collections import deque
from time import sleep

WIDTH = 60
HEIGHT = 20

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_game(snake, food, score, game_over=False):
    clear_screen()
    
    # Desenhar bordas superior
    print("+" + "-" * (WIDTH - 2) + "+")
    
    # Desenhar campo de jogo
    for y in range(1, HEIGHT):
        line = "|"
        for x in range(1, WIDTH - 1):
            if (y, x) == food:
                line += "◆"
            elif (y, x) in snake:
                if (y, x) == snake[0]:
                    line += "●"
                else:
                    line += "○"
            else:
                line += " "
        line += "|"
        print(line)
    
    # Desenhar bordas inferior
    print("+" + "-" * (WIDTH - 2) + "+")
    print(f"Score: {score} | Comandos: W/A/S/D ou Setas | Q para sair")
    
    if game_over:
        print(f"\nGAME OVER! Pontuação final: {score}")

def get_direction_input(current_direction):
    if msvcrt.kbhit():
        key = msvcrt.getch().decode('utf-8', errors='ignore').lower()
        
        if key == 'q':
            return None
        elif key == 'w' and current_direction != (1, 0):
            return (-1, 0)
        elif key == 's' and current_direction != (-1, 0):
            return (1, 0)
        elif key == 'a' and current_direction != (0, 1):
            return (0, -1)
        elif key == 'd' and current_direction != (0, -1):
            return (0, 1)
    
    return current_direction

def main():
    # Inicializar cobra no centro
    start_x = WIDTH // 2
    start_y = HEIGHT // 2
    snake = deque([(start_y, start_x), (start_y, start_x - 1), (start_y, start_x - 2)])
    
    # Direção inicial
    direction = (-1, 0)  # cima
    
    # Gerar comida
    food = (random.randint(2, HEIGHT - 2), random.randint(2, WIDTH - 3))
    
    # Pontuação
    score = 0
    
    game_over = False
    
    while not game_over:
        draw_game(snake, food, score)
        
        # Capturar input
        direction = get_direction_input(direction)
        if direction is None:
            break
        
        # Calcular nova posição da cabeça
        head_y, head_x = snake[0]
        new_head_y = head_y + direction[0]
        new_head_x = head_x + direction[1]
        
        # Verificar colisão com paredes
        if new_head_y <= 0 or new_head_y >= HEIGHT or new_head_x <= 0 or new_head_x >= WIDTH - 1:
            game_over = True
            break
        
        # Verificar colisão consigo mesma
        if (new_head_y, new_head_x) in snake:
            game_over = True
            break
        
        # Adicionar nova cabeça
        snake.appendleft((new_head_y, new_head_x))
        
        # Verificar se comeu
        if (new_head_y, new_head_x) == food:
            score += 10
            # Gerar nova comida
            food = (random.randint(2, HEIGHT - 2), random.randint(2, WIDTH - 3))
            while food in snake:
                food = (random.randint(2, HEIGHT - 2), random.randint(2, WIDTH - 3))
        else:
            # Remover cauda se não comeu
            snake.pop()
        
        sleep(0.1)  # Controlar velocidade do jogo
    
    # Game Over
    draw_game(snake, food, score, game_over=True)
    print("\nObrigado por jogar!")


if __name__ == '__main__':
    main()
    main()
