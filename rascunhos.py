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

#MEXENDO COM VARIAVEIS
#var1 = 'azul'
#var2 = 'vermelho'
#var3 = 'rosa'
#var4 = 'verde'

#FAZER UM SAQUE

#saldo = 500
#saque = float(input('Insira o valor do saque desejado:\n'))
#while saque>saldo:
#    saque = float(input('Saldo insuficiente, insira um novo valor:\n'))
#novosaldo = saldo-saque
#print('Saque realizado com sucesso! Seu novo saldo é {}.'.format(novosaldo))

#print('A flor é {0}, o carro é {1}, o céu é {2} e a árvore é {3}.'.format(var3,var2,var1,var4))

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