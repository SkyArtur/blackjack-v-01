class Menu:
    def __int__(self):
        """
         Disponibiliza os menus do jogo, processa os inputs do usuário. Retorna
         um valor inteiro correspondente a escolha do usuário.

         Propriedades:
            - menu_inicial
            - menu_jogo
            - menu_final

        """
        self.__resposta = None

    def __processar_menu(self, opcao1=None, opcao2=None, opcao3=None):
        """
        Recebe a entrada do usuário e a compara com os parâmetros repassados como
        opções válidas. Retorna a resposta do usuário apenas se ela for uma letra
        do alfabeto ou uma das opções oferecidas.

        :param opcao1: str: resposta esperada
        :param opcao2: str: resposta esperada
        :param opcao3: str: resposta esperada
        :return: int: resposta do usuário
        """
        msg = '''Atenção:
        Parece que você o que você digitou 
        não é uma opção válida!'''
        while True:
            self.__resposta = input('=> ')
            while not self.__resposta.isalpha():
                print(msg)
                self.__resposta = input('=> ')
            else:
                if self.__resposta in opcao1:
                    self.__resposta = 1
                elif self.__resposta in opcao2:
                    self.__resposta = 2
                elif self.__resposta in opcao3:
                    self.__resposta = 3
                else:
                    print(msg)
                    continue
                return self.__resposta

    @property
    def menu_inicial(self):
        texto = '''Login:
        (L) Efetuar login
        (C) Cadastrar novo
        (S) Sair'''
        print(texto)
        return self.__processar_menu('lL', 'Cc', 'sS')

    @property
    def menu_jogo(self):
        texto = '''O que você deseja a seguir:
        (C) Mais uma Carta
        (P) Parar'''
        print(texto)
        return self.__processar_menu("cC", "pP")

    @property
    def menu_final(self):
        texto = '''Deseja Jogar Outra Vez:
        (S) Sim
        (N) Não'''
        print(texto)
        return self.__processar_menu('sS', "nN")