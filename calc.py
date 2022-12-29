def materias():
    print('')
    print('{} qual materia você gostaria de calcular suas notas?'.format(nome))
    print('1) Português')
    print('2) Matemática')
    print('3) Geografia')
    print('4) História')

def calculos():
    print('Nota primeiro bimestre')
    n1 = float(input('>'))
    print('Nota segundo bimestre')
    n2 = float(input('>'))
    print('Nota terceiro bimestre')
    n3 = float(input('>'))
    print('Nota quarto bimestre')
    n4 = float(input('>'))
    notas = (n1+n2+n3+n4)
    med = notas/4
    necessario = 5 - med
    if med < 5:
        print('{} infelizmente você reprovou, sua nota foi {} e você necessita de {} pontos para ser aprovado.'.format(nome, med, necessario))
    else:
        print('Parabéns {}, você foi aprovado. Sua nota foi {}'.format(nome, med))
    print('Deseja ver sua nota em outra matéria?')

r = 'S'

print('Qual é seu nome?')
nome = input('> ')
while r == 'S':
    materias()
    escolhamenu = int(input('> '))
    if escolhamenu == 1:
        print('Você escolheu Português')
        calculos()
        tentardenovo = input('> ').upper().strip()[0]
    elif escolhamenu == 2:
        print('Você escolheu Matemática')
        calculos()
        tentardenovo = input('> ').upper().strip()[0]
    elif escolhamenu == 3:
        print('Você escolheu Geografia')
        calculos()
        tentardenovo = input('> ').upper().strip()[0]
    elif escolhamenu == 4:
        print('Você escolheu História')
        calculos()
        tentardenovo = input('> ').upper().strip()[0]
    else:
        print('Escolha inválida!')