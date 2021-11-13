import logging
import logging.config
import yaml
import math
import random

with open('logger.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
logger = logging.getLogger(__name__)

win_logger = logging.getLogger(__name__)
f_handler = logging.FileHandler("wins.log")
f_handler.setLevel(logging.WARNING)
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)
win_logger.addHandler(f_handler)


class Menu:
    def __init__(self):
        self.choice = input("Hello, what do you want to do next? "
                            "\n 1 - play tic-tac-toe, 2 - see wins log, 3 - clear wins log, 4 - quit game \n")
        Menu.do_choice(self)

    def do_choice(self):
        if self.choice == "1":
            play(t, x_player, o_player)
            Menu()
        elif self.choice == "2":
            with open("wins.log") as w:
                lines = w.read()
                print(lines)
            Menu()
        elif self.choice == "3":
            with open('wins.log', 'w') as w:
                w.truncate(0)
            Menu()
        elif self.choice == "4":
            logger.info("Goodbye, have a nice day!")
            exit()
        else:
            logger.error("Wrong input try numbers from 1 to 4")
            Menu()


class Player:
    def __init__(self, letter, name: str):
        self.letter = letter
        self.name = name

    def next_move(self, game):
        pass


class ComputerRandomPlayer(Player):
    def __init__(self, letter, name):
        super().__init__(letter, name)
        logger.info(f"Random Computer Player {name} is playing {letter}")

    def next_move(self, game):
        square = random.choice(game.available_moves())
        logger.info(f"Computer Player {self.name} chooses to put {self.letter} to {square} square")
        return square


class UserPlayer(Player):
    def __init__(self, letter, name):
        super().__init__(letter, name)
        logger.info(f"User Player {name} is playing {letter}")

    def next_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(f"Player's {self.name} with {self.letter} move. Input (0-8) to make a move:")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                logger.error("Invalid square, try again.")
        return val


class TicTacToe:

    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_winner = None
        logger.info(f"The game board is initialized, current winner is {self.current_winner}")

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")
        logger.info("The board is printed.")

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")
        logger.info("The squares in the board are enumerated.")

    def available_moves(self):
        moves = []
        for (i, space) in enumerate(self.board):
            if space == " ":
                moves.append(i)
        logger.info(f"List of available moves is {moves}")
        return moves

    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(" ")

    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind * 3: (row_ind + 1) * 3]
        if all([space == letter for space in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([space == letter for space in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([space == letter for space in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([space == letter for space in diagonal2]):
                return True
        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
    letter = "X"
    while game.empty_squares():
        if letter == "O":
            square = o_player.next_move(game)
            current_player = o_player
        else:
            square = x_player.next_move(game)
            current_player = x_player
        if game.make_move(square, letter):
            if print_game:
                logger.info(f"{current_player.name} makes a move with {letter} to {square}")
                game.print_board()
                print("")
            if game.current_winner:
                if print_game:
                    logger.warning(f"{current_player.name} with {letter} wins!")
                    win_logger.warning(f"{current_player.name} with {letter} wins!")
                return letter
            letter = "O" if letter == "X" else "X"
    if print_game:
        logger.warning(f"It's a tie between {x_player.name} and {o_player.name}!")
        win_logger.warning(f"It's a tie between {x_player.name} and {o_player.name}!")



if __name__ == "__main__":
    x_player = UserPlayer("X", "Peter")
    o_player = ComputerRandomPlayer("O", "LilyComputer")
    t = TicTacToe()
    menu = Menu()
    menu.do_choice()

