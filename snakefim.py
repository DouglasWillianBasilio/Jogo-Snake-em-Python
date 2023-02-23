import random
import curses



#MENU BASICO DO JOGO
def print_menu():
    print("+---------------------------------+")
    print("|        JOGO DA COBRINHA         |")
    print("+---------------------------------+")
    print("| Opções:                         |")
    print("| 1. Iniciar                      |")
    print("+---------------------------------+")

def get_menu_choice():
    choice = input("Escolha uma opção: ")
    return choice

def main():
    print_menu()
    choice = get_menu_choice()
    if choice == '1':
        # Iniciar Jogo
        pass
    
    else:
        print("Opção inválida, escolha novamente.")
        main()

if __name__ == "__main__":
    main()


# ALTURA E LARGURA DO TERMINAL
altura, largura = curses.initscr().getmaxyx()
janela = curses.newwin(altura, largura, 0, 0)


#CONFIGURANDO CURSES
curses.curs_set(False)
janela.keypad(True)
janela.nodelay(True)

#CRIANDO LIMITE DE TELA
for pos in range(0, largura -1):
    janela.addch(0, pos, '-')
    janela.addch(altura -1, pos, '-')

for pos in range (0, altura -1):
     janela.addch(pos, 0, '-')
     janela.addch(pos, largura -1, '-')

#CRIANDO E ADICIONANDO COBRA 
cobra = [[2, 4], [2, 3], [2, 2]]
for pos in range (0, len(cobra)):
     janela.addch(cobra[pos][0], cobra [pos][1], '#')


posicao_cabeca = [2, 4]

#CRIANDO E ADICIONANDO MAÇÃ
maca = [5, 5]
janela.addch(maca[0], maca[1], '*')

#ÍNICIO DE MOVIMENTO
tecla = -1
tecla_nova = curses.KEY_RIGHT
ultima_posicao = 'r'

#COLOCANDO PONTUAÇÃO E AUMENTANDO VELOCIDADE
pontuacao = 0
velocidade_movimento = 100


#JOGO
while True:
    tecla_nova = janela.getch()
    tecla = tecla if tecla_nova == -1 else tecla_nova  #RECEBENDO INFORMAÇÃO DO TECLADO CASO USUARIO NAO DIGITE NADA COBRA CONTINUA A DIREITA


#CONTROLE TECLAS EM RELAÇAO AO MOVIMENTO DA COBRA
    if tecla == curses.KEY_DOWN   and ultima_posicao != 'u': ultima_posicao ='d'
    elif tecla == curses.KEY_UP and ultima_posicao != 'd': ultima_posicao ='u'
    elif tecla == curses.KEY_LEFT and ultima_posicao != 'r': ultima_posicao ='l'
    if tecla == curses.KEY_RIGHT and ultima_posicao != 'l': ultima_posicao ='r'

    if ultima_posicao =='r':posicao_cabeca[1] +=1
    if ultima_posicao =='l':posicao_cabeca[1] -=1
    if ultima_posicao =='u':posicao_cabeca[0] -=1
    if ultima_posicao =='d':posicao_cabeca[0] +=1

#CONTROLANDO COBRA AO PEGAR UMA MAÇÃ
    if posicao_cabeca == maca:
        pontuacao +=1
        maca =[random.randint(1, altura -2),random.randint (1, largura -2)]
        janela.addch(maca[0], maca[1], '*')
        velocidade_movimento = velocidade_movimento -10 if velocidade_movimento -10>5 else velocidade_movimento

    #CASO COBRA BATA NAS BORDAS
    elif (posicao_cabeca[0] == altura -1 or posicao_cabeca[0] == 0) or (posicao_cabeca[1] == largura -1 or posicao_cabeca[1] == 0): break
        

    #CASO NÃO SEJA NADA CONTINUA MOVIMENTO
    else:
        cauda = cobra.pop()
        janela.addch(cauda[0], cauda[1], ' ')

    
    cobra.insert(0, list(posicao_cabeca))
    janela.addch(posicao_cabeca[0], posicao_cabeca[1], '#')

    #CASO COBRA BATA NELA MESMO
    if cobra[0] in cobra[1:]:break
    #VELOCIDADE DA COBRA
    curses.napms(velocidade_movimento)
    janela.refresh()

#MENSAGEM DE PONTUAÇÃO
janela.addstr(int(altura / 2), int(largura / 2.5), "Pontuação: " + str(pontuacao))
janela.refresh()
curses.napms(2000)
curses.endwin()

#PAUSE

#pause = input("O jogo foi PAUSADO digite 'c' para continuar: ")
#if pause == 'p':
    #while True:
        #continue_ = input("Digite 'c' para continuar: ")
        #if continue_ == 'c':
            #break