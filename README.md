# KolkoKrzyzyk
Tic-tac-toe game (for n-size board) implemented with alfa-beta pruning algorithm. Project conducted for Artificial Inteligence Fundamentals course at WUT.



Podstawy sztucznej inteligencji – przeszukiwanie

Gosk Emilia, Naumiuk Agnieszka

Temat MM.GD3 Gra w Kółko i Krzyżyk


1. Treść zadania
Wykorzystując algorytm min-max i odcinanie alfa-beta zaprojektować i zaimplementować algorytm
umożliwiający rozegranie gry w Kółko i Krzyżyk. Działanie algorytmu należy zaprezentować w formie
prostej interaktywnej aplikacji graficznej/konsolowej umożliwiającej rozegranie gry zgodnie z jej
regułami przeciwko komputerowi. WE: kto rozpoczyna grę, rozmiar planszy N (n >= 3), maksymalna
głębokość przeszukiwania przestrzeni stanów. WY: prosty interfejs gry.


2. Przyjęte założenia

• Gracz – X, komputer - O

• Puste pole na planszy ‘_’

• Ruch możliwy na pustym polu w zakresie planszy – ograniczenia

• 4 możliwości zakończenia: wygrana w wierszu, wygrana w kolumnie, wygrana na
przekątnej, remis

• Gracz X dąży do maksimum, gracz O dąży do minimum

• Zapisywany i podawany jest czas oceny stanu i wyboru najlepszego kroku


3. Opis algorytmu

Algorytm został napisany w języku Python jako jedna klasa wraz z metodami. Metody te
służą:

• Inicjalizacji gry (stworzeniu pustej planszy oraz wyborze rozpoczynającego gracza)

• Wyświetlaniu planszy w konsoli,

• Sprawdzaniu poprawności przebiegu kolejki gracza X (poprawny ruch)

• Sprawdzaniu warunków zakończenia gry (remis lub wygrana jednego z graczy)

• Korzystając z algorytmu min-max z przycinaniem alfa-beta proponowaniu
najlepszego ruchu graczowi X oraz zagraniu gracza O


4. Instrukcja użytkownika

• Po rozpoczęciu gry zgodnie z wyświetlonymi na konsoli informacjami należy
wprowadzić rozmiar planszy (nie mniejszy niż 3) oraz zdecydować czy chce się
wykonać pierwszy ruch

• Następnie algorytm ocenia stan planszy i proponuje najlepszy krok dla danego gracza

• Należy wprowadzić współrzędną X (kolumna) oraz Y(wiersz) odpowiadające pustemu
polu na planszy

• Jeśli wystąpią warunki końca gry – wygrana, przegrana, remis – zostaną spełnione gra
kończy się i wyświetla się odpowiedni komunikat
