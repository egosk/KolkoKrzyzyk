import time

# do poprawki:
# gdzies jest dziura w logice
# po w sytuacji
# o . .
# . x .
# o x x
# komputer zamiast postawic brakujace o i wygrac
# stawia o w srodkowej kolumnie by nie pozwolic graczowi wygrac w kolejnym ruchu

# dodatkowo na razie dziala poprawnie tylko jesli zaczyna gracz
# trzeba wprowadzic 'y' gdy komputer pyta czy chcesz zaczac
# czyli kolejna rzecz do poprawki to obsluga tego kto zaczyna gre

#TO DO
# dodac walidacje na wejsciach
# dodac wygrana na diagonali


class TicTacToeGame:
    rozmiar_planszy = 0
    def __init__(self):
        self.zacznij_gre()

    def zacznij_gre(self):
        #TO DO dodac walidacje na wejscie
        self.rozmiar_planszy = int(input('Podaj rozmiar planszy: '))
        self.current_state = []
        for x in range(0, self.rozmiar_planszy):
            self.current_state.append([])
            for y in range(0, self.rozmiar_planszy):
                self.current_state[x].append('_')


        # TO DO dodac walidacje na wejscie
        kolej_gry = input('Czy chcesz wykonac pierwszy ruch (t/n): ')
        if kolej_gry == 't':
            self.kolejka_gracza = 'x'
        elif kolej_gry == 'n':
            self.kolejka_gracza = 'o'

    def rysuj_plansze(self):
        for i in range(0, self.rozmiar_planszy):
            for j in range(0, self.rozmiar_planszy):
                print('{}|'.format(self.current_state[i][j]), end=" ")
            print()
        print()

    def mozliwy_ruch(self, xx, yy):
        # czy nie wychodzimy poza plansze
        if xx < 0 or xx > self.rozmiar_planszy or yy < 0 or yy > self.rozmiar_planszy:
            return False
        # czy pole jest puste
        elif self.current_state[xx][yy] != '_':
            return False
        else:
            return True

    def koniec_gry(self):


        wygrana_o = 'o' * self.rozmiar_planszy
        wygrana_x = 'x' * self.rozmiar_planszy

        # wygrana w  wierszu
        for i in range (0, self.rozmiar_planszy):
            rzad = ''
            for j in range (0,self.rozmiar_planszy):
                rzad +=(self.current_state[i][j])
            if rzad == wygrana_x or rzad == wygrana_o:
                return self.current_state[i][0]

        # wygrana w kolumnie
        for i in range (0, self.rozmiar_planszy):
            kolumna = ''
            for j in range (0,self.rozmiar_planszy):
                kolumna +=(self.current_state[j][i])3
            if kolumna == wygrana_x or kolumna == wygrana_o:
                return self.current_state[0][i]

        #TO DO wygrane na diagonali
        for i in range(0, self.rozmiar_planszy):
            przekatna=''
            przekatna +=(self.current_state[i][i])
        if przekatna == wygrana_x or przekatna == wygrana_o:
            return self.current_state[0][0]

        for i in range(0,self.rozmiar_planszy):
            przekatna_rev=''
            for j in range(self.rozmiar_planszy,0):
                przekatna_rev +=(self.current_state[i][j])        
        if przekatna_rev == wygrana_x or przekatna_rev == wygrana_o:
            return self.current_state[i][j]
                 



        #czy plansza jest pelna
        for i in range(0, self.rozmiar_planszy):
            for j in range(0, self.rozmiar_planszy):
                # Jest puste pole gra nadal trwa
                if (self.current_state[i][j] == '_'):
                    return None

        # Remis
        return '_'


    def max(self):

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
                if self.current_state[i][j] == '_':
                    # Na pustym polu gracz 'o'wykonuje ruch wywolując Min
                    # To jedna z gałęzi drzewa stanów
                    self.current_state[i][j] = 'o'
                    (m, min_i, min_j) = self.min()
                    # Poprawa wartości maxv
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    # Pole znowu puste
                    self.current_state[i][j] = '_'
        return (maxv, px, py)

    def min(self):

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
                if self.current_state[i][j] == '_':
                    self.current_state[i][j] = 'x'
                    (m, max_i, max_j) = self.max()
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.current_state[i][j] = '_'

        return (minv, qx, qy)




    def play(self):
        while True:
            self.rysuj_plansze()
            self.wynik = self.koniec_gry()

            # komunikat ze gra sie skonczyla
            if self.wynik != None:
                if self.wynik == 'x':
                    print('The winner is X!')
                elif self.wynik == 'o':
                    print('The winner is O!')
                elif self.wynik == '_':
                    print("It's a tie!")

                self.zacznij_gre()
                return

            # ruch gracza
            if self.kolejka_gracza == 'x':

                while True:

                    start = time.time()
                    (m, qx, qy) = self.min()
                    end = time.time()
                    print('Czas oceny stanu: {}s'.format(round(end - start, 7)))
                    print('Zalecany ruch: X = {}, Y = {}'.format(qx, qy))

                    px = int(input('Wprowadź współrzędną X: '))
                    py = int(input('Wprowadź współrzędną Y: '))

                    (qx, qy) = (px, py)

                    if self.mozliwy_ruch(px, py):
                        self.current_state[px][py] = 'x'
                        self.kolejka_gracza = 'o'
                        break
                    else:
                        print('Niemożliwy ruch! Spróbuj ponownie.')

            # ruch komuptera
            else:
                (m, px, py) = self.max()
                self.current_state[px][py] = 'o'
                self.kolejka_gracza = 'x'



g = TicTacToeGame()
g.play()


