import time

print('''
SITUAÇÃO..

     Você e tres amigos estariam em uma floresta, bem longe de tudo
    que se meche, apenas algumas larvas procurando carniça para se
    alimentarem e se aproveitarem estavam por perto.

     Você e seus amigos moram em seneka, uma pequena cidade nos
    estados unidos, estavam jogando um jogo de cartas, chamado portão de alma[...] 
''')

time.sleep(5)

print()
print('''
- vai, mata a medusa willie!'
    disse mikael, se referindo ao jogo em quanto puxava uma carta de seu deck;

    o que willie faz?...
''')

time.sleep(2)

print('''
[1] - jogar uma carta pra garantir uma vida extra
[2] - atacar a medusa e que vença o melhor
[3] - recuar e desistir da batalha 
''')

time.sleep(2)

escolha1 = input('sua escolha =')

if (escolha1) == '1':
    print('*você não se protege do golpe da medusa, mas se salva e arranca sua cabeça na primeira chance que tem*')
    time.sleep(1)
    print('wow, que estrategia incrivel, parabens willie!')
elif (escolha1) == '2':
    print('''
    *a medusa ve sua fraqueza e avança rapidamente em zigzag contra willie, logo, sem 
    pensar duas vezes, willie finca sua lança no estomago de medusa, causando uma 
    dor insuportavel e fazendo ela sangrar até chegar a morte...*''')
    time.sleep(2)
    print('brutal... porem, necessario, todos da mesa ficam em silencio após o que acabou de acontecer')
elif (escolha1) == '3':
    print('oh... okay, adeus ;)')
    time.sleep(2)
    print('''
    desligando

    …………$$……………………………………..$$…………
    …………$$……………………………………..$$…………
    …………..$$s………………………………s$$…………..
    …………….$$$$……………………….$$$$…………….
    ………………³$$$$..¶¶¶¶¶¶¶¶..$$$$³………………
    ………………..³$$$$..¶¶¶¶¶¶..$$$$³………………..
    ………………¶..$$$$$..¶¶¶¶..$$$$$..¶………………
    …………….¶¶¶..$$$..¶¶¶¶¶¶..$$$..¶¶………………
    …………….¶¶¶….¶¶¶¶¶¶¶¶¶¶….¶¶¶¶………………
    …………….¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶………………
    ………………..¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶………………..
    ………………..¶¶……..¶¶¶¶……….¶……………………
    ………………..¶¶……..¶¶¶¶……….¶¶………………….
    ………………..¶¶¶¶¶¶¶¶..¶¶¶¶¶¶¶¶………………….
    ………………….¶¶¶¶¶¶……¶¶¶¶¶¶¶………………….
    ……………………….¶¶¶¶¶¶¶¶¶…………………………
    ……………………….¶..¶..¶..¶..¶…………………………
    …………¶…………..¶…………..¶…………..¶…………..
    ……….¶¶……………………………………….¶¶…………
    ……….¶¶……………………………………….¶¶…………
    ……….¶¶…………..¶¶……….¶¶…………..¶¶…………
    ……….¶¶..¶¶..¶¶..¶…………..¶..¶¶..¶¶..¶¶…………
    ……¶..¶¶..¶¶..¶¶..¶…………..¶..¶¶..¶¶..¶¶..¶……..
    ….¶¶..¶¶..¶¶..¶¶..¶…………..¶..¶¶..¶¶..¶¶..¶¶……
    ……¶¶¶¶..¶¶..¶¶………………….¶¶..¶¶..¶¶¶¶……..
    ''')
    exit()
else:
    exit()

print('\n'
      'você ouve um barulho de disparo na floresta...\n'
      '\n'
      'quem você decide enviar pra investigar?\n'
      '\n')

time.sleep(2)

print('''
[w] - willie
[a] - amber
[c] - cherry
''')

person = input('sua escolha =')

if (person) == 'w':
    person = 'willie'
    time.sleep(2)
    print(person,
          'saiu para investigar, no caminho ele cansa e encontra uma cabana ebandonada, porem a porta estava trancada...')
    print()
    time.sleep(2)
    print('ele ve um tronco de carvalho, decide se deitar para descansar, e acaba dormindo...')
    time.sleep(2)
    for n in range(4):
        time.sleep(3)
        print('...')
        print()
    print(person, 'esta inconciente :(')

elif person == 'c':
    person = 'cherry'
    time.sleep(2)
    print(person,
          'saiu para investigar, no caminho ela cansa e encontra uma cabana ebandonada, porem a porta estava trancada...')
    print()
    time.sleep(2)
    print('ala ve um tronco de carvalho, decide se deitar para descansar, e acaba dormindo...')
    time.sleep(2)
    for n in range(4):
        time.sleep(3)
        print('...')
        print()
    print(person, 'esta inconciente :(')

elif (person) == 'a':
    person = 'amber'
    time.sleep(2)
    print(person,
          'saiu para investigar, no caminho ela cansa e encontra uma cabana ebandonada, porem a porta estava trancada...')
    print()
    time.sleep(2)
    print('ela ve um tronco de carvalho, decide se deitar para descansar, e acaba dormindo...')
    time.sleep(2)
    for n in range(4):
        time.sleep(3)
        print('...')
        print()
    print(person, 'esta inconciente :(')
else:
    exit()

time.sleep(3)
salvador = 'mikael'

print('\n'
      'em quanto isso, no acampamento, ', salvador, ' sentiu falta de', person, '...\n'
                                                                                'ele saiu para ver o que estava acontecendo, e ao chegar se deparou com',
      person, 'inconciente com seus olhos totalmente brancos\n'
              '\n')
print(
    '---------------------------------------------------------------------------------------------------------------------------------------------------------')
time.sleep(3)

print(salvador, 'precisa entrar na cabana, o que preende fazer?\n'
                '\n'
                '\n'
                '...\n')

time.sleep(3)

print('''
[1] - olhar no galpão
[2] - olhar nas moitas
[3] - dar um soco na porta
''')

escolha2 = input('sua escolha =')

if (escolha2) == 'theo':
    print('você invocou o deus do s3xo >:3')
    print('''
    ele aparece, da uma sarrada bem gostosa
    na porta da cabana, após isso ele apenas some
    dizendo:
    - passa o zarpe gostosa
    ''')

elif (escolha2) == '1':
    print(salvador,
          'abre o galpão, e se depara com baldes de gordura animal, carne seca, uma faca de açougueiro coberta de sangue e um pé de cabra')
    time.sleep(2)
    print(salvador, ':hmmmmm otimo local pra um assassinato igual naqueles jogos de terror')
    time.sleep(2)
    print()
    print(
        '---------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(salvador, 'pega o pé de cabra e a faca de açougueiro colocando em sua mochila')
    print('espaço da mochila: 3/5')

elif (escolha2) == '2':
    print(salvador,
          'se da de cara com uma cobra, ela te morde e agora esta com o status envenenado! busque um antidoto durante a jogatina, ou acabara perdendo',
          salvador)
    print('''
    envenenado = p
    sangrando = b
    queimando = f
    ''')
    time.sleep(2)
    print()
    print('-aw, minha mão doi muito!')
    salvador = 'mikael(🌢p)'
    time.sleep(2)
    print('')
    print(salvador,
          'abre o galpão, e se depara com baldes de gordura animal, carne seca, uma faca de açougueiro coberta de sangue e um pé de cabra')
    time.sleep(2)
    print(salvador, ':hmmmmm otimo local pra um assassinato igual naqueles jogos de terror')
    time.sleep(2)
    print()
    print(
        '---------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(salvador, 'pega o pé de cabra e a faca de açougueiro colocando em sua mochila')
    print('espaço da mochila: 3/5')

elif (escolha2) == '3':
    print('você da um soco na porta, consegue quebra-la, mas ganha algumas feridas na mão... desnecessario, não acha?')

else:
    exit()
print(salvador, 'coloca o corpo de', person, 'para dentro da cabana, em busca de um lugar mais seguro')
time.sleep(3)
print('''ao entrar na cabana, daria pra echergar uma luz forte, em um clima 
tenso em um silencio gritante, da pra sentir o cheiro forte de sangue no
local, a luz, vem de uma brecha na cortina, não traz uma sensação boa para
os dois, decide investigar?

s/n = sim/não''')
time.sleep(2)
print()
escolha3 = input('sua escolha =')
time.sleep(2)

print('\n'
      '\n'
      '\n'
      '\n')
time.sleep(2)
if (escolha3) == 's':
    print(salvador, 'se aproxima da cortina, com sua faca de açougueiro em uma mão, e sua laterna em outra...')
    time.sleep(2)
    print('ele sente seu suor frio escorrer, sua ansiedade aumenta e ele tem fortes palpitações de imediato...')
    time.sleep(2)
    print('a sensação é horrivel, ele ve que em algo de errado e imediatamente recua :(')
elif(escolha3) == 'n':
    print('você apenas desiste de olhar oque em de errado com aquela cortina :)')
else:
    for n in range(10):
        time.sleep(0.5)
        print('''
        #####################################
         por favor, leve essse jogo a sério.
        #####################################
        ''')
        print()
    exit()


