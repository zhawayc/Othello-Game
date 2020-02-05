import copy


class Computer:
    def __init__(self, board, WHITE, BLACK):
        '''Constructor of the computer class'''
        self.MAX_NUM = 9999
        self.DFS_LAYER = 4
        self.WHITE = WHITE
        self.BLACK = BLACK
        self.board = board
        self.tmp_max_black = -self.MAX_NUM

    def dfs(self, i, j, new_board, layer, color):
        '''To minimize the maximum score of black tile, each recursion store
        the potiential highest difference between the black tiles and white
        tiles'''
        if(layer == self.DFS_LAYER):
            if(new_board.point[self.BLACK]-new_board.point[self.WHITE] >
               self.tmp_max_black):
                self.tmp_max_black = new_board.point[self.BLACK] - \
                    new_board.point[self.WHITE]
            return
        flag = 0
        for row in range(new_board.number_of_rows):
            for col in range(new_board.number_of_rows):
                if(new_board.check_valid(row, col, color)):
                    flag = 1
                    tmp_new_board = copy.deepcopy(new_board)
                    tmp_new_board.add_tile(row, col, color)
                    self.dfs(row, col, tmp_new_board, layer+1, self.WHITE-color)
        if(flag == 0):
            tmp_new_board = copy.deepcopy(new_board)
            self.dfs(row, col, tmp_new_board, layer+1, color)

    def computer_go(self):
        '''Get the maximum black score compared to white score from the dfs
        helper function, and compute the lowest highest black score compared
        to white score in this function'''
        max_white = self.MAX_NUM
        final_x = -1
        final_y = -1
        for i in range(self.board.number_of_rows):
            for j in range(self.board.number_of_rows):
                if(self.board.check_valid(i, j, self.WHITE)):
                    new_board = copy.deepcopy(self.board)
                    self.dfs(i, j, new_board, 0, self.BLACK)
                    if(max_white > self.tmp_max_black):
                        max_white = self.tmp_max_black
                        final_x = i
                        final_y = j
                self.tmp_max_black = -self.MAX_NUM
        self.board.add_tile(final_x, final_y, self.WHITE)
