import pygame
import random
from funcoes import limparTela
pygame.init()
tamanho = (880,521)
clock = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho )
icone = pygame.image.load("assets/icone.ico")
pygame.display.set_icon(icone)
pygame.display.set_caption("Corrida Maluca")
branco = (255,255,255)
preta = (0,0,0)
fundo = pygame.image.load("assets/fundo.png")
carro1 = pygame.image.load("assets/carro1.png")
carro2 = pygame.image.load("assets/carro2.png")
carro3 = pygame.image.load("assets/carro3.png")
telaDeVitoria = pygame.image.load("assets/papapa.png")

movXCar1 = 0
movXCar2 = 0
movXcar3 = 0
posYCar1 = 25
posYCar2 = 170
posYcar3 = 90

vitoria = pygame.mixer.Sound("assets/vitoria.mp3")
vitoria.set_volume(0.5)
pygame.mixer.music.load("assets/trilha.mp3")
pygame.mixer.music.play(-1) #-1 looping, 1,2 3 vezes
acabou = False
somDaVitoria = False
while True:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            quit()
   
    tela.fill( branco )
    tela.blit(fundo, (0,0))
    tela.blit(carro1, (movXCar1,posYCar1))
    tela.blit(carro2, (movXCar2,posYCar2))
    tela.blit(carro3, (movXcar3, posYcar3))
    
    if not acabou :
        movXCar1 = movXCar1 + random.randint(0,10)
        movXCar2 = movXCar2 + random.randint(0,10)
        movXcar3 = movXcar3 + random.randint (0,10)
    else:
        pygame.mixer.music.stop()
        if somDaVitoria == False:
            pygame.mixer.Sound.play(vitoria)
            somDaVitoria = True
        
    
    if movXCar1 > 880:
        movXCar1 = 0
        posYCar1 = 290
        
    if movXCar2 > 880:
        movXCar2 = 0
        posYCar2 = 430
    
    if movXcar3 > 880:
        movXcar3 = 0
        posYcar3 = 355
    
    fonte = pygame.font.Font("freesansbold.ttf",60)
    textoVermelho = fonte.render("Vermelho Ganhou!", True, branco)
    textoAmarelo = fonte.render("Amarelo Ganhou!", True, branco)
    textoAzul = fonte.render("Azul Ganhou!", True, branco)
    
    if posYCar1 == 290 and movXCar1 >= 800 and movXCar1 > movXCar2:
        tela.blit(telaDeVitoria, (0,0))
        acabou = True
        
    elif posYCar2 == 430 and movXCar2 >= 800 and movXCar2 > movXCar1:
        tela.blit(telaDeVitoria, (0,0))
        acabou = True
        
    elif posYcar3 == 355 and movXcar3 >= 800 and movXcar3 > movXCar1 and movXcar3 > movXCar2:
        tela.blit(telaDeVitoria, (0,0))
        acabou = True
        


        
        
    
    pygame.display.update()
    clock.tick(60)
pygame.quit()
    

