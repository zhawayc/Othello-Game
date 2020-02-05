import time


class GameManager:
    def __init__(self, cell_size, white, black):
        '''Constructor of the game manager'''
        self.player_turn = True
        self.CELL_SIZE = cell_size
        self.BLACK = black
        self.WHITE = white

    def computer_make_move(self, board, computer):
        '''decide whether it is the computer's turn and let the computer
        move a tile'''
        if(not self.player_turn):
            computer.computer_go()
            time.sleep(0.5)
            if(not self.next_move_is_valid(board)):
                if(not self.next_move_is_valid(board)):
                    board.win_or_lose()

    def player_make_move(self, x, y, board):
        '''decide whether it is the player's turn and let the player
        move a tile'''
        x = x//self.CELL_SIZE
        y = y//self.CELL_SIZE
        if(self.player_turn):
            if(not (board.add_tile(x, y, self.BLACK))):
                return
            if(not self.next_move_is_valid(board)):
                if(not self.next_move_is_valid(board)):
                    board.win_or_lose()

    def next_move_is_valid(self, board):
        '''Decide whether the next player has any valid moves'''
        self.player_turn = not self.player_turn
        if(self.player_turn):
            color = self.BLACK
        else:
            color = self.WHITE

        if(not board.check_if_any_valid(color)):
            return False

        return True
