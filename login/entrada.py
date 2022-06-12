from hashlib import md5


class Entrada:
    def __init__(self, entrada='=> '):
        """
        Input para entrada de dados do usuário. Higieniza a entrada do usuário,
        retornando um string sem caractéres acentuados ou espaços vazios.

        :param entrada: entrada_usuario
        """
        self.__entrada = self.__validar(entrada)

    def __validar(self, entrada):
        """
        Função para validação da entrada do usuário mantendo o mesmo em um laço
        até que os caractéres digitados não contenham  espaços ou acentos.

        :param entrada: input(entrada)
        :return: str: -> entrada do usuário
        """
        msg = '''Atenção:
        Não são aceitos letras acentuadas ou 
        espaços vazios entre as letras.
        '''
        while True:
            self.__entrada = input(entrada)
            if self.__entrada.find(' ') > -1 or not self.__entrada.isascii():
                print(msg)
            else:
                return self.__entrada

    @property
    def hash_entrada(self):
        """
        Usa a função md5() do módulo hashlib para transformar a entrada do usuário
        em um hash.

        :return: hash(entrada_usuario)
        """
        self.__entrada = bytes(str(self.__entrada.strip()), 'utf-8')
        self.__entrada = md5(self.__entrada).hexdigest()
        return self.__entrada



