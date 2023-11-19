import os
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel


class PasswordDialog(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedWidth(300)
        self.setFixedHeight(100)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.confirm_button = QPushButton("Ok")
        self.confirm_button.clicked.connect(self.check_password)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Sudo Password:"))
        layout.addWidget(self.password_input)
        layout.addWidget(self.confirm_button)

        self.setLayout(layout)

    def check_password(self):
        password = self.password_input.text()

        os.chdir("src")

        command = "sudo python main.py"

        process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE)

        process.stdin.write((password + '\n').encode('utf-8'))
        process.stdin.flush()

        self.close()
        process.wait()

if __name__ == "__main__":
    app = QApplication([])
    dialog = PasswordDialog()
    dialog.show()
    app.exec_()