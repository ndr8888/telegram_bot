import sqlite3

from PyQt5 import QtCore, QtWidgets

from db_data import db_session
from db_data.questions import Questions
from game.game import run_game


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1036, 645)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1101, 771))
        self.label.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.505382, y1:0.267, x2:0.506, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(248, 255, 247, 255));")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 1011, 71))
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 200, 411, 131))
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 411, 21))
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 370, 411, 191))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 340, 411, 21))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 580, 411, 51))
        self.pushButton.setStyleSheet("background-color: rgba(210, 220, 210, 150);\n"
                                      "border: 1px solid rgba(210, 220, 210, 180);\n"
                                      "border-radius: 10px;\n"
                                      "color: black;\n"
                                      "font-weight: bold;\n"
                                      "font-size: 16px;\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 150, 411, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(430, 470, 601, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(430, 500, 591, 21))
        self.label_7.setObjectName("label_7")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(430, 530, 601, 31))
        self.spinBox.setObjectName("spinBox")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 580, 601, 51))
        self.pushButton_2.setStyleSheet("background-color: rgba(210, 220, 210, 150);\n"
                                        "border: 1px solid rgba(210, 220, 210, 180);\n"
                                        "border-radius: 10px;\n"
                                        "color: black;\n"
                                        "font-weight: bold;\n"
                                        "font-size: 16px;\n"
                                        "")
        self.pushButton_2.setObjectName("pushButton_2")
        self.qs = QtWidgets.QTextBrowser(Form)
        self.qs.setGeometry(QtCore.QRect(430, 200, 601, 261))
        self.qs.setObjectName("listView")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(430, 150, 601, 21))
        self.label_8.setObjectName("label_8")

        self.pushButton_game = QtWidgets.QPushButton(Form)
        self.pushButton_game.setGeometry(QtCore.QRect(0, 25, 200, 51))
        self.pushButton_game.setStyleSheet("background-color: rgba(210, 220, 210, 150);\n"
                                           "border: 1px solid rgba(210, 220, 210, 180);\n"
                                           "border-radius: 10px;\n"
                                           "color: black;\n"
                                           "font-weight: bold;\n"
                                           "font-size: 16px;\n"
                                           "")
        self.pushButton_game.setObjectName("pushButton_game")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.questions_update()

        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)
        self.pushButton_game.clicked.connect(self.start_game)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#1a271a;\">Изменение базы данных</span></p></body></html>"))
        self.label_3.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#1a271a;\">Вопрос:</span></p></body></html>"))
        self.label_4.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#1a271a;\">Ответ:</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Добавить"))
        self.label_5.setText(_translate("Form",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Добавить</span></p></body></html>"))
        self.label_6.setText(_translate("Form",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Удалить</span></p><p align=\"center\"><br/></p></body></html>"))
        self.label_7.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Введите номер вопроса:</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "Удалить"))
        self.label_8.setText(_translate("Form",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Содержимое базы данных:</span></p></body></html>"))

        self.pushButton_game.setText(_translate("Form", "игра"))

    def add(self):
        db_session.global_init('db_data/questions.db')
        db_sess = db_session.create_session()
        qa = Questions()
        conn = sqlite3.connect('db_data/questions.db')
        cur = conn.cursor()
        qid = cur.execute("SELECT * FROM questions").fetchall()[-1][0]
        conn.commit()
        conn.close()
        qa.quest = self.textEdit.toPlainText()
        qa.ans = self.textEdit_2.toPlainText()
        qa.id = qid + 1
        db_sess.add(qa)
        db_sess.commit()
        self.textEdit.setText('')
        self.textEdit_2.setText('')
        self.questions_update()

    def start_game(self):
        run_game()

    def delete(self):
        conn = sqlite3.connect(r'db_data\questions.db')
        cur = conn.cursor()
        cur.execute(f"DELETE FROM questions WHERE id = {self.spinBox.value()}")
        conn.commit()
        conn.close()
        self.questions_update()

    def questions_update(self):
        conn = sqlite3.connect('db_data/questions.db')
        cur = conn.cursor()
        res = cur.execute('SELECT * FROM questions').fetchall()
        t = ''
        for r in res:
            t += str(r[0]) + '. ' + r[1] + '\n' + r[2] + '\n\n'
        self.qs.setText(t)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
