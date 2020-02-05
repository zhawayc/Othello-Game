from computer import Computer
from game_controller import GameController
from board import Board


def test_constructor():
    '''Test the constructor'''
    gc = GameController(400)
    board = Board(400, 4, gc, 255, 0)
    cp = Computer(board, 255, 0)
    assert cp.MAX_NUM == 9999
    assert cp.WHITE == 255
    assert cp.BLACK == 0
    assert cp.board == board
    assert cp.tmp_max_black == -cp.MAX_NUM


def test_dfs():
    '''Test the dfs helper function'''
    gc = GameController(800)
    board = Board(800, 8, gc, 255, 0)
    cp = Computer(board, 255, 0)
    cp.dfs(2, 4, board, 4, 255)
    assert cp.tmp_max_black == 0


def test_computer_go():
    '''Test the computer go method'''
    gc = GameController(800)
    board = Board(800, 8, gc, 255, 0)
    cp = Computer(board, 255, 0)
    cp.computer_go()
    assert cp.board.disks[2][4].color == cp.WHITE
