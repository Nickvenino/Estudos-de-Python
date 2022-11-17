# MODULOS - IMPORT - IMPORTA TUDO DA BIBLIOTECA
# FROM BIBLIOTECA IMPORT NOME DO Q VC QUER - IMPORTAR UMA UNICA COISA DE UMA BIBLIOTECA
# BIBLIOTECA MATH
# CEIL - ARREDONDA PRA CIMA
# FLOOR - ARREDONDA PRA BAIXO
# TRUNC - ELIMINA DA VIRGULA PRA FRENTE
# SQRT - CALULAR RAIZ QUADRADA
# FACTORIAL - FATORIAL
# MATH. - VER TODAS AS FUNCIONALIDADES

#from math import sqrt,trunc
#num = int(input('Insira um número: '))
#raiz = sqrt(num)
#print('A raiz quadrada de {} é {}'.format(num,trunc(raiz)))

#import math 
#num = int(input('Insira um número: '))
#raiz = math.sqrt(num)
#print('A raiz quadrada de {} é {}'.format(num,math.trunc(raiz)))

#MANIPULANDO TEXTO

#FATIAMENTO

# frase[9] - indice 9

#frase = 'nicolli'
#print(frase[6])
# n = 0, i = 1, c = 2, o = 3, l = 4, l = 5, i = 6.
#[1:5] - do 1 ao 4
#[1:10:2] - do ao 10 pulando de 2 em 2
#[:5] - do 0 ao 5
#[5:] - do 5 ao final
#[9::3] - do 9 ao final pulando de 3 em 3

#ANALISE

#Len(frase) - tamanho da frase (quant de caracteres)
#frase = 'nicolli venino santana'
#print(len(frase))

#frase.count('o') - ver quantas vezes aparece a letra o
#frase = 'nicolli venino santana'
#print(frase.count('i'))

#frase.count('o',0,13) - ver quantas vezes aparece a letra o + contagem
#frase = 'nicolli venino santana'
#print(frase.count('o',0,9))

#frase.find('nick') - em que momento começou a parte deo de uma frase - #-1 igual a não tem
#frase = 'nicolli venino santana'
#print(frase.find('nino'))
#frase.rfind - em que momento apareceu pela ultima vez 

# in - curso in fraseo - existe a palavra curso na variavel frase?
#frase = 'nicolli venino santana'
#print('venino' in frase)
#retorna False or True

#TRANSFORMAÇÃO

#frase.replace('nicole', 'nicolli') - substitui nicole para nicolli
#frase = 'nicole venino santana'
#print(frase)
#print(frase.replace('nicole', 'nicolli'))

#frase.upper() - deixar tudo em maiusculo
#frase = 'nicolli venino santana'
#print(frase.upper())

#frase.lower() - deixa tudo em minusculo
#frase = 'NICOLLI VENINO SANTANA'
#print(frase.lower())

#frase.capitalize() - deixa só o primeiro caractere em maiusculo
#frase = 'nicolli venino santana'
#print(frase.capitalize())

#frase.title() - deixa todos primeiros carcteres das palavras em maiusculo
#frase = 'nicolli venino santana'
#print(frase.title())

#frase.strip() - remove espaços no começo e final da frase
#frase = '   nicolli venino santana  '
#print(frase)
#print(frase.strip())

#frase.rstrip() - remove só os espaços da direita (ultimos)
#frase.lscript() - remove só os espaços da esquerda (primeiros)

#DIVISÃO

#frase.split() - divisão considerando os espaços (lista)
#frase = 'nicolli venino santana'
#print(frase.split())

#JUNÇÃO

#'-'.join(frase) - junta considerando os espaços
#frase = 'nicolli venino santana'
#print('-'.join(frase))

#BRINCANDO COM AS MANIPULAÇÕES DE TEXTO

#frase = '   nicolli venino santana  '
#frase = frase.strip()
#lista = frase.split()
#print(lista[0])

#MOSTRA O NOME COM LETRAS MAISCULAS E MINUSCLAS + QUANTIDADE LETRAS DO NOME SEM OS ESPAÇOS E DO PRIMEIRO NOME
#name = input('Digite seu nome inteiro: ')
#print(name.upper())
#print(name.lower())
#separado = name.split()
#n1 = len(separado[0].strip())
#n2 = len(separado[1].strip())
#n3 = len(separado[2].strip())
#resultado = n1+n2+n3
#print('A quantidade de letras do nome, sem os espaços é {}.'.format(resultado))
#quant1name = len(separado[0])
#print('A quantidade de letras do primeiro nome é {}.'.format(quant1name))

#MOSTRAR UNIDADE, DEZENA, CENTA E MILHAR DE UM NÚMERO QUALQUER
#num = int((input('Digite um número de 0 a 9999: ')))
#u = num // 1 %10 #pegar a unidade
#d = num // 10 %10 #pegar a dezena
#c = num // 100 %10 #pegar a centena
#m = num // 1000 %10 #pegar o milhar
#print('Unidade: {}'.format(u))
#print('Dezenas: {}'.format(d))
#print('Centenas: {}'.format(c))
#print('Milhar: {}'.format(m))

#frase = '   nicolli venino santana  '
#frase = frase.strip()
#lista = frase.split()
#print(lista[0])

#LER O NOME DE UMA CIDADE E VER SE ELA COMEÇA COM SÃO:
#cidade = input('Digite o nome da sua cidade: ')
#c = cidade.split()
#if c[0] == 'São':
#        print('Sua cidade começa com o nome São!')
#else:
#        print('Sua cidade não começa com o nome São!')

#OUTRA FORMA:
#city = input('Qual sua ciadade: ')
#c = city.split()
#print("Sua cidade começa com Santo:{}".format('Santo' in c[0]))
#retorna False or True

#VER SE A PESSOA TEM SILVA NO NOME
#name = input('Digite o seu nome:\n')
#print('Você tem Silva no nome: {}'.format('Silva' in name))

#LER UMA FRASE VER QUANTAS VEZES APARECE A LETRA "A", EM QUAL APOSIÇÃO ELA APARECE ´PELA PRIMEIRA E A ULTIMA VEZ
#frase = input('Digite uma frase: ')
#print('A frase contem {} vezes a letra A'.format(frase.count('a')))
#print('A primeira letra A se encontra na posição {}'.format(frase.find('a')))
#print('A ultima letra A se encontra na posição {}'.format(frase.rfind('a')))

#MOSTRAR O PRIMEIRO E O ULTIMO NOME
#name = input('Insira o seu nome inteiro: ')
#print(n)
#print('Primeiro nome: {}'.format(n[0]))
#print('Ultimo nome: {}'.format(n[-1]))

#Pular linha sem pular linha - usar """  """
#print("""bom dia nick
#tenha uma vida legal
#vc é incrivel
#esta tudo bem""")

#EM QUE NÚMERO EU PENSEI:

#from random import randint
#computador = randint(0,10)
#print('Olá! Sou um computador e pensei em um número entre 0 e 10...')
##zwhile jogador != computador:
#        jogador = int(input('Você errou! Tente novamente: '))
#print('PARABÉNS! Você acertou!')

#VERIFICAR SE UM ANO É BISSEXTO OU NÃO:
#from datetime import date
#ano = int(input('Insira o ano que quer analisar (Coloque 0 para o ano atual): '))
#if ano == 0:
#        ano = date.today().year
#if ano %4 ==0 and ano %100 !=0 or ano %400 ==0:
#        print('{}, é um ano BISSEXTO!'.format(ano))
#else:
#        print('{}, NÃO é um ano bissexto!'.format(ano))

#CALCULADORA

#n1 = float(input('Insira o primeiro valor:\n'))
#n2 = float(input('Insira o segundo valor:\n'))
#op = input('insira o tipo de operação:\n')

#if op == '+':
#    soma = n1+n2
#    print('A soma entre {} e {} é {}'.format(n1,n2,soma))
#elif op == '-':
#     sub = n1-n2 
#     print('A subtração entre {} e {} é {}'.format(n1,n2,sub))
#elif op == "*":
#    mult = n1*n2
#    print('A multiplicação entre {} e {} é {}'.format(n1,n2,mult))
#elif op == "/":
#    div = n1/n2
#    print('A divisão entre {} e {} é {}'.format(n1,n2,div))
#elif op == "//":
#    divex = n1//n2
#    print('A divisão exata entre {} e {} é {}'.format(n1,n2,divex))
#elif op == "**":
#    pot = n1**n2
#    print('{}, elevado a {} é {}'.format(n1,n2,pot))
#elif op == "%":
#    rest = n1%n2
#    print('O resto da divisão entre {0} e {1} é {2}'.format(n1,n2,rest))

#CALCULAR A MÉDIA DE NOTAS
#ABAIXO DE 5: REPROVADO
#EXATAMENTE 5: RECUPERAÇÃO
#ACIMA DE 5: APROVADO

#name = input('Olá aluno, qual é o seu nome?\n')
#print('Olá, {}'.format(name))
#port = int(input('Insira a sua nota de português: '))
#mat = int(input('Insira a sua nota de matemática: '))
#geo = int(input('Insira a sua nota de geografia: '))
#his = int(input('Insira a sua nota de história: '))
#art = int(input('Insira s aua nota de artes: '))
#bio = int(input('Insira a sua nota de biologia: '))
#fis = int(input('Insira a sua nota de fisica: '))
#qui = int(input('Insira a sua nota de quimica: '))
#média = (port+mat+geo+his+art+bio+fis+qui)/8
#if média <5:
#    print('{}, você foi REPROVADO! Sua média foi {}'.format(name, média))
#elif média ==5:
#    print('{}, você está de RECUPERAÇÃO! Sua média foi {}'.format(name, média))
#else:
#    print('{}, você foi APROVADO! Sua média foi de {}, parabéns!'.format(name, média))

#MOSTRAR O ANTECESSOR E O SUCESSOR DE UM NÚMERO
#num = int(input('Insira o número: '))
#ant = num-1
#suc = num+1
#print('O antecessor de {} é {} e o sucessor é {}'.format(num,ant,suc))

#PAR OU IMPAR!

#player1 = input('Olá player1! Qual é o seu nome?\n')
#player2 = input('Olá player2! Qual é o seu nome?\n')
#esc1 = input('{}, escolha um entre par ou impar:\n'.format(player1))
#while esc1 == 'par':
#    opção = input('{}, você será impar! Digite ok para continuar: '.format(player2))
#    if opção == 'ok':
#        n1 = int(input('{}, escolha um número: '.format(player1)))
#        n2 = int(input('{}, escolha um número: '.format(player2)))
        # impar + par = impar
        # par + impar = impar
        # par + par + par
        # impar + impar = par
        # player1 = par - player2 = impar
#        while n1%2 == 0:
#            if n2%2 == 0:
#                print('O resultado da soma é PAR! O ganhador é {}!'.format(player1))
#            elif n2%2 != 0:
#                print('O resultado da soma é IMPAR! O ganhador é {}!'.format(player2))
#            break
#        while n1%2 != 0:
#            if n2%2 == 0:
#                print('O resultado da soma é IMPAR! O ganhador é {}!'.format(player2))
#            elif n2%2 != 0:
#                print('O resultado da soma é PAR! O ganhador é {}!'.format(player1))
#            break
#    break
#while esc1 == 'impar':
#    opção = input('{}, você será par! Digite ok para continuar: '.format(player2))
#    if opção == 'ok':
#        n1 = int(input('{}, escolhe um número: '.format(player1)))
#        n2 = int(input('{}, escolha um número: '.format(player2)))
#        while n1%2 == 0:
#            if n2%2 == 0:
#               print('O resultado da soma é PAR! O ganhador é {}!'.format(player2))
#            elif n2%2 != 0:
#                print('O resultado da soma é IMPAR! O ganhador é {}!'.format(player1))
#            break
#        while n1%2 != 0:
#            if n2%2 == 0:
#                print('O resultado da soma é IMPAR! O ganhador é {}!'.format(player1))
#            elif n2%2 != 0:
#                print('O resultado da soma é PAR! O ganhador é {}!'.format(player2))
#            break
#    break
#
#verresultado = input('Desejam ver o resultado? Digite sim ou não: ')
#if verresultado == 'sim':
#    resultado = n1+n2
#    print('{} somado a {} é {}.'.format(n1,n2,resultado))


#PEDRA, PAPEL E TESOURA!

#player1 = input('Olá player1! Qual é o seu nome?\n')
#player2 = input('Olá player 2! Qual é o seu nome?\n')
#jogada1 = input('{}, digite um entre pedra, papel ou tesoura:\n'.format(player1))
#jogada2 = input('{}, digite um entre pedra, papel ou tesoura:\n'.format(player2))

#while jogada1 == jogada2:
#    print('EMPATE! Tentem novamente!')
#    jogada1 = input('{}, digite um entre pedra, papel ou tesoura:\n'.format(player1))
#    jogada2 = input('{}, digite um entre pedra, papel ou tesoura:\n'.format(player2))

#while jogada1 == 'papel':
#    if jogada2 == 'pedra':
#        print('O ganhador é {}!'.format(player1))
#    elif jogada2 == 'tesoura':
#        print('O ganhador é {}!'.format(player2))
#    break
#while jogada1 == 'pedra':
#    if jogada2 == 'papel':
#        print('O ganhador é {}!'.format(player2))
#    elif jogada2 == 'tesoura':
#        print('O ganhador é {}!'.format(player1))
#    break
#while jogada1 == 'tesoura':
#    if jogada2 == 'papel':
#        print('O ganhador é {}!'.format(player1))
#    elif jogada2 == 'pedra':
#        print('O ganhador é {}!'.format(player2))
#    break

#BRINCANDO COM VARIAVEIS
#var1 = 'azul'
#var2 = 'vermelho'
#var3 = 'rosa'
#var4 = 'verde'
#print('A flor é {0}, o carro é {1}, o céu é {2} e a árvore é {3}.'.format(var3,var2,var1,var4))

#BRIMCANDO COM OS CARACTERES
#name = input('Qual o seu nome?\n')
#print('Bom dia, {:#^20}!'.format(name))
#year1 = int(input('Em que ano você nasceu, {:>10}?\n'.format(name)))
#year2 = int(input('Em que ano estamos agora, {:<10}?\n'.format(name)))
#age = year2-year1
#print('{:$^20},'.format(name),end=' ')
#print('Você tem {:^20} anos!'.format(age))

#FAZER UM SAQUE

#saldo = 500
#saque = float(input('Insira o valor do saque desejado:\n'))
#while saque>saldo:
#    saque = float(input('Saldo insuficiente, insira um novo valor:\n'))
#novosaldo = saldo-saque
#print('Saque realizado com sucesso! Seu novo saldo é {}.'.format(novosaldo))


#BRINCANDO COMCONDIÇÕES
#Diz o nome, idade atrevez do ano e as próximas idades até 2100

#name = input('Olá, qual é o seu nome?\n')
#year1 = int(input('Certo {}, qual o ano em que você nasceu?\n' .format(name)))
#year2 = int(input('Ok {}, agora me diga, em que ano estamos agora?\n' .format(name)))
#age = year2-year1
#if age>=18:
#    print('Uau, você é bem grande {}! '.format(name) + 'Já tem {} anos e é maior de idade!'.format(age))
#else:
#    print('Wow,você ainda é bem jovenm {}! '.format(name) + 'Ainda tem {} anos e é menor de idade!'.format(age))

#print('Veja a seguir suas próximas idades até 2100:')
#contador = 0
#while contador<79: 
#    print(age+contador)
#    contador = contador+1

#BRINCANDO COM LISTAS

#VER O ITEM DE ALGUMA LISTA PELA ORDEM:
#lista_compras = ['banana', 'maça','uva', 'pera', 'melancia', 'morango', 'abacaxi', 'melão', 'laranja']
#print(lista_compras[0])

# -1 = EXIBE O ULTIMO ITEM

# .APPEND ACRESCENTA ALGO NA UKTIMA POSIÇÃO
#lista_compras = ['banana', 'maça','uva', 'pera', 'melancia', 'morango', 'abacaxi', 'melão', 'laranja']
#lista_compras.append('limão')
#print(lista_compras)

# .INSERT ACRESCENTA NA POSIÇÃO DESEJADA
#lista_compras = ['banana', 'maça','uva', 'pera', 'melancia', 'morango', 'abacaxi', 'melão', 'laranja']
#lista_compras.insert(0, 'limão')
#print(lista_compras)

# DEL DELETA NA POSIÇÃO DESEJADA
#lista_compras = ['banana', 'maça','uva', 'pera', 'melancia', 'morango', 'abacaxi', 'melão', 'laranja']
#del lista_compras[1]
#print(lista_compras)

# REMOVE DELETA PELO NOME
#lista_compras = ['banana', 'maça','uva', 'pera', 'melancia', 'morango', 'abacaxi', 'melão', 'laranja']
#lista_compras.remove('abacaxi')
#print(lista_compras)

#PARA O USUARIO INSERIR O VALOR DA LISTA
#lista_tarefas = []
#c=0
#while c<5:
#    tarefa = input('Insira uma tarefa:\n')
#    lista_tarefas.append(tarefa)
#    c=c+1
#print(lista_tarefas)

#BRIMCANDO COM TUPLAS
#Tuplas podem servir como elementos que armazenam outros elementos para uma lista

#cliente1 = ('nick', '15', '000000000')
#cliente2 = ('lua', '18', '111111111')
#cliente3 = ('sol', '12', '222222222')

#clientes = []
#clientes.append(cliente1, cliente2, cliente3)
#print(clientes[0])