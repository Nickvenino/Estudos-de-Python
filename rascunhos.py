# SOMA SIMPLES
#n1 = int(input('Digite o primeiro número: '))
#n2 = int(input('Digite o segundo número: '))
#s = n1+n2
#print('A soma é {}!'.format(s))

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
#        # impar + par = impar
#        # par + impar = impar
#        # par + par + par
#        # impar + impar = par
#        # player1 = par - player2 = impar
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
#                print('O resultado da soma é PAR! O ganhador é {}!'.format(player2))
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