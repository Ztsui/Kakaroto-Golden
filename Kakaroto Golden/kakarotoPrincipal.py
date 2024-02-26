from math import sin, cos, sqrt, degrees, atan2
from random import seed, random, randint
from copy import deepcopy
#
#Este arquivo contém todas as mecânicas utilizadas para fazer o jogo!
#Tudo está devidamente comentado também!
#
#

#declaração das variáveis de terreno e movimentação
#T = Terreno // C = Custo
CG = 1
TG = 1
CA = 10
TA = 2
CM = 35
TM = 3
up = 1
down = 2
left = 3
right = 4
#Validação do espaço das esferas (utilizado em def executar)
def verificaEspaco(ls, li, p):
    return ls[0] >= p[0] and ls[1] >= p[1] and li[0] <= p[0] and li[1] <= p[1]

class Node:
    def __init__(self, position, g_score, h_score):
        self.position = position
        self.g_score = g_score
        self.h_score = h_score

    def f_score(self):
        return self.g_score + self.h_score

class Principal:

    def astar(self, initial_state, goal_state, map):
        open_list = [Node(initial_state, 0, self.heuristic(initial_state, goal_state))]

    def __init__(self, agente, tamanho=84, semente=None):
        #Tamanho = tamanho do mapa // Semente = gerar o mapa aleatóriamente
        self.agente = agente
        self.tamanho = tamanho
        if semente is not None:
            seed(semente)
        #Cria a casinha do mestre Kame e as esferas!
        self.casinhaMestreKame = (randint(0, tamanho - 1), randint(0, tamanho - 1))
        self.esferas = [(randint(0, tamanho-1), randint(0, tamanho-1)) for _ in range(7)]
        self.esferas = [pos for pos in self.esferas if pos != self.casinhaMestreKame]

        #Criação do mapa
        aa = [random() for _ in range(6)]
        seno = [[sin(aa[0] * x ** 2 + aa[1] * y + aa[2]) for y in range(tamanho)] for x in range(tamanho)]
        coseno = [[cos(aa[3] * y ** 2 + aa[4] * x + aa[5]) for y in range(tamanho)] for x in range(tamanho)]
        self.mapa = [[None] * tamanho for _ in range(tamanho)]
        for x in range(tamanho):
            for y in range(tamanho):
                z = seno[x][y] + coseno[x][y]
                if z < -.5:
                    self.mapa[x][y] = 1
                elif z < .5:
                    self.mapa[x][y] = 2
                else:
                    self.mapa[x][y] = 3
        #Criação dos objetos: agente, contagem de terrenos e seus custos
        self.posicaoAgente = list(self.casinhaMestreKame)
        self.contagem = 0
        self.custo = 0


    def executar(self):
        #Contagem da QUANTIDADE dos terrenos.
        self.contagem += 1
        #Coleta das esferas
        if tuple(self.posicaoAgente) in self.esferas:
            self.esferas.remove(tuple(self.posicaoAgente))
        #Tentativa de criar o radar dragão com base na rosa dos ventos (direções NSLO)
        radar_direcao = {direcao: 0 for direcao in
                         ["norte", "sul", "leste", "oeste", "nordeste", "noroeste", "suldeste", "suldoeste"]}
        proximidade = list()
        limite_sup = (self.posicaoAgente[0] - 3, self.posicaoAgente[1] - 3)
        limite_inf = (self.posicaoAgente[0] + 3, self.posicaoAgente[1] + 3)

        for p in self.esferas:
            if verificaEspaco(limite_sup, limite_inf, p):
                proximidade.append(p)
            else:
                angulo = degrees(atan2((p[1] - self.posicaoAgente[1]), (p[0] - self.posicaoAgente[0])))

                if angulo < 0: angulo = -angulo + 180
                #Implementação a ser utilizada com o algoritmo A*, porém sem sucesso
               # limites_direcoes = [(112.5, "norte"), (292.5, "sul"), (22.5, "leste"), (202.5, "oeste"),
               #                    (67.5, "nordeste"),  (157.5, "noroeste"), (247.5, "suldoeste"),  (337.5, "suldeste")]

        #Verificação dos objetos criados + verificação do radar Dragão
        direcao = self.agente({ "posicao": deepcopy(self.posicaoAgente), "área do radar": proximidade,
                                "casinha do mestre": deepcopy(self.casinhaMestreKame), "esferas do dragão": len(self.esferas)
        })

        if not isinstance(direcao, int) or direcao not in range(1, 5):
            raise Exception("Fora de alcance.")

        direcoes = {
            1: (0, -1),  # Up
            2: (0, 1),  # Down
            3: (-1, 0),  # Left
            4: (1, 0),  # Right
        }
        dx, dy = direcoes[direcao]
        x, y = self.posicaoAgente

        if not (0 <= x + dx < self.tamanho and 0 <= y + dy < self.tamanho):
            raise Exception("Kakaroto, volte imediatamente! Não é para você sair deste planeta antes de completar o treino!")

        # Mapeamento dos custos dos terrenos
        CUSTOS_TERRENOS = {
            TG: CG,
            TM: CM,
            TA: CA,
        }

        # Atualiza custo e posição do agente
        custo_terreno = CUSTOS_TERRENOS[self.mapa[self.posicaoAgente[0]][self.posicaoAgente[1]]]
        self.custo += custo_terreno
        if direcao == up:
            self.posicaoAgente[1] -= 1
        elif direcao == down:
            self.posicaoAgente[1] += 1
        elif direcao == left:
            self.posicaoAgente[0] -= 1
        else:
            self.posicaoAgente[0] += 1




