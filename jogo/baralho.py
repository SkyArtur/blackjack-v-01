from random import shuffle
from time import sleep


class Baralho:
    def __init__(self):
        """
        Construtora do baralho. Concatena os valores das listas 'naipes' e 'grandezas',
        retorna uma carta do baralho criado, através de sua propriedade 'dar_cartas'.

        @property
        dar_carta -> str: carta
        """
        self.__naipes = ['\u2660', '\u2665', '\u2666', '\u2663']
        self.__grandezas = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.__baralho_misturado = []
        self.__criar_baralho()
        self.__carta = self.__baralho_misturado.pop()

    @property
    def dar_carta(self):
        """
        Getter. Retorna a carta para o jogador

        :return: str -> carta
        """
        return self.__carta

    def __criar_baralho(self):
        """
        Função criadora do jogo. Retorna uma lista com os valores fora de
        sequência.

        :return: shuffle(list()) -> baralho_misturado
        """
        for naipe in self.__naipes:
            for grandeza in self.__grandezas:
                self.__baralho_misturado.append(f"{grandeza}{naipe}")
        return shuffle(self.__baralho_misturado)

    @classmethod
    def print_carta(cls, cartas):
        """
        Exibe ascii art da carta retirada. Usa função sleep() do módulo 'time'
        para gerar um pequeno atraso na exibição das cartas.

        :param cartas: list[]
        :return: print() -> cartas
        """
        fig = "\u2668"
        for i in cartas:
            carta = f''' ___________
|        {i:<3}|
| |   {fig}   | |
|___________|'''
            sleep(0.3)
            print(carta)
