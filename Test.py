class Test:
    caption = ''
    question = ''
    answer = ''
    rAnswer = ''

    def __init__(self, caption, question, rAnswer):
        self.caption = caption
        self.question = question
        self.rAnswer = rAnswer

    def getCaption(self):
        return self.caption

    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return self.answer

    def setAnswer(self, answer):
        self.answer = answer

    def check(self):
        return self.answer == self.rAnswer
