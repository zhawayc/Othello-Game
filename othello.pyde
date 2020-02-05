from board import Board
from game_controller import GameController
from game_manager import GameManager
from computer import Computer

NUMBER_OF_ROWS = 8
CELL_SIZE = 100
LENGTH = NUMBER_OF_ROWS * CELL_SIZE
BLACK = 0
WHITE = 255
cur_color = BLACK

gamecontroller = GameController(LENGTH)
gamemanager = GameManager(CELL_SIZE, WHITE, BLACK)
board = Board(LENGTH, NUMBER_OF_ROWS, gamecontroller, WHITE, BLACK)
computer = Computer(board,255,0)

def setup():
    size(LENGTH,LENGTH)

def draw():
    gamecontroller.prompt_input()
    gamemanager.computer_make_move(board,computer)
    board.display()
    gamecontroller.update()

def mousePressed():   
    gamemanager.player_make_move(mouseX,mouseY,board)
    board.display()
    
