from game_manager import GameManager
from game_controller import GameController
from board import Board
from computer import Computer

def test_constructor():
    '''Test the constructor of game manager'''
    gm=GameManager(100,255,0)
    assert gm.player_turn == True
    assert gm.BLACK == 0
    assert gm.WHITE == 255

def test_computer_make_move():
    '''Test the method of computer make move'''
    gm=GameManager(100,255,0)
    gc=GameController(400)
    board=Board(400,4,gc,255,0)
    cp=Computer(board,255,0)
    gm.player_turn=False
    gm.computer_make_move(board,cp)
    assert board.disks[0][2].color==255

def test_player_make_move():
    '''Test the method of user make move'''
    gm=GameManager(100,255,0)
    gc=GameController(400)
    board=Board(400,4,gc,255,0)
    
    # test a field which is impossible to trigger any flips
    invalid_x=50
    invalid_y=250
    gm.player_make_move(invalid_x,invalid_y,board)
    assert board.disks[0][0]==""

    # test a field which alreadly has a tile on it
    invalid_x=150
    invalid_y=150
    gm.player_make_move(invalid_x,invalid_y,board)
    assert board.disks[0][0]==""

    # test a valid field
    valid_x=350
    valid_y=250
    gm.player_make_move(valid_x,valid_y,board)
    assert board.disks[3][2].color==0

def test_next_move_is_valid():
    '''test the method of next move is valid'''
    gm=GameManager(100,255,0)
    gc=GameController(400)
    board=Board(400,4,gc,255,0)
    assert gm.next_move_is_valid(board)==True 
    board.disks[1][2].color=255
    board.disks[2][1].color=255
    assert gm.next_move_is_valid(board)==False    

    