import sys

from PyQt5 import uic
from TestSupplier import TestSupplier
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):

    testList = []
    n = 0

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Программа тестирования')
        uic.loadUi('main.ui', self)
        self.testList = TestSupplier().getTestList()
        self.run_test()
        self.next_button.clicked.connect(self.next)
        self.back_button.clicked.connect(self.back)


    def run_test(self):
        #TODO скрыть кнопки
        test = self.testList[self.n]
        self.c_label.setText(test.getCaption())
        self.q_label.setText(test.getQuestion())
        self.answer_input.setText(test.getAnswer())
        #TODO отобразить номер теста 1 из 2


    def next(self):
        test = self.testList[self.n]
        test.setAnswer(self.answer_input.toPlainText())
        self.n += 1
        self.run_test()

    def back(self):
        test = self.testList[self.n]
        test.setAnswer(self.answer_input.toPlainText())
        if self.n != 0:
            self.n -= 1
        self.run_test()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
