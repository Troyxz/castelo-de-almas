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
    pensar duas vezes, willie finca sua lança na parte de baixo de medusa, causando uma 
    dor insuportavel e fazendo ela sangrar até chegar a morte...*''')
    time.sleep(2)
    print('brutal... porem, necessario, todos da mesa ficam em silencio apos o que acabou de acontecer')
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

