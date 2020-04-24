import unittest

from kolkokrzyzyk import TicTacToeGame

class KolkoKrzyzykTest(unittest.TestCase):

    

    def test_stan_planszy(self):
        self.rozmiar_planszy=3
        oczekiwany_stan=['x','x','x']
        sprawdz_plansze=''
        for i in range (0, self.rozmiar_planszy):
            self.stan_planszy[i][0]='x'
            sprawdz_plansze+=self.stan_planszy[i][0]   
        self.assertEqual(oczekiwany_stan, sprawdz_plansze)       

    def test_mozliwy_ruch(self):
        self.rozmiar_planszy=3
        # ruch poza plansza
        i=0
        j=4
        ruch=TicTacToeGame.mozliwy_ruch(self, i, j)
        self.assertFalse(ruch)
        # wpisanie w zajetym miejscu
        k=2
        self.stan_planszy[i][k]='o'
        ruch1=TicTacToeGame.mozliwy_ruch(self, i, k)
        self.assertFalse(ruch1)
        # mozliwy ruch
        l=1
        ruch2=TicTacToeGame.mozliwy_ruch(self, l, k)
        self.assertTrue(ruch2)

    def test_wygrana_rzad(self):
        self.rozmiar_planszy=4
        oczekiwany_rzad='x'
        for i in range (0, self.rozmiar_planszy):
            self.stan_planszy[i][0]='x'
        rzad=TicTacToeGame.koniec_gry(self)
        self.assertEqual(oczekiwany_rzad, rzad) 

    def test_wygrana_kolumna(self):
        self.rozmiar_planszy=4
        oczekiwana_kolumna='o'
        for i in range (0, self.rozmiar_planszy):
            self.stan_planszy[0][i]='o'
        kolumna=TicTacToeGame.koniec_gry(self)
        self.assertEqual(oczekiwana_kolumna, kolumna)

    def test_wygrana_przekatna(self):
        self.rozmiar_planszy=3
        self.stan_planszy=[['x','o','_'],['o','x','_'],['_','_','x']]
        przekatna=TicTacToeGame.koniec_gry(self)
        oczekiwana_przekatna='x'
        self.assertEqual(oczekiwana_przekatna, przekatna)


    def test_wygrana_przekatna_rev(self):
        self.rozmiar_planszy=3
        self.stan_planszy=[['x','o','o'],['x','o','_'],['o','_','x']]
        przekatna_rev=TicTacToeGame.koniec_gry(self)
        oczekiwana_przekatna_rev='o'
        self.assertEqual(oczekiwana_przekatna_rev, przekatna_rev)

    def test_pelna_plansza(self):
        self.rozmiar_planszy=3
        self.stan_planszy=[['o','x','o'],['x','x','o'],['x','o','x']]
        oczekiwany_remis='_'
        remis=TicTacToeGame.koniec_gry(self)
        self.assertEqual(oczekiwany_remis, remis)

    def test_kontynuuj_gre(self):
        self.rozmiar_planszy=3
        self.stan_planszy=[['o','x','_'],['x','x','o'],['x','o','x']]
        puste_pole=None
        pole=TicTacToeGame.koniec_gry(self)
        self.assertEqual(puste_pole, pole)

if __name__=='__main__':
    unittest.main()


            


