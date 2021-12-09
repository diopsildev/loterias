from random import sample, choice, randint
from time import sleep
from os import system


mes = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
       'Novembro', 'Dezembro')

team = ('SAO PAULO/SP', 'CEARA/CE', 'PALMEIRAS/SP', 'ATHLETICO/PR', 'UBERLANDIA/MG', 'CRICIUMA/SC',
        'RIVER/PI', 'BAHIA/BA', 'RIO BRANCO/AC', 'UNIAO SAO JOAO/SP', 'BOTAFOGO/PB', 'ATLETICO/MG', 'GREMIO/RS',
        'OLARIA/RJ', 'REMO/PA', 'TREZE/PB', 'MARILIA/SP', 'CRB/AL', 'SAO RAIMUNDO/AM', 'CORITIBA/PR',
        'SANTO ANDRE/SP', 'YPIRANGA/AP', 'JI-PARANA/RO', 'SERGIPE/SE', 'GOIAS/GO', 'NACIONAL/AM',
        'XV PIRACICABA/SP', 'VILA NOVA/GO', 'PALMAS/TO', 'PONTE PRETA/SP', 'FIGUEIRENSE/SC', 'FLUMINENSE/RJ',
        'INTERNACIONAL/RS', 'JOINVILLE/SC', 'OPERARIO/MS', 'CRUZEIRO/MG', 'ATLETICO/GO', 'BRASILIENSE/DF',
        'NAUTICO/PE', 'UNIAO BARBARENSE/SP', 'GUARANI/SP', 'TUNA LUSO/PA', 'IPATINGA/MG', 'AVAI/SC',
        'RIO BRANCO/ES', 'JUVENTUS/SP', 'GAMA/DF', 'BRAGANTINO/SP', 'MIXTO/MT', 'BANGU/RJ', 'AMERICA/MG',
        'VILLA NOVA/MG', 'ABC/RN', 'ITUANO/SP', 'DESPORTIVA/ES', 'AMERICA/RN', 'SANTA CRUZ/PE', 'PAYSANDU/PA',
        'FLAMENGO/RJ', 'AMERICA/RJ', 'INTER LIMEIRA/SP', 'SAO CAETANO/SP', 'LONDRINA/PR', 'VASCO/RJ', 'CSA/AL',
        'MOTO CLUBE/MA', 'CORINTHIANS/SP', 'JUVENTUDE/RS', 'AMERICANO/RJ', 'SAMPAIO CORREA/MA', 'PAULISTA/SP',
        'BARUERI/SP', 'SANTOS/SP', 'VITORIA/BA', 'PORTUGUESA/SP', 'FORTALEZA/CE', 'PARANA/PR', 'BOTAFOGO/RJ',
        'RORAIMA/RR', 'SPORT/PE')


print('''1 - Mega-sena
2 - Quina
3 - Lotofácil
4 - Lotomania
5 - Timemania
6 - Dupla Sena
7 - Dia de Sorte
8 - Super Sete
9 - Sair
Escolha sua opção: ''')


n1: int = int(input())

if n1 == 1:
    a = list(range(1, 61))
    print(sorted(sample(a, 6)))
    sleep(2)

elif n1 == 2:
    b = list(range(1, 81))
    print(sorted(sample(b, 5)))
    sleep(2)

elif n1 == 3:
    c = list(range(1, 26))
    print(sorted(sample(c, 15)))
    sleep(2)

elif n1 == 4:
    d = list(range(0, 100))
    print(sorted(sample(d, 50)))
    sleep(2)

elif n1 == 5:
    e = list(range(1, 81))
    print(sorted(sample(e, 10)))
    print(choice(team))
    sleep(2)

elif n1 == 6:
    f = list(range(1, 51))
    print(sorted(sample(f, 6)))
    print(sorted(sample(f, 6)))
    sleep(2)

elif n1 == 7:
    g = list(range(1, 32))
    print(sorted(sample(g, 7)))
    print(choice(mes))
    sleep(2)

elif n1 == 8:
    h = []
    for i in range(7):
        h.append(randint(0, 10))
    print(h)
    sleep(2)

elif n1 == 9:
    print('Até logo!')
    sleep(2)
    exit(0)

else:
    print('Essa não é uma opção válida!')
    sleep(5)

system("python main.py")
exit()
