from game_controller import GameController

def test_constructor():
    '''Test the constructor of the game controller'''
    gc= GameController(400)
    assert gc.size == 400
    assert gc.white_score == 0
    assert gc.black_score == 0
    assert gc.white_wins == False
    assert gc.black_wins == False
    assert gc.equal == False
    assert gc.complete == False