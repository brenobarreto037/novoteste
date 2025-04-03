import pygame
import os

# Inicializando o Pygame
pygame.init()

# Configurações da tela
LARGURA_TELA = 800
ALTURA_TELA = 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Pong")

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

# Configurações das raquetes e da bola
RAQUETE_LARGURA = 15
RAQUETE_ALTURA = 100
BOLA_RAIO = 10

# Velocidade do jogo
velocidade_raquete = 15
velocidade_bola_x = 7
velocidade_bola_y = 7

# Função para desenhar as raquetes
def desenhar_raquete(x, y):
    pygame.draw.rect(tela, BRANCO, [x, y, RAQUETE_LARGURA, RAQUETE_ALTURA])

# Função para desenhar a bola
def desenhar_bola(x, y):
    pygame.draw.circle(tela, BRANCO, [x, y], BOLA_RAIO)

# Função para exibir o texto na tela
def mostrar_pontuacao(pontos_jogador1, pontos_jogador2):
    fonte = pygame.font.SysFont("arial", 30)
    texto_pontos = fonte.render(f"{pontos_jogador1} - {pontos_jogador2}", True, BRANCO)
    tela.blit(texto_pontos, [LARGURA_TELA // 2 - texto_pontos.get_width() // 2, 20])

# Função para salvar as pontuações
def salvar_pontuacao(pontos_jogador1, pontos_jogador2):
    with open("pontuacoes.txt", "a") as f:
        f.write(f"{pontos_jogador1} - {pontos_jogador2}\n")

# Função principal do jogo
def jogo():
    # Posições iniciais
    x_raquete1 = 20
    y_raquete1 = ALTURA_TELA // 2 - RAQUETE_ALTURA // 2
    x_raquete2 = LARGURA_TELA - 20 - RAQUETE_LARGURA
    y_raquete2 = ALTURA_TELA // 2 - RAQUETE_ALTURA // 2
    x_bola = LARGURA_TELA // 2
    y_bola = ALTURA_TELA // 2
    velocidade_bola_x = 7
    velocidade_bola_y = 7

    pontos_jogador1 = 0
    pontos_jogador2 = 0

    clock = pygame.time.Clock()
    executando = True

    while executando:
        # Verificando eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False

        # Movimentação das raquetes
        teclas = pygame.key.get_pressed()

        # Raquete 1 (Jogador 1)
        if teclas[pygame.K_w] and y_raquete1 > 0:
            y_raquete1 -= velocidade_raquete
        if teclas[pygame.K_s] and y_raquete1 < ALTURA_TELA - RAQUETE_ALTURA:
            y_raquete1 += velocidade_raquete

        # Raquete 2 (Jogador 2)
        if teclas[pygame.K_UP] and y_raquete2 > 0:
            y_raquete2 -= velocidade_raquete
        if teclas[pygame.K_DOWN] and y_raquete2 < ALTURA_TELA - RAQUETE_ALTURA:
            y_raquete2 += velocidade_raquete

        # Movimentação da bola
        x_bola += velocidade_bola_x
        y_bola += velocidade_bola_y

        # Colisão com o topo e a parte inferior
        if y_bola <= 0 or y_bola >= ALTURA_TELA - BOLA_RAIO:
            velocidade_bola_y *= -1

        # Colisão com as raquetes
        if (x_bola <= x_raquete1 + RAQUETE_LARGURA and y_bola >= y_raquete1 and y_bola <= y_raquete1 + RAQUETE_ALTURA) or (x_bola >= x_raquete2 - BOLA_RAIO and y_bola >= y_raquete2 and y_bola <= y_raquete2 + RAQUETE_ALTURA):
            velocidade_bola_x *= -1

        # Pontuação
        if x_bola <= 0:
            pontos_jogador2 += 1
            x_bola = LARGURA_TELA // 2
            y_bola = ALTURA_TELA // 2
            velocidade_bola_x *= -1

        if x_bola >= LARGURA_TELA:
            pontos_jogador1 += 1
            x_bola = LARGURA_TELA // 2
            y_bola = ALTURA_TELA // 2
            velocidade_bola_x *= -1

        # Desenhando elementos na tela
        tela.fill(PRETO)
        desenhar_raquete(x_raquete1, y_raquete1)
        desenhar_raquete(x_raquete2, y_raquete2)
        desenhar_bola(x_bola, y_bola)
        mostrar_pontuacao(pontos_jogador1, pontos_jogador2)

        # Atualizando a tela
        pygame.display.update()

        # Definindo a taxa de quadros
        clock.tick(60)

    # Salvar a pontuação
    salvar_pontuacao(pontos_jogador1, pontos_jogador2)

    # Finalizando o Pygame
    pygame.quit()

# Iniciando o jogo
if __name__ == "__main__":
    jogo()
