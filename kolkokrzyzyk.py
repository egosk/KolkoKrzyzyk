import time


#TO DO :
# 1. poprawka logiki:
# gdzies jest dziura w logice
# po w sytuacji
# o . .
# . x .
# o x x
# komputer zamiast postawic brakujace o i wygrac
# stawia o w srodkowej kolumnie by nie pozwolic graczowi wygrac w kolejnym ruchu
# -- > wydaje mi sie ze juz poprawilam ale jeszcze potestowac trzeba

# 2. dodac walidacje na wejsciach
# plansza musi byc n>=3



class TicTacToeGame:
    rozmiar_planszy = 0
    def __init__(self):
        self.zacznij_gre()

    # pobiera wielkosc planszy i kto zaczyna
    def zacznij_gre(self):
        #TO DO dodac walidacje na wejscie
        self.rozmiar_planszy = int(input('Podaj rozmiar planszy: '))
        self.stan_planszy = []
        for x in range(0, self.rozmiar_planszy):
            self.stan_planszy.append([])
            for y in range(0, self.rozmiar_planszy):
                self.stan_planszy[x].append('_')


        # TO DO dodac walidacje na wejscie
        kolej_gry = input('Czy chcesz wykonac pierwszy ruch (t/n): ')
        if kolej_gry == 't':
            self.kolejka_gracza = 'x'
        elif kolej_gry == 'n':
            self.kolejka_gracza = 'o'

    #rysuje pusta plansze n x n
    def rysuj_plansze(self):
        for i in range(0, self.rozmiar_planszy):
            for j in range(0, self.rozmiar_planszy):
                print('{}|'.format(self.stan_planszy[i][j]), end=" ")
            print()
        print()

    # sprawdza czy ruch jest dozwolony
    def mozliwy_ruch(self, xx, yy):
        # czy nie wychodzimy poza plansze
        if xx < 0 or xx > self.rozmiar_planszy or yy < 0 or yy > self.rozmiar_planszy:
            return False
        # czy pole jest puste
        elif self.stan_planszy[xx][yy] != '_':
            return False
        else:
            return True

    #sprawdza warunki zakonczenia gry
    def koniec_gry(self):
        wygrana_o = 'o' * self.rozmiar_planszy
        wygrana_x = 'x' * self.rozmiar_planszy

        # wygrana w  wierszu
        for i in range (0, self.rozmiar_planszy):
            rzad = ''
            for j in range (0,self.rozmiar_planszy):
                rzad +=(self.stan_planszy[i][j])
            if rzad == wygrana_x or rzad == wygrana_o:
                return self.stan_planszy[i][0]

        # wygrana w kolumnie
        for i in range (0, self.rozmiar_planszy):
            kolumna = ''
            for j in range (0,self.rozmiar_planszy):
                kolumna +=(self.stan_planszy[j][i])
            if kolumna == wygrana_x or kolumna == wygrana_o:
                return self.stan_planszy[0][i]

        # wygrane na diagonali
        przekatna = ''
        for i in range(0, self.rozmiar_planszy):
            przekatna +=(self.stan_planszy[i][i])
            if przekatna == wygrana_x or przekatna == wygrana_o:
                return self.stan_planszy[0][0]

        przekatna_rev = ''
        for i in range(0, self.rozmiar_planszy):
            przekatna_rev += self.stan_planszy[i][self.rozmiar_planszy - 1 - i]
            if przekatna_rev == wygrana_x or przekatna_rev == wygrana_o:
                return self.stan_planszy[0][self.rozmiar_planszy - 1]


        #czy plansza jest pelna
        for i in range(0, self.rozmiar_planszy):
            for j in range(0, self.rozmiar_planszy):
                # Jest puste pole gra nadal trwa
                if (self.stan_planszy[i][j] == '_'):
                    return None

        # Remis
        return '_'


    def max(self, alpha, beta):

        # Możliwe wartości maxv:
        # -1 - przegrana
        # 0  - remis
        # 1  - wygrana

        # najgorszy przypadek
        maxv = -2

        px = None
        py = None

        wynik = self.koniec_gry()

        
        if wynik == 'x':
            return (-1, 0, 0)
        elif wynik == 'o':
            return (1, 0, 0)
        elif wynik == '_':
            return (0, 0, 0)

        for i in range(0, self.rozmiar_planszy):
            for j in range(0, self.rozmiar_planszy):
                if self.stan_planszy[i][j] == '_':
                    # Na pustym polu gracz 'o'wykonuje ruch wywolując Min
                    # To jedna z gałęzi drzewa stanów
                    self.stan_planszy[i][j] = 'o'

                    (m, min_i, min_j) = self.min(alpha, beta)
                    # Poprawa wartości maxv
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    # Pole znowu puste
                    self.stan_planszy[i][j] = '_'

                    if maxv >= beta:
                        return (maxv, px, py)

                    if maxv > alpha:
                        alpha = maxv
        return (maxv, px, py)

    def min(self, alpha, beta):

        # Możliwe wartości minv:
        # -1 - przegrana
        # 0  - remis
        # 1  - wygrana

        # najgorszy przypadek
        minv = 2

        qx = None
        qy = None

        wynik = self.koniec_gry()

        if wynik == 'x':
            return (-1, 0, 0)
        elif wynik == 'o':
            return (1, 0, 0)
        elif wynik == '_':
            return (0, 0, 0)

        for i in range(0, self.rozmiar_planszy):
            for j in range(0, self.rozmiar_planszy):
                if self.stan_planszy[i][j] == '_':
                    self.stan_planszy[i][j] = 'x'
                    (m, max_i, max_j) = self.max(alpha, beta)
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.stan_planszy[i][j] = '_'

                    if minv <= alpha:
                        return (minv, qx, qy)

                    if minv < beta:
                        beta = minv

        return (minv, qx, qy)




    def play(self):

        while True:
            self.rysuj_plansze()
            self.wynik = self.koniec_gry()

            # komunikat ze gra sie skonczyla
            if self.wynik != None:
                if self.wynik == 'x':
                    print('Wygrywa x! Gratulacje!')
                elif self.wynik == 'o':
                    print('Wygrywa o! Powodzenia nastepnym razem.')
                elif self.wynik == '_':
                    print("Remis!")

                # self.zacznij_gre()
                return

            # ruch gracza
            if self.kolejka_gracza == 'x':
                while True:
                    start = time.time()
                    (m, qx, qy) = self.min(-2,2)
                    end = time.time()
                    print('Czas oceny stanu: {}s'.format(round(end - start, 7)))
                    print('Zalecany ruch: X = {}, Y = {}'.format(qx, qy))

                    px = int(input('Wprowadź współrzędną X: '))
                    py = int(input('Wprowadź współrzędną Y: '))

                    (qx, qy) = (px, py)

                    if self.mozliwy_ruch(px, py):
                        self.stan_planszy[px][py] = 'x'
                        self.kolejka_gracza = 'o'
                        break
                    else:
                        print('Niedozwolony ruch! Spróbuj ponownie.')

            # ruch komuptera
            else:

                (m, px, py) = self.max(-2,2)
                self.stan_planszy[px][py] = 'o'
                self.kolejka_gracza = 'x'



g = TicTacToeGame()
g.play()




