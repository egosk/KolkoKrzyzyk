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
    board_size = 0
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        #TO DO dodac walidacje na wejscie
        self.board_size = int(input('Insert Board size: '))
        self.current_state = []
        for x in range(0, self.board_size):
            self.current_state.append([])
            for y in range(0, self.board_size):
                self.current_state[x].append('_')


        # TO DO dodac walidacje na wejscie
        your_turn = input('Do you want to have the first move (y/n): ')
        if your_turn == 'y':
            self.player_turn = 'x'
        elif your_turn == 'n':
            self.player_turn = 'o'

    def draw_board(self):
        for i in range(0, self.board_size):
            for j in range(0, self.board_size):
                print('{}|'.format(self.current_state[i][j]), end=" ")
            print()
        print()

    def is_move_valid(self, xx, yy):
        # czy nie wychodzimy poza plansze
        if xx < 0 or xx > self.board_size or yy < 0 or yy > self.board_size:
            return False
        # czy pole jest puste
        elif self.current_state[xx][yy] != '_':
            return False
        else:
            return True

    def is_game_finished(self):


        winning_configuation_o = 'o' * self.board_size
        winning_configuation_x = 'x' * self.board_size

        # wygrana w  wierszu
        for i in range (0, self.board_size):
            this_row = ''
            for j in range (0,self.board_size):
                this_row +=(self.current_state[i][j])
            if this_row == winning_configuation_x or this_row == winning_configuation_o:
                return self.current_state[i][0]

        # wygrana w kolumnie
        for i in range (0, self.board_size):
            this_column = ''
            for j in range (0,self.board_size):
                this_column +=(self.current_state[j][i])
            if this_column == winning_configuation_x or this_column == winning_configuation_o:
                return self.current_state[0][i]

        #TO DO wygrane na diagonali





        #czy plasnsza jest pelna
        for i in range(0, self.board_size):
            for j in range(0, self.board_size):
                # There's an empty field, we continue the game
                if (self.current_state[i][j] == '_'):
                    return None

        # It's a tie!
        return '_'


    def max(self):

        # Possible values for maxv are:
        # -1 - loss
        # 0  - a tie
        # 1  - win

        # We're initially setting it to -2 as worse than the worst case:
        maxv = -2

        px = None
        py = None

        result = self.is_game_finished()

        # If the game came to an end, the function needs to return
        # the evaluation function of the end. That can be:
        # -1 - loss
        # 0  - a tie
        # 1  - win
        if result == 'x':
            return (-1, 0, 0)
        elif result == 'o':
            return (1, 0, 0)
        elif result == '_':
            return (0, 0, 0)

        for i in range(0, self.board_size):
            for j in range(0, self.board_size):
                if self.current_state[i][j] == '_':
                    # On the empty field player 'O' makes a move and calls Min
                    # That's one branch of the game tree.
                    self.current_state[i][j] = 'o'
                    (m, min_i, min_j) = self.min()
                    # Fixing the maxv value if needed
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    # Setting back the field to empty
                    self.current_state[i][j] = '_'
        return (maxv, px, py)

    def min(self):

        # Possible values for minv are:
        # -1 - win
        # 0  - a tie
        # 1  - loss

        # We're initially setting it to 2 as worse than the worst case:
        minv = 2

        qx = None
        qy = None

        result = self.is_game_finished()

        if result == 'x':
            return (-1, 0, 0)
        elif result == 'o':
            return (1, 0, 0)
        elif result == '_':
            return (0, 0, 0)

        for i in range(0, self.board_size):
            for j in range(0, self.board_size):
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
            self.draw_board()
            self.result = self.is_game_finished()

            # Printing the appropriate message if the game has ended
            if self.result != None:
                if self.result == 'x':
                    print('The winner is X!')
                elif self.result == 'o':
                    print('The winner is O!')
                elif self.result == '_':
                    print("It's a tie!")

                self.initialize_game()
                return

            # If it's player's turn
            if self.player_turn == 'x':

                while True:

                    start = time.time()
                    (m, qx, qy) = self.min()
                    end = time.time()
                    print('Evaluation time: {}s'.format(round(end - start, 7)))
                    print('Recommended move: X = {}, Y = {}'.format(qx, qy))

                    px = int(input('Insert the X coordinate: '))
                    py = int(input('Insert the Y coordinate: '))

                    (qx, qy) = (px, py)

                    if self.is_move_valid(px, py):
                        self.current_state[px][py] = 'x'
                        self.player_turn = 'o'
                        break
                    else:
                        print('The move is not valid! Try again.')

            # If it's AI's turn
            else:
                (m, px, py) = self.max()
                self.current_state[px][py] = 'o'
                self.player_turn = 'x'


        # winning_configuation = 'x' * self.board_size
        # print(winning_configuation)
        #
        # self.is_game_finished()
        # self.current_state[0][2]='x'
        # self.current_state[1][2] = 'x'
        # self.current_state[2][2] = 'x'
        # self.current_state[3][2] = 'x'
        # self.current_state[4][2] = 'x'
        # # self.current_state[3][0] = 'o'
        # # self.current_state[3][1] = 'o'
        # # self.current_state[3][2] = 'o'
        # # self.current_state[3][3] = 'o'
        # # self.current_state[3][4] = 'o'
        # # self.current_state[3][5] = 'o'
        #
        #
        #
        #
        # self.draw_board()
        #
        # print(self.is_game_finished())
        # self.draw_board()
        #
        # px = int(input('Insert the X coordinate: '))
        # py = int(input('Insert the Y coordinate: '))
        #
        # (gx, gy) = (px, py)
        #
        # if self.is_move_valid(px, py):
        #     self.current_state[px][py] = 'x'
        #     self.player_turn = 'o'
        #     #break
        # else:
        #     print ('The move is not valid')
        #
        # self.draw_board()
        #
        # px = int(input('Insert the X coordinate: '))
        # py = int(input('Insert the Y coordinate: '))
        #
        # (gx, gy) = (px, py)
        #
        # if self.is_move_valid(px, py):
        #     self.current_state[px][py] = 'x'
        #     self.player_turn = 'o'
        #     # break
        # else:
        #     print('The move is not valid')
        #
        # self.draw_board()

g = TicTacToeGame()
g.play()


