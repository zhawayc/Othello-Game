class Disk:
    def __init__(self, row, col, color):
        '''Constructor of the disk class'''
        self.color = color
        self.row = row
        self.col = col
    
    def display(self):
        '''Display the disk on the screen'''
        SIZE = 90
        fill(self.color)
        ellipse(self.row, self.col, SIZE, SIZE)