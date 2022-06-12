from login.entrada import Entrada
from login.gerente import Gerente


class Usuario:
    def __init__(self):
        """
        Criar objeto usuário, seus atributos nome e senha, e suas respectivas
        propriedades.
        """
        self.__nome_usuario = None
        self.__senha_usuario = None

    def __iter__(self):
        return

    @property
    def nome(self):
        return self.__nome_usuario

    @nome.setter
    def nome(self, nome):
        self.__nome_usuario = nome

    @property
    def senha(self):
        return self.__senha_usuario

    @senha.setter
    def senha(self, senha):
        self.__senha_usuario = senha


class Cadastro(Usuario):
    def __init__(self):
        """
        Fornece input parametrizado para settar atributos a <class>Usuario.
        Armazena os dados do usuário. Verifica a existência do usuario em arquivo.
        """
        super().__init__()
        self.nome = Entrada('Digite seu nome de usuário: ').hash_entrada
        self.senha = Entrada('Digite a sua chave: ').hash_entrada

    @property
    def cadastrar(self):
        """
        Recebe nome e senha de <class>Usuario e chama a <class>Gerente para verificar
        se o usuário já está cadastrado, se não, realiza o cadastro do usuário.

        :return: ->  False if: Gerente is True else True
        """
        if Gerente(self.nome, self.senha).verificar:
            return False
        else:
            Gerente(self.nome, self.senha).armazenar()
            return True

    @property
    def validar_usuario(self):
        """
        Recebe nome e senha de <class>Usuario e chama a <class>Gerente para verificar
        se o usuário já está cadastrado, senão, retorna False.

        :return: ->  True if: Gerente is True
                 -> False else:
        """

        if Gerente(self.nome, self.senha).verificar == 1:
            return True
        else:
            return False
