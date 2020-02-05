import re


class GameController:
    def __init__(self, size):
        '''Constructor of the game controller'''
        self.size = size
        self.white_score = 0
        self.black_score = 0
        self.white_wins = False
        self.black_wins = False
        self.equal = False
        self.complete = False

    def update(self):
        '''Update the scores and results of the game controller'''
        TO_LEFT = 140
        TEXT_FILL = 120
        TEXT_SIZE_RESULT = 50
        TEXT_SIZE_SCORES = 20
        white_message = "White has " + str(self.white_score) + " tiles"
        black_message = "Black has " + str(self.black_score) + " tiles"
        if(self.white_wins or self.black_wins or self.equal):

            if(self.white_wins):
                fill(TEXT_FILL)
                textSize(TEXT_SIZE_RESULT)
                text("WHITE WINS", self.size/2-TO_LEFT, self.size/2)

            elif(self.black_wins):
                fill(TEXT_FILL)
                textSize(TEXT_SIZE_RESULT)
                text("BLACK WINS", self.size/2-TO_LEFT, self.size/2)

            else:
                fill(TEXT_FILL)
                textSize(TEXT_SIZE_RESULT)
                text("SCORE TIED", self.size/2-TO_LEFT, self.size/2)

            textSize(TEXT_SIZE_SCORES)
            text(white_message, self.size/2-TO_LEFT, self.size/2 + TO_LEFT // 2)
            text(black_message, self.size/2-TO_LEFT, self.size/2 + TO_LEFT)
            self.complete = True

    def prompt_input(self):
        '''Prompt the user to input the name'''
        if(self.complete):
            noLoop()
            name = self.input("Enter your name")
            score_file = open("score.txt", "a+")

            if(name):
                input_words = name+"\t"+str(self.black_score)+"\n"
                score_file.seek(0, 0)
                highest_record = score_file.readline().strip()
                if(highest_record):
                    tmp_score = int(re.split("\t", highest_record)[-1])
                    if(tmp_score < self.black_score):
                        score_file.seek(0, 0)
                        content = score_file.read()
                        input_words = input_words+content
                        score_file.seek(0, 0)
                    else:
                        score_file.seek(0, 2)
                else:
                    score_file.seek(0, 2)
                score_file.writelines(input_words)
                score_file.close()

    def input(self, message=""):
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)
