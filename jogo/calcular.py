class CalcularMao:
    def __init__(self, mao: list):
        """
        Recebe uma lista contendo as cartas da mão a ser calculada. Procura em um
        dicionário, um valor para a carta que seja correspondete a sua grandeza.
        Guarda os áses tirados pelos jogadores. Atribui aos áses o valor 11 ou 1.
        Retorna o cálculo da mão do jogador

        :param mao: lista de cartas do jogador.
        """
        self.__valores = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                          '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        self.__mao = mao
        self.__resultado_da_mao = 0
        self.__ases = 0

    @property
    def cacular(self):
        """
        Soma os valores das cartas. Verifica se há áses no jogo, e define o valor
        dos áses em 1 ou 11 a depender da presença deles na mão.

        :return: int -> resultado da mão
        """
        for carta in self.__mao:
            self.__resultado_da_mao += self.__valores[carta[:-1]]
            if "A" in carta:
                self.__ases += 1
        while self.__resultado_da_mao > 21 and self.__ases > 0:
            self.__resultado_da_mao -= 10
            self.__ases -= 1
        return self.__resultado_da_mao


class CompararMaos(CalcularMao):
    def __init__(self, casa, jogador):
        """
        Classe responsável por comparar as mãos do jogador e da casa e definir o
        vencedor da rodada ou o empate, que só irá ocorrer quando o total da mão
        e número de cartas em cada mão forem iguais. Caso contário, o jogador com
        o menor número de cartas na mão é o vencedor da rodada.

        :param casa: int: soma da mão da casa
        :param jogador: int: soma da mão do  jogador
        """
        super().__init__(casa)
        self.__total_casa = self.cacular
        super().__init__(jogador)
        self.__total_jogador = self.cacular
        self.__resultado = self.__resultado(casa, jogador)

    def __str__(self):
        """
        Permite a impressão da mensagem de retorno da classe.

        :return: str: -> resultado
        """
        return self.__resultado

    def __resultado(self, casa, jogador):
        """
        Compara o total das mãos da casa e do jogador e retorna o resultado. Para
        critério de desempate o número de cartas menor em mãos, define o ganhador,
        se ambos possuirem o mesmo número de cartas a vitória vai para o jogador.

        :param casa: total da mão da casa
        :param jogador: total da mão do jogador
        :return: str: -> mensagem
        """
        if self.__total_jogador < self.__total_casa <= 21:
            return "Você Perdeu!"
        elif self.__total_casa < self.__total_jogador <= 21:
            return "VOCÊ GANHOU!"
        elif self.__total_casa == 21:
            return "Você Perdeu"
        elif self.__total_jogador == 21:
            return "VOCÊ GANHOU!"
        elif (self.__total_casa == self.__total_jogador) == (len(casa) < len(jogador)):
            return "Você Perdeu!"
        elif (self.__total_casa == self.__total_jogador) == (len(casa) >= len(jogador)):
            return "VOCÊ GANHOU!"
        else:
            return "Empate!"
