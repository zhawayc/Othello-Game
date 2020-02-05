from game_controller import GameController
from board import Board
from disk import Disk


def test_constructor():
    '''Test the constructor of board'''
    gc = GameController(0)
    board = Board(0, 0, gc, 255, 0)
    assert board.BLACK == 0
    assert board.WHITE == 255
    assert board.length == 0
    assert board.number_of_rows == 0
    assert board.gc == gc
    assert board.disks == []
    assert board.TOP_SCORE == board.number_of_rows * 2
    assert board.SECOND_TOP_SCORE == board.number_of_rows
    assert board.DANGEROUS_SCORE == -board.number_of_rows

    gc = GameController(400)
    board = Board(400, 4, gc, 255, 0)
    assert board.BLACK == 0
    assert board.WHITE == 255
    assert board.length == 400
    assert board.number_of_rows == 4
    assert board.interval == 100
    assert board.disks[1][1].color == 255
    assert board.disks[2][2].color == 255
    assert board.disks[1][2].color == 0
    assert board.disks[2][1].color == 0
    assert board.gc == gc
    assert board.tiles_count[255] == 2
    assert board.tiles_count[0] == 2
    assert board.point[0] == 2
    assert board.point[255] == 2
    assert board.points[0][0] == board.TOP_SCORE
    assert board.points[1][0] == board.DANGEROUS_SCORE

    gc = GameController(800)
    board = Board(800, 8, gc, 255, 0)
    assert board.BLACK == 0
    assert board.WHITE == 255
    assert board.length == 800
    assert board.number_of_rows == 8
    assert board.interval == 100
    assert board.disks[3][3].color == 255
    assert board.disks[4][4].color == 255
    assert board.disks[3][4].color == 0
    assert board.disks[4][3].color == 0
    assert board.gc == gc
    assert board.tiles_count[255] == 2
    assert board.tiles_count[0] == 2
    assert board.point[0] == 2
    assert board.point[255] == 2
    assert board.points[0][0] == board.TOP_SCORE
    assert board.points[1][0] == board.DANGEROUS_SCORE
    assert board.points[-1][2] == board.SECOND_TOP_SCORE


def test_generate_disk():
    '''Test the generate disk method'''
    gc = GameController(400)
    board = Board(400, 4, gc, 255, 0)
    board.generate_disk(3, 2, 255)
    assert board.disks[3][2].color == 255
    assert board.disks[3][2].row == 350
    assert board.disks[3][2].col == 250


def test_complete_points():
    '''Test the complete points method'''
    gc = GameController(400)
    board = Board(400, 4, gc, 255, 0)
    board.complete_points()
    assert board.points[0][0] == board.TOP_SCORE
    assert board.points[1][0] == board.DANGEROUS_SCORE


def test_add_tile():
    '''Test the add tile method'''
    gc = GameController(400)
    board = Board(400, 4, gc, 255, 0)
    flip_num = board.add_tile(1, 1, 255)
    assert flip_num == 0
    flip_num = board.add_tile(0, 1, 0)
    assert flip_num == 1


def test_check_if_any_valid():
    '''Test the check if any valid method'''
    gc = GameController(400)
    board = Board(400, 4, gc, 255, 0)
    assert board.check_if_any_valid(0) == True
    board.disks[1][1].color = 0
    board.disks[2][2].color = 0
    assert board.check_if_any_valid(0) == False


def test_check_valid():
    '''Test the check valid method'''
    gc = GameController(400)
    board = Board(400, 4, gc, 255, 0)
    assert board.check_valid(0, 1, 255) == False
    assert board.check_valid(1, 0, 0) == True


def test_flip_over():
    '''Test the flip over method'''
    gc = GameController(400)
    board = Board(400, 4, gc, 255, 0)
    assert board.flip_over(1, 0, 0) == 1
    board.disks[1][1].color = 0
    board.disks[2][2].color = 0
    assert board.flip_over(1, 0, 0) == 0


def test_win_or_lose():
    '''Test the win or lose method'''
    gc = GameController(400)
    board = Board(400, 4, gc, 255, 0)
    board.tiles_count[0] = 8
    board.tiles_count[255] = 8
    board.win_or_lose()
    assert board.gc.equal == True
    board.tiles_count[0] = 10
    board.tiles_count[255] = 6
    board.win_or_lose()
    assert board.gc.black_wins == True
    board.tiles_count[0] = 4
    board.tiles_count[255] = 12
    board.win_or_lose()
    assert board.gc.white_wins == True
