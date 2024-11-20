from os import system
import pygame

def placar1(Primeiro):
    fonte = pygame.font.Font("freesansbold.ttf",30)
    placar = f"Primeiro: {Primeiro}"
    return fonte.render(placar, True, (255,255,255))

def placar2(Segundo):
    fonte = pygame.font.Font("freesansbold.ttf",30)
    placar = f"Segundo: {Segundo}"
    return fonte.render(placar, True, (255,255,255))

def placar3(Terceiro):
    fonte = pygame.font.Font("freesansbold.ttf",30)
    placar = f"Terceiro: {Terceiro}"
    return fonte.render(placar, True, (255,255,255))

    
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

