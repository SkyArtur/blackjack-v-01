<p align="center" >
  <img width="360" height="180" alt="Logo BlackJack" src="https://user-images.githubusercontent.com/93395366/173211055-85e66ac3-a3b0-4bda-abca-a04e7da4752f.png">
</p>
<hr>

# Projeto prático no apredizado em Python

> Status : Concluído

![GitHub forks](https://img.shields.io/github/forks/skyartur/blackjack-v-01?style=social)
![GitHub Repo stars](https://img.shields.io/github/stars/SkyArtur/blackjack-v-01?style=social)

## Sobre mim e sobre este projeto:
Quando resolvi deixar de ser um simples usuário, e passar a fazer parte deste universo da programação, um sentimento de pânico surgiu quando comecei a imaginar como eu faria para aprender tantas linguagens de programação, tantas siglas e tudo mais. Mas com a ajuda, mesmo a distância, de professores, amigos e livros, as coisas começaram a fluir. Por uma semana busquei reunir o pouco que aprendi neste projeto, o qual espero que no futuro, possa olhar com vergonha pelos erros que cometi, mas que por hora, me dá muito orgulho.
O programa em linha de comando, foi escrito em Python e tem como base o exercício proposto no livro - Introdução a computação usando Python de Ljubomir Perkovic,pg. 203-206, 2016. Embora baseado no código do livro, muito foi adicionado com o intuito de abranjer os conhecimentos básicos da linguagem, que aprendi até o momento.

## Conceitos Básicoa Abordados:
- métodos de manipulação de strings
- list comprehension
- laços de iteração
- dicionários
- type casting
- docstrings
- imports
- manipulaçao de arquivo de texto
- programação procedural 
- e uma tentativa de orientação a objetos😁

Acrescentei um login e cadastro de novos usuários. O nome do usuário e senha são armazenados em um arquivo .txt que uso como armazenamento (ainda não cheguei em Banco de Dados). Uso o algoritmo MD5 para criar uma concatenação entre o hash do nome do usuário e senha:

     7b5a67574d8b1d77d2803b24946950f0$0e1ebad68af7f0ae4830b7ac92bc3c6f
     
O sinal '$' me permite realizar a leitura do hash e validar o nome do usuário e a senha, liberando o login, também é utilizado para não permitir que outro usuário seja criado com um nome de usuário já existente. Apessar da simplicidade do programa, afinal, também não cheguei ainda em GUI 😔, ele me deu confiança de que consigo programar. Afinal, deu trabalho bolar o login. 

Também criei inputs para o usuário de modo a não permtir que o programa quebre por uma entrada de dado de tipo incorreto.

https://user-images.githubusercontent.com/93395366/173219560-8ac99e2e-27e1-472c-b829-ea4fd099691a.mp4

O programa é dividido em sete módulos, o principal, três módulos para login e três para o jogo. A pasta usuarios, onde fica armazenado o arquivo .txt é criada automaticamente apartir do primeiro usuário cadastrado. 

Há um executável em exe.win-amd64-3.10, feito com cx-Freeze.
 
## Agradecimento mais que especial 🙏

Aos queridos e competentes intrutores Alura, que têm me ajudado nessa minha nova empreitada: 

| [<img src="https://avatars.githubusercontent.com/u/74275?v=4" width=115><br><sub>Nico Steppat</sub>](https://github.com/steppat) |  [<img src="https://avatars.githubusercontent.com/u/30351153?v=4" width=115><br><sub>Guilherme Lima</sub>](https://github.com/guilhermeonrails) |  [<img src="https://avatars.githubusercontent.com/u/8438821?v=4" width=115><br><sub>Gabriel Saldanha</sub>](https://github.com/gcrsaldanha) | [<img src="https://avatars.githubusercontent.com/u/3089882?v=4" width=115><br><sub>Vanessa Me Tonini</sub>](https://github.com/vanessametonini) | [<img src="https://avatars.githubusercontent.com/u/215004?v=4" width=115><br><sub>Pedro Marins</sub>](https://github.com/pedromarins) | [<img src="https://avatars.githubusercontent.com/u/6991415?v=4" width=115><br><sub>Vinicius Dias</sub>](https://github.com/cviniciussdias) | [<img src="https://avatars.githubusercontent.com/u/51391?v=4" width=115><br><sub>Guilherme Silveira</sub>](https://github.com/guilhermesilveira) | [<img src="https://avatars.githubusercontent.com/u/71636?v=4" width=115><br><sub>Paulo Silveira</sub>](https://github.com/peas)
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |

## Autor

| [<img src="https://avatars.githubusercontent.com/u/93395366?v=4" width=115><br><sub>Artur dos Santos Shon</sub>](https://github.com/SkyArtur) 
| :---: |
