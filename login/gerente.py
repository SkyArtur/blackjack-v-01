from os import mkdir


class Gerente:
    def __init__(self, *args):
        """
        Responsável pelo armazenamento dos dados do jogador em um arquivo de texto.
        Realiza a leitura do arquivo para confirmar usuário.

        :param args: nome_usuario, senha_usuario
        """
        self.__caminho = './usuarios/usuarios.txt'
        self.__nome = args[0]
        self.__senha = args[1]
        self.__dados = f'{args[0]}${args[1]}'

    def __buscar(self):
        """
        Retorna True se conseguir realizar a leitura do arquivo de usuarios, senão,
        retorna False.

        :return: bool: True|False
        """
        try:
            __arquivo = open(self.__caminho, 'rt')
            __arquivo.close()
        except FileNotFoundError:
            return False
        else:
            return True

    def armazenar(self):
        """
        Verifica se o arquivo do usuário existe e pode ser atualizado, do contrário,
        cria o diretório e o arquivo dos usuários.
        """
        if self.__buscar():
            __arquivo = open(self.__caminho, 'at')
            __arquivo.write(f'{self.__dados}\n')
            __arquivo.close()
        else:
            try:
                mkdir('./usuarios/')
            except FileExistsError:
                pass
            __arquivo = open(self.__caminho, 'wt+')
            __arquivo.write(f'{self.__dados}\n')
            __arquivo.close()

    @property
    def verificar(self):
        """
        Executa a leitura do arquivo de usuários. Retorna True(1, 2), se encontrar
        o nome do usuário ou o nome e senha do usuário, senão, False.

        :return: True|False
        """
        try:
            __arquivo = open(self.__caminho, 'rt')
            __dados_usuarios = __arquivo.readlines()
            usuarios = [dados.strip() for dados in __dados_usuarios]
            __arquivo.close()
            __dados_usuarios.clear()
        except FileNotFoundError:
            print('Arquivo não encontrado!')
        else:
            nome = False
            senha = False
            for usuario in usuarios:
                if self.__nome in usuario[:usuario.find('$')]:
                    nome = True
                if self.__senha in usuario[usuario.find('$') + 1:]:
                    senha = True
            if nome is True and senha is True:
                return 1
            elif nome is True and senha is False:
                return 2
            else:
                return False

