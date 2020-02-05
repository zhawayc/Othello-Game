from disk import Disk
from game_controller import GameController


class Board:
    def __init__(self, length, number_of_rows, gamecontroller, white, black):
        '''The constructor of board class'''
        self.BLACK = black
        self.WHITE = white
        self.length = length
        self.number_of_rows = number_of_rows
        self.TOP_SCORE = self.number_of_rows * 2
        self.SECOND_TOP_SCORE = self.number_of_rows
        self.DANGEROUS_SCORE = - self.number_of_rows
        self.disks = [["" for c in range(self.number_of_rows)]
                      for r in range(self.number_of_rows)]
        if(not self.number_of_rows == 0):
            self.interval = self.length / self.number_of_rows
            self.disks = [["" for c in range(self.number_of_rows)]
                          for r in range(self.number_of_rows)]
            self.generate_disk(self.number_of_rows/2-1,
                               self.number_of_rows/2, self.BLACK)
            self.generate_disk(self.number_of_rows/2,
                               self.number_of_rows/2-1, self.BLACK)
            self.generate_disk(self.number_of_rows/2-1,
                               self.number_of_rows/2-1, self.WHITE)
            self.generate_disk(self.number_of_rows/2,
                               self.number_of_rows/2, self.WHITE)
            self.tiles_count = {self.WHITE: 2, self.BLACK: 2}
            self.point = {self.WHITE: 2, self.BLACK: 2}
            self.points = [
                [1 for i in range(self.number_of_rows)] for j in
                range(self.number_of_rows)]
            self.complete_points()
        self.gc = gamecontroller

    def generate_disk(self, x, y, color):
        '''Generate a disk in the nested list'''
        self.disks[int(x)][int(y)] = Disk(
            x*self.interval+self.interval/2,
            y*self.interval+self.interval/2, color)

    def complete_points(self):
        '''Complete the board of points'''
        self.points[0][0] = self.TOP_SCORE
        self.points[-1][-1] = self.TOP_SCORE
        self.points[-1][0] = self.TOP_SCORE
        self.points[-1][-1] = self.TOP_SCORE

        self.points[1][1] = self.DANGEROUS_SCORE
        self.points[-1][1] = self.DANGEROUS_SCORE
        self.points[-2][-2] = self.DANGEROUS_SCORE
        self.points[1][-1] = self.DANGEROUS_SCORE

        for i in range(1, self.number_of_rows-1):
            if(i == 1 or i == self.number_of_rows-2):
                tmp_score = self.DANGEROUS_SCORE
            else:
                tmp_score = self.SECOND_TOP_SCORE

            self.points[i][0] = tmp_score
            self.points[0][i] = tmp_score
            self.points[-1][i] = tmp_score
            self.points[i][-1] = tmp_score

    def display(self):
        '''Display the board on the screen'''
        STROKE_WEIGHT = 2
        background(0, 120, 0)
        strokeWeight(STROKE_WEIGHT)
        for i in range(1, self.number_of_rows):
            line(0, self.interval * i, self.length, self.interval*i)
            line(self.interval*i, 0, self.interval*i, self.length)
        for r in self.disks:
            for c in r:
                if(not c == ""):
                    c.display()

    def add_tile(self, new_x, new_y, color):
        '''Add a tile to the board'''
        if(not self.check_valid(new_x, new_y, color)):
            return False
        self.generate_disk(new_x, new_y, color)
        self.tiles_count[color] += 1
        self.point[color] += self.points[new_x][new_y]

        tmp_flip = self.flip_over(new_x, new_y, color)
        if(self.tiles_count[self.WHITE]+self.tiles_count[self.BLACK] ==
           self.number_of_rows**2):
            self.win_or_lose()
        return tmp_flip

    def check_if_any_valid(self, color):
        '''Check if there is any legal moves for the player on the board'''
        for i in range(self.number_of_rows):
            for j in range(self.number_of_rows):
                if(self.check_valid(i, j, color)):
                    if(color == self.WHITE):
                        print("Computer's turn!")
                    else:
                        print("Your turn")
                    return True
        return False

    def check_valid(self, x, y, color):
        '''Check if a certain move is a legal one'''
        if(not self.disks[x][y] == ""):
            return False
        dx = [-1, 1, 0, 0, -1, -1, 1, 1]
        dy = [0, 0, -1, 1, -1, 1, 1, -1]
        for i in range(len(dx)):
            new_x = x+dx[i]
            new_y = y+dy[i]
            if(new_x < self.number_of_rows and new_x >= 0 and new_y <
               self.number_of_rows and new_y >= 0 and
               not self.disks[new_x][new_y] == "" and
               self.disks[new_x][new_y].color == self.WHITE-color):
                # if the tile directly next to the tile has a different color
                for j in range(1, self.number_of_rows):
                    # if there is another tile in this row/column/diagnal has
                    # the same color with the tile
                    new_new_x = new_x+dx[i]*j
                    new_new_y = new_y+dy[i]*j
                    if(new_new_x < self.number_of_rows and new_new_x >= 0 and
                       new_new_y < self.number_of_rows and new_new_y >= 0):
                        if(self.disks[new_new_x][new_new_y] == ""):
                            # if there is an empty field, directly break
                            break
                        elif(self.disks[new_new_x][new_new_y].color == color):
                            return True
                    else:
                        # if out of scope, directly break
                        break
        return False

    def flip_over(self, x, y, color):
        '''Flip the relevant tiles after adding a tile to the board'''
        tmp_flip = 0
        dx = [-1, 1, 0, 0, -1, -1, 1, 1]
        dy = [0, 0, -1, 1, -1, 1, 1, -1]
        for i in range(len(dx)):
            new_x = x+dx[i]
            new_y = y+dy[i]
            flag = 0
            if(new_x < self.number_of_rows and new_x >= 0 and new_y <
               self.number_of_rows and new_y >= 0 and
               not self.disks[new_x][new_y] == "" and
               self.disks[new_x][new_y].color == self.WHITE-color):
                # if the tile directly next to the tile has a different color
                for j in range(1, self.number_of_rows):
                    # if there is another tile in this row/column/diagnal 
                    # has the same color with the tile
                    new_new_x = new_x+dx[i]*j
                    new_new_y = new_y+dy[i]*j
                    if(new_new_x < self.number_of_rows and new_new_x >= 0 and
                       new_new_y < self.number_of_rows and new_new_y >= 0):
                        if(self.disks[new_new_x][new_new_y] == ""):
                            # if there is an empty field, directly break
                            break

                        elif(self.disks[new_new_x][new_new_y].color == color):
                            tmp_flip = tmp_flip + \
                                max(abs(new_new_x-new_x), abs(new_new_y-new_y))
                            for k in range(0, j):
                                tmp_new_x = new_x + dx[i]*k
                                tmp_new_y = new_y + dy[i]*k
                                self.disks[tmp_new_x][tmp_new_y].color = color
                                self.tiles_count[self.WHITE-color] -= 1
                                self.point[self.WHITE -
                                           color] -= self.points[tmp_new_x][tmp_new_y]
                                self.point[color] += self.points[tmp_new_x][tmp_new_y]
                                self.tiles_count[color] += 1
                                flag = 1
                            if(flag == 1):
                                break

                    else:
                        # if out of scope, directly break
                        break

        return tmp_flip

    def win_or_lose(self):
        '''Decide whether the player wins or loses'''
        self.gc.white_score = self.tiles_count[self.WHITE]
        self.gc.black_score = self.tiles_count[self.BLACK]
        if(self.tiles_count[self.WHITE] > self.tiles_count[self.BLACK]):
            self.gc.white_wins = True
        elif(self.tiles_count[self.BLACK] > self.tiles_count[self.WHITE]):
            self.gc.black_wins = True
        else:
            self.gc.equal = True
