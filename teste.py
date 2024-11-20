import pygame
import random

pygame.init()

# Configurações básicas
tamanho = (880, 521)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
icone = pygame.image.load("assets/icone.ico")
pygame.display.set_icon(icone)
pygame.display.set_caption("Corrida Maluca")
branco = (255, 255, 255)
preto = (0, 0, 0)
fundo = pygame.image.load("assets/fundo.png")
carro1 = pygame.image.load("assets/carro1.png")
carro2 = pygame.image.load("assets/carro2.png")
carro3 = pygame.image.load("assets/carro3.png")
fonte = pygame.font.Font("freesansbold.ttf", 30)

# Posições iniciais
movXCar1 = 0
movXCar2 = 0
movXCar3 = 0
posYCar1 = 25
posYCar2 = 170
posYCar3 = 90

# Sons
vitoria = pygame.mixer.Sound("assets/vitoria.mp3")
vitoria.set_volume(0.5)
pygame.mixer.music.load("assets/trilha.mp3")
pygame.mixer.music.play(-1)

acabou = False

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()

    # Atualização da tela
    tela.fill(branco)
    tela.blit(fundo, (0, 0))
    tela.blit(carro1, (movXCar1, posYCar1))
    tela.blit(carro2, (movXCar2, posYCar2))
    tela.blit(carro3, (movXCar3, posYCar3))

    # Atualização das posições
    if not acabou:
        movXCar1 += random.randint(0, 10)
        movXCar2 += random.randint(0, 10)
        movXCar3 += random.randint(0, 10)

    # Determinar posições manualmente
    if movXCar1 > movXCar2 and movXCar1 > movXCar3:
        vencedor = "Carro Vermelho"
        if movXCar2 > movXCar3:
            segundo = "Carro Amarelo"
            terceiro = "Carro Azul"
            dist_vencedor_segundo = movXCar1 - movXCar2
            dist_segundo_terceiro = movXCar2 - movXCar3
        else:
            segundo = "Carro Azul"
            terceiro = "Carro Amarelo"
            dist_vencedor_segundo = movXCar1 - movXCar3
            dist_segundo_terceiro = movXCar3 - movXCar2
    elif movXCar2 > movXCar1 and movXCar2 > movXCar3:
        vencedor = "Carro Amarelo"
        if movXCar1 > movXCar3:
            segundo = "Carro Vermelho"
            terceiro = "Carro Azul"
            dist_vencedor_segundo = movXCar2 - movXCar1
            dist_segundo_terceiro = movXCar1 - movXCar3
        else:
            segundo = "Carro Azul"
            terceiro = "Carro Vermelho"
            dist_vencedor_segundo = movXCar2 - movXCar3
            dist_segundo_terceiro = movXCar3 - movXCar1
    else:
        vencedor = "Carro Azul"
        if movXCar1 > movXCar2:
            segundo = "Carro Vermelho"
            terceiro = "Carro Amarelo"
            dist_vencedor_segundo = movXCar3 - movXCar1
            dist_segundo_terceiro = movXCar1 - movXCar2
        else:
            segundo = "Carro Amarelo"
            terceiro = "Carro Vermelho"
            dist_vencedor_segundo = movXCar3 - movXCar2
            dist_segundo_terceiro = movXCar2 - movXCar1

    # Exibir informações
    texto_vencedor = fonte.render(f"Vencedor: {vencedor}", True, preto)
    texto_dist_vencedor_segundo = fonte.render(f"Distância 1º - 2º: {dist_vencedor_segundo}", True, preto)
    texto_dist_segundo_terceiro = fonte.render(f"Distância 2º - 3º: {dist_segundo_terceiro}", True, preto)

    tela.blit(texto_vencedor, (10, 10))
    tela.blit(texto_dist_vencedor_segundo, (10, 50))
    tela.blit(texto_dist_segundo_terceiro, (10, 90))

    # Atualizar tela
    pygame.display.update()
    clock.tick(60)
