from pygame import *
from sys import exit
from os import path
from kakarotoPrincipal import *


def exec(dragonBall):
    #executa o pygame (biblioteca escolhida para o 2D :] )
    init()
    #Leque de cores para utilização!!
    #Você pode mudar a paleta do seu planeta como desejar! Basta localizar o item em questão e trocar seu nome por um da Lista!!
    #caso deseje, você pode adicionar mais opções também ao utilizar o sistema RGB
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BROWN = (218,165,32)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    PURPLE = (128, 0, 128)
    ORANGE = (255, 165, 0)
    GREY = (128, 128, 128)
    TURQUOISE = (64, 224, 208)

#Aqui você pode trocar a skin do agente! Utilize a que você mais gostar!!
#Apenas troque o comentário com cada linha de código.

#   kakaroto = image.load(path.join("medio-kakaroto.png"))
#   kakaroto = image.load(path.join("piccolo1.png"))
#   kakaroto = image.load(path.join("piccolo2.png")) #melhor otimizado por causo do tamanho!
    kakaroto = image.load(path.join("cade_o_luffy.jpg"))
#   kakaroto = image.load(path.join("mini-kakaroto.png"))
    casaMestreKame = image.load(path.join("kame.png"))
    bolinhaDoDragao = image.load(path.join("bolinha.png"))
    #aqui você pode aumentar ou diminuir o tamanho da tela! Mas não é recomendado por causa de possíveis bugs de rendeziração da matriz!
    screen = display.set_mode((600, 600), 0, 0, 0, 0)
    #Esta é a velocidade que o agente precisa esperar para começar a andar!
    tempoPartida = 1000
    clock = time.Clock()

    #Temos uma musiquinha para acompanhar nosso herói em sua jornada!!
    mixer.music.load("the-rules.mp3")
#    mixer.music.load("GT.mp3")
#   mixer.music.load("classico.mp3")
    mixer.music.play(-1)

    while True:
        for e in event.get():
            if e.type == QUIT:
                exit(0)
        #escolhe a cor do mundo (fora da matriz)
        screen.fill(TURQUOISE)
        #velocidade do personagem!
        tempoPartida -= clock.tick()
        if tempoPartida < 0:
            dragonBall.executar()
            #No tempoPartida abaixo, é possível escolher a velocidade que o agente irá percorrer cada terreno
            #1000ms = 1s    (quanto menor, mais rápido)
            tempoPartida = 500
            display.set_caption("Kakaroto Golden! Esforço: " + str(dragonBall.custo) + ", Terrenos: " + str(dragonBall.contagem))

        #Gerador do mapa!
        #Aqui é um processo importante, pois irá definir o mapa e seus terrenos!!
        for x, i in enumerate(range(-8, 9)):
            for y, j in enumerate(range(-8, 9)):
                p = (dragonBall.posicaoAgente[0] + i, dragonBall.posicaoAgente[1] + j)
                #Gerando os terrenos como retângulos
                if p[0] >= 0 and p[0] < dragonBall.tamanho and p[1] >= 0 and p[1] < dragonBall.tamanho:
                    cor = BLUE
                    if dragonBall.mapa[p[0]][p[1]] == TM:
                        cor = BROWN
                    elif dragonBall.mapa[p[0]][p[1]] == TG:
                        cor = GREEN
                    draw.rect(screen, cor, rect.Rect((x * 36, y * 36), (36, 36)))
                    #Colocando o ponto de partida
                    if p == dragonBall.casinhaMestreKame: screen.blit(casaMestreKame, rect.Rect((x * 36 + 5, y * 36), (36, 36)))
                    #Gerando todas as esferas no mapa em modo aleatório
                    if p in dragonBall.esferas: screen.blit(bolinhaDoDragao, rect.Rect((x * 36 + 6, y * 36 + 8), (36, 36)))

        # desenha o personagem escolhido
        screen.blit(kakaroto, rect.Rect((294, 288), (36, 36)))
        #gera as linhas do radar
        draw.lines(screen, PURPLE, True, [(180, 180), (180, 432), (432, 432), (432, 180)], 1)
        #função do pygame para atualizar a tela gráfica
        display.update()
        #exibição no console do python com a pontuação total
        print("Kakaroto Golden Z! Esforço: " + str(dragonBall.custo) + ", Terrenos: " + str(dragonBall.contagem))




