from PyQt5.QtWidgets import QDialog, QPushButton, QLabel

class WarningDialog:

    title = ''
    answer = ''
    x = 0
    y = 0
    result = False
    dialog = None

    def __init__(self, title, answer, x, y):
        self.title = title
        self.answer = answer
        self.x = x
        self.y = y

    def render_dialog(self):
        dialog = QDialog()
        self.dialog = dialog
        dialog.setGeometry(self.x + 52.5, self.y + 75, 300, 100)
        dialog.setWindowTitle(self.title)
        dialog.ok_button = QPushButton('OK', dialog)
        dialog.ok_button.move(120, 60)
        dialog.cancel_button = QPushButton('Cancel', dialog)
        dialog.cancel_button.move(200, 60)
        dialog.label = QLabel(dialog)
        dialog.label.setText(self.answer)
        dialog.label.move(30, 20)

        dialog.ok_button.clicked.connect(self.ok)
        dialog.cancel_button.clicked.connect(self.cancel)
        dialog.exec()
        return self.result

    def ok(self):
        self.result = True
        self.dialog.close()

    def cancel(self):
        self.result = False
        self.dialog.close()
