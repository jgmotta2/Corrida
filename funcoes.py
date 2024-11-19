from os import system
import pygame

def limparTela():
    system("Cls")
    
    
def returnVencedor(vencedor):
    fonte = pygame.font.Font("freesansbold.ttf",30)
    colocacao = f"1ª {vencedor}"
    return fonte.render(colocacao, True, (255,255,255))

def returnSegundo(segundo):
    fonte = pygame.font.Font("freesansbold.ttf",30)
    colocacao = f"2ª {segundo}"
    return fonte.render(colocacao, True, (255,255,255))

def returnTerceiro(terceiro):
    fonte = pygame.font.Font("freesansbold.ttf",30)
    colocacao = f"3ª {terceiro}"
    return fonte.render(colocacao, True, (255,255,255))