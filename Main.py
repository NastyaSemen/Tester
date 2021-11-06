import sys

from PyQt5 import uic
from TestSupplier import TestSupplier
from WarningDialog import WarningDialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLabel
from PyQt5.QtCore import QPoint

class MyWidget(QMainWindow):

    testList = []
    n = 0

    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.testList = TestSupplier().getTestList()
        self.run_test()
        self.next_button.clicked.connect(self.next)
        self.back_button.clicked.connect(self.back)
        self.end_button.setVisible(False)

    def run_test(self):
        self.setWindowTitle('Программа тестирования')
        self.render_test_count()
        self.render_buttons()
        test = self.testList[self.n]
        self.c_label.setText(test.getCaption())
        self.q_label.setText(test.getQuestion())
        self.answer_input.setText(test.getAnswer())

    def render_test_count(self):
        count = str(self.n + 1) + '/' + str(len(self.testList))
        self.count_label.setText(count)

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

    def render_buttons(self):
        if self.n < 1:
            self.back_button.setVisible(False)
        else:
            self.back_button.setVisible(True)
        if self.n + 1 == len(self.testList):
            self.next_button.setVisible(False)
            self.next_button.setEnabled(False)
            self.end_button.setVisible(True)
            self.end_button.setEnabled(True)
            self.end_button.setText('Итог')
            self.end_button.clicked.connect(self.itog)
        else:
            self.next_button.setVisible(True)
            self.next_button.setEnabled(True)
            self.end_button.setVisible(False)
            self.end_button.setEnabled(False)

    def itog(self):
        coords = QPoint(self.mapToGlobal(QPoint(0,0)))
        result = self.render_dialog("Название окна", "Вопрос", coords.x(), coords.y())



    def render_dialog(self, title, answer, x, y):
        dialog = WarningDialog(title, answer, x, y)
        result = dialog.render_dialog()
        print(result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
