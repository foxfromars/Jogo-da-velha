
import sys
def main():    
    
    Jogo_da_velha = [
        ['[ ]','[ ]','[ ]'],
        ['[ ]','[ ]','[ ]'],
        ['[ ]','[ ]','[ ]']
    ]
    playerCount = 1
    def display():
        for e in range(0,3):
            for i in range(0,3):
                print(Jogo_da_velha[e][i],end='')
            print('\n')
    def vitoria():
        for e in range(0,3):
            #checar horizontal
            if Jogo_da_velha[e][0]=='[X]' or Jogo_da_velha[e][0]=='[O]': 
                if Jogo_da_velha[e][0]==Jogo_da_velha[e][1] and Jogo_da_velha[e][0]==Jogo_da_velha[e][2]:
                    return True 
            #checar vertical
            if Jogo_da_velha[0][e]=='[X]' or Jogo_da_velha[0][e]=='[O]':                
                if Jogo_da_velha[0][e]==Jogo_da_velha[1][e] and Jogo_da_velha[0][e]==Jogo_da_velha[2][e]:
                    return True     
        if Jogo_da_velha[0][0]=='[X]' or Jogo_da_velha[0][0]=='[O]':
            if Jogo_da_velha[0][0]==Jogo_da_velha[1][1] and Jogo_da_velha[0][0]==Jogo_da_velha[3][3]:
                return True
        if Jogo_da_velha[0][2]=='[X]' or Jogo_da_velha[0][2]=='[O]':
            if Jogo_da_velha[0][2]==Jogo_da_velha[1][1] and Jogo_da_velha[0][2]==Jogo_da_velha[2][0]:
                return True    
    def atualizar(jogada, jogador):
        y=int(jogada[0]) - 1
        x=int(jogada[2]) - 1
        if Jogo_da_velha[y][x]=='[ ]':
            if jogador%2!=0:
                Jogo_da_velha[y][x]='[X]'
            elif jogador%2==0:
                Jogo_da_velha[y][x]='[O]'
    def check(jogada):
        if Jogo_da_velha[int(jogada[0])-1][int(jogada[2])-1]=='[ ]':
            return True
        else:
            return False
    def playAgain():
        playAgain = input('Você gostaria de jogar novamente Y/N ?')
        if playAgain=='Y':
            main()
        else:
            print('obrigado por jogar!!')
            exit()
    print('JOGO DA VELHA NO TERMINAL!!!')
    countUp=0
    while True :    
        #checar o empate
        if countUp==9:
            print('EMPATE!!')
            playAgain() 
        display()
        jogada=input('introduza sua jogada:')
        if check(jogada)==True:
            atualizar(jogada,playerCount)
        else :
            print('!!!JOGADA INVÁLIDA!!!')
            continue        
        if vitoria()==True:
            if playerCount%2!=0:
                print('Jogador 1 venceu!!')
            else:
                print('Jogador 2 venceu!!')
            playAgain()        
        playerCount+=1
        countUp+=1
main()
