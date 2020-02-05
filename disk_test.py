from disk import Disk


def test_constructor():
    '''Test the constructor of the disk'''
    d = Disk(2, 1, 0)
    assert d.row == 2
    assert d.col == 1
    assert d.color == 0
