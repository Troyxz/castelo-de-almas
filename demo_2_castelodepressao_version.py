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
if (escolha1) == '2':
    print('''
    *a medusa ve sua fraqueza e avança rapidamente em zigzag contra willie, logo, sem 
    pensar duas vezes, willie finca sua lança no estomago de medusa, causando uma 
    dor insuportavel e fazendo ela sangrar até chegar a morte...*''')
    time.sleep(2)
    print('brutal... porem, necessario, todos da mesa ficam em silencio após o que acabou de acontecer')
if (escolha1) == '3':
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
    print(person, 'saiu para investigar, no caminho ele cansa e encontra uma cabana ebandonada, porem a porta estava trancada...')
    print()
    time.sleep(2)
    print('ele ve um tronco de carvalho, decide se deitar para descansar, e acaba dormindo...')
    time.sleep(2)
    for n in range(4):
        time.sleep(3)
        print('...')
        print()
    print(person, 'esta inconciente :(')

if person == 'c':
    person = 'cherry'
    time.sleep(2)
    print(person, 'saiu para investigar, no caminho ela cansa e encontra uma cabana ebandonada, porem a porta estava trancada...')
    print()
    time.sleep(2)
    print('ala ve um tronco de carvalho, decide se deitar para descansar, e acaba dormindo...')
    time.sleep(2)
    for n in range(4):
        time.sleep(3)
        print('...')
        print()
    print(person, 'esta inconciente :(')

if (person) == 'a':
    person = 'amber'
    time.sleep(2)
    print(person,'saiu para investigar, no caminho ela cansa e encontra uma cabana ebandonada, porem a porta estava trancada...')
    print()
    time.sleep(2)
    print('ela ve um tronco de carvalho, decide se deitar para descansar, e acaba dormindo...')
    time.sleep(2)
    for n in range(4):
        time.sleep(3)
        print('...')
        print()
    print(person,'esta inconciente :(')

time.sleep(3)
salvador = 'mikael'

print('\n'
      'em quanto isso, no acampamento, ',salvador,' sentiu falta de',person,'...\n'
      'ele saiu para ver o que estava acontecendo, e ao chegar se deparou com', person, 'inconciente com seus olhos totalmente brancos\n'
      '\n')
print('---------------------------------------------------------------------------------------------------------------------------------------------------------')
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