import pygame
import random
from funcoes import returnVencedor, returnSegundo, returnTerceiro, placar1, placar2, placar3
pygame.init()
tamanho = (880,521)
clock = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho )
icone = pygame.image.load("assets/icone.ico")
pygame.display.set_icon(icone)
pygame.display.set_caption("Corrida Maluca")
branco = (255,255,255)
preto = (0,0,0)
fundo = pygame.image.load("assets/fundo.png")
carro1 = pygame.image.load("assets/carro1.png")
carro2 = pygame.image.load("assets/carro2.png")
carro3 = pygame.image.load("assets/carro3.png")
telaDeVitoria = pygame.image.load("assets/papapa.png")
fonte = pygame.font.Font("freesansbold.ttf", 50)
ranking = fonte.render("Ranking: ", True, (branco))


movXCar1 = 0
movXCar2 = 0
movXCar3 = 0
posYCar1 = 25
posYCar2 = 170
posYCar3 = 90

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
    tela.blit(carro3, (movXCar3, posYCar3))
    
    if not acabou :
        movXCar1 = movXCar1 + random.randint(0,10)
        movXCar2 = movXCar2 + random.randint(0,10)
        movXCar3 = movXCar3 + random.randint (0,10)
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
    
    if movXCar3 > 880:
        movXCar3 = 0
        posYCar3 = 355
    
    if movXCar1 > movXCar2 and movXCar1 > movXCar3:
        Primeiro = "Vermelho"
        if movXCar2 > movXCar3:
            Segundo = "Amarelo"
            Terceiro = "Azul"
            dist_primeiro_segundo = movXCar1 - movXCar2
            dist_segundo_terceiro = movXCar2 - movXCar3
        else:
            Segundo = "Azul"
            Terceiro = "Amarelo"
            dist_primeiro_segundo = movXCar1 - movXCar3
            dist_segundo_terceiro = movXCar3 - movXCar2
            
    elif movXCar2 > movXCar1 and movXCar2 > movXCar3:
        Primeiro = "Amarelo"
        if movXCar1 > movXCar3:
            Segundo = "Vermelho"
            Terceiro = "Azul"
            dist_primeiro_segundo = movXCar2 - movXCar1
            dist_segundo_terceiro = movXCar1 - movXCar3
        else:
            Segundo = "Azul"
            Terceiro = "Vermelho"
            dist_primeiro_segundo = movXCar2 - movXCar3
            dist_segundo_terceiro = movXCar3 - movXCar1
            
    else:
        Primeiro = "Azul"
        if movXCar1 > movXCar2:
            Segundo = "Vermelho"
            Terceiro = "Amarelo"
            dist_primeiro_segundo = movXCar3 - movXCar1
            dist_segundo_terceiro = movXCar1 - movXCar2
        else:
            Segundo = "Amarelo"
            Terceiro = "Vermelho"
            dist_primeiro_segundo = movXCar3 - movXCar2
            dist_segundo_terceiro = movXCar2 - movXCar1
    
    tela.blit(placar1(Primeiro), (100, 200))
    tela.blit(placar2(Segundo), (100, 250))
    tela.blit(placar3(Terceiro), (100, 300))
    

    

    if posYCar1 == 290 and movXCar1 >= 800 and (movXCar1 > movXCar2 > movXCar3 or movXCar1 > movXCar3 > movXCar2):
        if movXCar1 > movXCar2 > movXCar3:
            tela.blit(telaDeVitoria, (0,0)) 
            acabou = True
            tela.blit(ranking, (100, 100))
            tela.blit(returnVencedor("Vermelho"), (100, 200))
            tela.blit(returnSegundo("Amarelo"), (100,300))
            tela.blit(returnTerceiro("Azul"), (100,400))
        else:
            tela.blit(telaDeVitoria, (0,0)) 
            acabou = True
            tela.blit(ranking, (100, 100))
            tela.blit(returnVencedor("Vermelho"), (100, 200))
            tela.blit(returnSegundo("Azul"), (100,300))
            tela.blit(returnTerceiro("Amarelo"), (100,400))
            
        
    elif posYCar2 == 430 and movXCar2 >= 800 and (movXCar2 > movXCar1 > movXCar3 or movXCar2 > movXCar3 > movXCar1):
        if movXCar2 > movXCar1 > movXCar3:
            tela.blit(telaDeVitoria, (0,0))
            acabou = True
            tela.blit(ranking, (100, 100))
            tela.blit(returnVencedor("Amarelo"), (100, 200))
            tela.blit(returnSegundo("Vermelho"), (100,300))
            tela.blit(returnTerceiro("Azul"), (100,400))
        else:
            tela.blit(telaDeVitoria, (0,0)) 
            acabou = True
            tela.blit(ranking, (100, 100))
            tela.blit(returnVencedor("Amarelo"), (100, 200))
            tela.blit(returnSegundo("Azul"), (100,300))
            tela.blit(returnTerceiro("Vermelho"), (100,400))
        
    elif posYCar3 == 355 and movXCar3 >= 800 and (movXCar3 > movXCar1 > movXCar2 or movXCar3 > movXCar2 > movXCar1):
        if movXCar3 > movXCar1 > movXCar2:
            tela.blit(telaDeVitoria, (0,0))
            acabou = True
            tela.blit(ranking, (100, 100))
            tela.blit(returnVencedor("Azul"), (100, 200))
            tela.blit(returnSegundo("Vermelho"), (100,300))
            tela.blit(returnTerceiro("Amarelo"), (100,400))
        else: 
            tela.blit(telaDeVitoria, (0,0)) 
            acabou = True
            tela.blit(ranking, (100, 100))
            tela.blit(returnVencedor("Azul"), (100, 200))
            tela.blit(returnSegundo("Amarelo"), (100,300))
            tela.blit(returnTerceiro("Vermelho"), (100,400))
        
    pygame.display.update()
    clock.tick(60)
pygame.quit()
    

