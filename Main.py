import sys

from PyQt5 import uic
from TestSupplier import TestSupplier
from WarningDialog import WarningDialog
from IntroDialog import IntroDialog
from Diagram import Diagram
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLabel
from PyQt5.QtCore import QPoint

class MyWidget(QMainWindow):

    testList = []
    r_answer_count= 0
    n = 0

    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.show_intro()
        self.testList = TestSupplier().getTestList()
        self.run_test()
        self.next_button.clicked.connect(self.next)
        self.back_button.clicked.connect(self.back)
        self.end_button.setVisible(False)

    def show_intro(self):
        coords = QPoint(self.mapToGlobal(QPoint(0,0)))
        IntroDialog(coords.x(), coords.y()).render_dialog()
        # TODO Запустить новое окно по аналогии с warning логин пароль ссылка на регистрацию

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
        test = self.testList[self.n]
        test.setAnswer(self.answer_input.toPlainText())
        coords = QPoint(self.mapToGlobal(QPoint(0,0)))
        result = self.render_dialog("Название окна", "Вопрос", coords.x(), coords.y())
        if result:
            self.prepare_itog_widget()

    def prepare_itog_widget(self):
        self.clear_widget()
        self.setWindowTitle('Подведение итога')
        self.q_label.setText('')
        for test in self.testList:
            if test.check():
                self.r_answer_count += 1

        self.show_diagram_button = QPushButton(self)
        self.show_diagram_button.setText('Диаграмма')
        self.show_diagram_button.move(300, 10)
        self.show_diagram_button.resize(100, 30)
        self.show_diagram_button.show()

        self.show_diagram_button.clicked.connect(self.show_diagrama)

        self.result_label = QLabel(self)
        self.result_label.setText('Выполненно правильно - ' + str(self.r_answer_count))
        self.result_label.resize(200, 30)
        self.result_label.move(10, 150)
        self.result_label.show()

        self.end_testing = QPushButton('Завершить тестирование', self)
        self.end_testing.move(200, 250)
        self.end_testing.resize(190, 30)
        self.end_testing.show()

        self.menu_button = QPushButton('Вернуться в меню', self)
        self.menu_button.move(10, 250)
        self.menu_button.resize(150, 30)
        self.menu_button.show()

    def show_diagrama(self):
        if len(self.testList) == self.r_answer_count:
            Diagram().show([self.r_answer_count], ['Правильно'])
        elif self.r_answer_count == 0:
            Diagram().show([len(self.testList)], ['Неверно'])
        else:
            Diagram().show([self.r_answer_count, len(self.testList) - self.r_answer_count])

    def render_dialog(self, title, answer, x, y):
        dialog = WarningDialog(title, answer, x, y)
        result = dialog.render_dialog()
        return result

    def clear_widget(self):
        self.next_button.setVisible(False)
        self.next_button.setEnabled(False)
        self.end_button.setVisible(False)
        self.end_button.setEnabled(False)
        self.count_label.setVisible(False)
        self.count_label.setEnabled(False)
        self.answer_input.setVisible(False)
        self.answer_input.setEnabled(False)
        self.c_label.setVisible(False)
        self.c_label.setEnabled(False)
        self.back_button.setVisible(False)
        self.back_button.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
