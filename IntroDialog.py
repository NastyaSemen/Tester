from PyQt5.QtWidgets import QDialog, QPushButton, QLabel, QLineEdit
from Registration import Registration
from PyQt5.QtCore import QPoint
import psycopg2
from userdata.UserDataSupplier import UserDataSupplier

class IntroDialog:

    x = 0
    y = 0
    result = False
    dialog = None
    user_data = None

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

        dialog.info = QLabel(dialog)
        dialog.info.setText('Информация о пароле')
        dialog.info.move(10, 80)
        dialog.info.resize(200, 100)

        dialog.enter_next = QPushButton('Вход', dialog)
        dialog.enter_next.move(200, 200)
        dialog.enter_next.clicked.connect(self.check_password)

        dialog.sign_up = QPushButton('Регистрация', dialog)
        dialog.sign_up.move(10, 200)
        dialog.sign_up.resize(130, 25)
        dialog.sign_up.clicked.connect(self.sign_up)
        dialog.exec()
        return self.user_data

    def check_password(self):
        login = self.dialog.login_input.text()
        psw = self.dialog.password_input.text()
        result = UserDataSupplier().get_user_data(login, psw)
        if result[0]:
            self.dialog.info.setText('')
            self.user_data = result[0]
            self.dialog.close()
        else:
            self.render_error(result[1])

    def render_error(self, error_text):
        self.dialog.info.setText(error_text)


    def sign_up(self):
        coords = QPoint(self.dialog.mapToGlobal(QPoint(0,0)))
        Registration(coords.x(), coords.y()).render_dialog()

