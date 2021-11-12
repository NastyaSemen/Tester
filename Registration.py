from PyQt5.QtWidgets import QDialog, QPushButton, QLabel, QLineEdit

class Registration:

    x = 0
    y = 0
    result = False
    dialog = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def render_dialog(self):
        dialog = QDialog()
        self.dialog = dialog
        dialog.setGeometry(self.x, self.y, 300, 250)
        dialog.setWindowTitle('')

        dialog.login = QLabel(dialog)
        dialog.login.setText('Логин:')
        dialog.login.move(10, 20)

        dialog.password = QLabel(dialog)
        dialog.password.setText('Пароль:')
        dialog.password.move(10, 50)

        dialog.login_input = QLineEdit(dialog)
        dialog.login_input.move(80, 20)

        dialog.password_input = QLineEdit(dialog)
        dialog.password_input.move(80, 50)

        dialog.first_name = QLabel(dialog)
        dialog.first_name.setText('Имя:')
        dialog.first_name.move(10, 80)

        dialog.second_name = QLabel(dialog)
        dialog.second_name.setText('Фамилия:')
        dialog.second_name.move(10, 110)

        dialog.first_name_input = QLineEdit(dialog)
        dialog.first_name_input.move(80, 80)

        dialog.second_name_input = QLineEdit(dialog)
        dialog.second_name_input.move(80, 110)

        dialog.info = QLabel(dialog)
        dialog.info.setText('Информация о пароле')
        dialog.info.move(10, 130)
        dialog.info.resize(200, 50)

        dialog.enter_signup = QPushButton('Зарегистрироваться', dialog)
        dialog.enter_signup.move(140, 200)
        dialog.enter_signup.resize(160,25)

        dialog.enter_back = QPushButton('Назад', dialog)
        dialog.enter_back.move(10, 200)


        #dialog.ok_button.clicked.connect(self.ok)
        #dialog.cancel_button.clicked.connect(self.cancel)
        dialog.exec()
        return self.result
