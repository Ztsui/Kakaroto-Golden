from gui import *

#Infelizmente não foi possível implementar o algoritmo A*, então foram utilizadas posições up, down, left e right
#Para que fosse possível criar uma movimentação automática para o agente.
#Utilização: tire do comentário a opção desejada e coloque as outras como comentário!
def Movimentacao(info):
    return up
    #return down
    #return left
    #return right

#Executa o jogo!
if __name__ == "__main__":
    print('Vamos desvendar as esferas do dragão!')
    dragonBall = Principal(Movimentacao)
    exec(dragonBall)