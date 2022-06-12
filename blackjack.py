from jogo.baralho import Baralho
from jogo.calcular import CalcularMao, CompararMaos
from jogo.menu import Menu
from login.cadastro import Cadastro
from sys import exit

letreiro = f'''
Copyright (c) 2022.
SkyArtur - Ponta Grossa/PR - Projeto BlackJack.
Este software é um exercício prático em Python.
----------------------------------------------       
 _     _            _                   _          
| |   | |          | |     _           | | 
| '_ \| |/ _` |/ __| |/ / | |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <  | | (_| | (__|   <
|_.__/|_|\__,_|\___|_|\_\ | |\__,_|\___|_|\_ 
                         _/ |
                        |__/  
----------------------------------------------'''


def pergunta_final():
    """
    Exibe o menu final da rodada.

    :return: function: blackjack | exit
    """
    resposta = Menu().menu_final
    return blackjack() if resposta == 1 else iniciar_blackjack()


def blackjack():
    """
    Função principal que possui todo o processamento do jogo.
    """
    msg_01 = """Você Perdeu!
        Sua mão ultrapassou...
        """
    msg_02 = """VOCÊ GANHOU!
    A casa ultrapassou...
    """
    baralho = Baralho
    casa = []
    jogador = []

    for i in range(2):
        jogador.append(baralho().dar_carta)
        casa.append(baralho().dar_carta)

    total_casa = CalcularMao(casa).cacular
    total_jogador = CalcularMao(jogador).cacular

    baralho.print_carta(casa)
    print(f" CASA - Total: {total_casa}")

    baralho.print_carta(jogador)
    print(f" JOGADOR - Total: {total_jogador}")

    resposta = Menu().menu_jogo

    while resposta == 1 and total_jogador < 21:
        jogador.append(baralho().dar_carta)
        total_jogador = CalcularMao(jogador).cacular
        baralho.print_carta(jogador)
        print(f" JOGADOR - Total: {total_jogador}")
        if total_jogador > 21:
            print(msg_01)
            return pergunta_final()
        resposta = Menu().menu_jogo

    while total_casa < total_jogador:
        casa.append(baralho().dar_carta)
        total_casa = CalcularMao(casa).cacular
        baralho.print_carta(casa)
        print(f" CASA - Total: {total_casa}")
        if total_casa > 21:
            print(msg_02)
            return pergunta_final()

    print(CompararMaos(casa, jogador))
    return pergunta_final()


def iniciar_blackjack():
    """
    Realiza o login do jogador ou o cadastro do novo jogador. Chama a função
    blackjack() e inicia o jogo.
    """
    msg_01 = """Atenção:
    Usuário ou senha inválidos. 
    """
    msg_02 = """Atenção:
    Usuário já cadastrado!
    """
    msg_03 = """Sucesso:
    Novo usuário cadastrado!
    """
    print(letreiro.strip())
    while True:
        resposta = Menu().menu_inicial
        if resposta == 1:
            usuario = Cadastro().validar_usuario
            if not usuario:
                print(msg_01)
                continue
            else:
                blackjack()
        elif resposta == 2:
            usuario = Cadastro().cadastrar
            while not usuario:
                print(msg_02)
                usuario = Cadastro().cadastrar
            else:
                print(msg_03)
                blackjack()
        else:
            exit()


if __name__ == "__main__":
    iniciar_blackjack()
