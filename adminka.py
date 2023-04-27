import sqlite3

from PyQt5 import QtCore, QtWidgets

from db_data import db_session
from db_data.courses_0 import Courses0
from db_data.courses_1 import Courses1
from db_data.courses_5 import Courses5
from db_data.questions import Questions
from game.game import run_game


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1036, 1300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1101, 1300))
        self.label.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.505382, y1:0.267, x2:0.506, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(248, 255, 247, 255));")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 1011, 71))
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 130, 411, 131))
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 411, 21))
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 300, 411, 191))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 270, 411, 21))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 510, 411, 51))
        self.pushButton.setStyleSheet("background-color: rgba(210, 220, 210, 150);\n"
                                      "border: 1px solid rgba(210, 220, 210, 180);\n"
                                      "border-radius: 10px;\n"
                                      "color: black;\n"
                                      "font-weight: bold;\n"
                                      "font-size: 16px;\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 80, 411, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(430, 400, 601, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(430, 430, 591, 21))
        self.label_7.setObjectName("label_7")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(430, 460, 601, 31))
        self.spinBox.setObjectName("spinBox")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 510, 601, 51))
        self.pushButton_2.setStyleSheet("background-color: rgba(210, 220, 210, 150);\n"
                                        "border: 1px solid rgba(210, 220, 210, 180);\n"
                                        "border-radius: 10px;\n"
                                        "color: black;\n"
                                        "font-weight: bold;\n"
                                        "font-size: 16px;\n"
                                        "")
        self.pushButton_2.setObjectName("pushButton_2")
        self.qs = QtWidgets.QTextBrowser(Form)
        self.qs.setGeometry(QtCore.QRect(430, 130, 601, 261))
        self.qs.setObjectName("listView")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(430, 80, 601, 21))
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

        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)
        self.pushButton_game.clicked.connect(self.start_game)



        self.label_21 = QtWidgets.QLabel(Form)
        self.label_21.setGeometry(QtCore.QRect(10, 570, 1011, 71))
        self.label_21.setObjectName("label_2")
        self.textEdit1 = QtWidgets.QLineEdit(Form)
        self.textEdit1.setGeometry(QtCore.QRect(10, 700, 411, 30))
        self.textEdit1.setObjectName("textEdit")
        self.label_31 = QtWidgets.QLabel(Form)
        self.label_31.setGeometry(QtCore.QRect(10, 670, 411, 21))
        self.label_31.setObjectName("label_3")
        self.textEdit_21 = QtWidgets.QTextEdit(Form)
        self.textEdit_21.setGeometry(QtCore.QRect(10, 770, 411, 191))
        self.textEdit_21.setObjectName("textEdit_2")
        self.label_41 = QtWidgets.QLabel(Form)
        self.label_41.setGeometry(QtCore.QRect(10, 740, 411, 21))
        self.label_41.setObjectName("label_4")

        self.label_91 = QtWidgets.QLabel(Form)
        self.label_91.setGeometry(QtCore.QRect(10, 970, 411, 21))
        self.label_91.setObjectName("label_3")
        self.textEdit31 = QtWidgets.QLineEdit(Form)
        self.textEdit31.setGeometry(QtCore.QRect(10, 1000, 411, 30))
        self.textEdit31.setObjectName("textEdit")

        self.label_111 = QtWidgets.QLabel(Form)
        self.label_111.setGeometry(QtCore.QRect(10, 1030, 601, 21))
        self.label_111.setObjectName("label_8")

        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(10, 1050, 100, 20))
        self.checkBox.setObjectName("textEdit")
        # self.checkBox.stateChanged.connect()

        self.checkBox1 = QtWidgets.QCheckBox(Form)
        self.checkBox1.setGeometry(QtCore.QRect(10, 1070, 100, 20))
        self.checkBox1.setObjectName("textEdit")
        # self.checkBox.stateChanged.connect()

        self.checkBox2 = QtWidgets.QCheckBox(Form)
        self.checkBox2.setGeometry(QtCore.QRect(10, 1090, 100, 20))
        self.checkBox2.setObjectName("textEdit")
        # self.checkBox.stateChanged.connect()

        self.pushButton1 = QtWidgets.QPushButton(Form)
        self.pushButton1.setGeometry(QtCore.QRect(10, 1120, 411, 51))
        self.pushButton1.setStyleSheet("background-color: rgba(210, 220, 210, 150);\n"
                                      "border: 1px solid rgba(210, 220, 210, 180);\n"
                                      "border-radius: 10px;\n"
                                      "color: black;\n" 
                                      "font-weight: bold;\n"
                                      "font-size: 16px;\n"
                                      "")
        self.pushButton1.setObjectName("pushButton")
        self.label_51 = QtWidgets.QLabel(Form)
        self.label_51.setGeometry(QtCore.QRect(10, 650, 411, 21))
        self.label_51.setObjectName("label_5")
        self.label_61 = QtWidgets.QLabel(Form)
        self.label_61.setGeometry(QtCore.QRect(430, 1070, 601, 21))
        self.label_61.setObjectName("label_6")
        self.label_71 = QtWidgets.QLabel(Form)
        self.label_71.setGeometry(QtCore.QRect(430, 1100, 591, 21))
        self.label_71.setObjectName("label_7")
        self.spinBox1 = QtWidgets.QSpinBox(Form)
        self.spinBox1.setGeometry(QtCore.QRect(430, 1130, 601, 31))
        self.spinBox1.setObjectName("spinBox")
        self.pushButton_21 = QtWidgets.QPushButton(Form)

        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")

        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setObjectName("textEdit1")
        self.radioButton.setChecked(True)

        self.radioButton1 = QtWidgets.QRadioButton(Form)
        self.radioButton1.setObjectName("textEdit2")

        self.radioButton2 = QtWidgets.QRadioButton(Form)
        self.radioButton2.setObjectName("textEdit3")

        self.verticalLayout_11.addWidget(self.radioButton)
        self.verticalLayout_11.addWidget(self.radioButton1)
        self.verticalLayout_11.addWidget(self.radioButton2)

        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(430, 700, 601, 90))
        self.widget.setLayout(self.verticalLayout_11)

        self.label_01 = QtWidgets.QLabel(Form)
        self.label_01.setGeometry(QtCore.QRect(430, 680, 601, 21))
        self.label_01.setObjectName("label_8")

        self.pushButton_21.setGeometry(QtCore.QRect(430, 1180, 601, 51))
        self.pushButton_21.setStyleSheet("background-color: rgba(210, 220, 210, 150);\n"
                                        "border: 1px solid rgba(210, 220, 210, 180);\n"
                                        "border-radius: 10px;\n"
                                        "color: black;\n"
                                        "font-weight: bold;\n"
                                        "font-size: 16px;\n"
                                        "")
        self.pushButton_21.setObjectName("pushButton_2")
        self.qs1 = QtWidgets.QTextBrowser(Form)
        self.qs1.setGeometry(QtCore.QRect(430, 800, 601, 261))
        self.qs1.setObjectName("listView")
        self.label_81 = QtWidgets.QLabel(Form)
        self.label_81.setGeometry(QtCore.QRect(430, 650, 601, 21))
        self.label_81.setObjectName("label_8")

        self.radioButton.clicked.connect(self.questions_update1)
        self.radioButton1.clicked.connect(self.questions_update1)
        self.radioButton2.clicked.connect(self.questions_update1)
        self.pushButton1.clicked.connect(self.add1)
        self.pushButton_21.clicked.connect(self.delete1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.questions_update()
        self.questions_update1()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#1a271a;\">Изменение вопросов</span></p></body></html>"))
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


        self.label_21.setText(_translate("Form",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#1a271a;\">Изменение курсов</span></p></body></html>"))
        self.label_31.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#1a271a;\">Название:</span></p></body></html>"))
        self.label_41.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#1a271a;\">Описание:</span></p></body></html>"))
        self.pushButton1.setText(_translate("Form", "Добавить"))
        self.label_51.setText(_translate("Form",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Добавить</span></p></body></html>"))
        self.label_61.setText(_translate("Form",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Удалить</span></p><p align=\"center\"><br/></p></body></html>"))
        self.label_71.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Введите номер курса:</span></p></body></html>"))
        self.pushButton_21.setText(_translate("Form", "Удалить"))
        self.label_81.setText(_translate("Form",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Содержимое базы данных:</span></p></body></html>"))
        self.label_91.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#1a271a;\">Ссылка на курс:</span></p></body></html>"))
        self.radioButton.setText(_translate("Form",
                                        "Дошкольники"))
        self.radioButton1.setText(_translate("Form",
                                        "1-4 классы"))
        self.radioButton2.setText(_translate("Form",
                                        "5-11 классы"))
        self.label_01.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Выберите группу курсов:</span></p></body></html>"))
        self.checkBox.setText(_translate("Form",
                                        "Дошкольники"))
        self.checkBox1.setText(_translate("Form",
                                        "1-4 классы"))
        self.checkBox2.setText(_translate("Form",
                                        "5-11 классы"))
        self.label_111.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Выберите группы курсов:</span></p></body></html>"))

    def add(self):
        db_session.global_init('db_data\questions_and_courses.db')
        db_sess = db_session.create_session()
        qa = Questions()
        conn = sqlite3.connect('db_data\questions_and_courses.db')
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

    def add1(self):
        nums = []
        if self.checkBox.isChecked():
            nums.append('0')
        if self.checkBox1.isChecked():
            nums.append('1')
        if self.checkBox2.isChecked():
            nums.append('5')
        for course_num in nums:
            # pass
            db_session.global_init('db_data\questions_and_courses.db')
            db_sess = db_session.create_session()
            if course_num == '0':
                qa = Courses0()
            elif course_num == '1':
                qa = Courses1()
            else:
                qa = Courses5()
            conn = sqlite3.connect('db_data\questions_and_courses.db')
            cur = conn.cursor()
            qid = cur.execute(f"SELECT * FROM courses{course_num}").fetchall()[-1][0]
            conn.commit()
            conn.close()
            qa.name = self.textEdit1.text()
            qa.description = self.textEdit_21.toPlainText()
            qa.link = self.textEdit31.text()
            qa.id = qid + 1
            db_sess.add(qa)
            db_sess.commit()
        self.textEdit1.setText('')
        self.textEdit_21.setText('')
        self.textEdit31.setText('')
        self.questions_update1()

    def start_game(self):
        run_game()

    def delete(self):
        conn = sqlite3.connect(r'db_data\questions_and_courses.db')
        cur = conn.cursor()
        cur.execute(f"DELETE FROM questions WHERE id = {self.spinBox.value()}")
        conn.commit()
        conn.close()
        self.questions_update()

    def delete1(self):
        conn = sqlite3.connect(r'db_data\questions_and_courses.db')
        cur = conn.cursor()
        if self.radioButton.isChecked():
            course_num = '0'
        elif self.radioButton1.isChecked():
            course_num = '1'
        else:
            course_num = '5'
        cur.execute(f"DELETE FROM courses{course_num} WHERE id = {self.spinBox1.value()}")
        conn.commit()
        conn.close()
        self.questions_update1()

    def questions_update(self):
        conn = sqlite3.connect('db_data/questions_and_courses.db')
        cur = conn.cursor()
        res = cur.execute('SELECT * FROM questions').fetchall()
        t = ''
        for r in res:
            t += str(r[0]) + '. ' + r[1] + '\n' + r[2] + '\n\n'
        self.qs.setText(t)

    def questions_update1(self):
        conn = sqlite3.connect('db_data/questions_and_courses.db')
        cur = conn.cursor()
        if self.radioButton.isChecked():
            course_num = '0'
        elif self.radioButton1.isChecked():
            course_num = '1'
        else:
            course_num = '5'
        res = cur.execute(f'SELECT * FROM courses{course_num}').fetchall()
        t = ''
        for r in res:
            t += str(r[0]) + '. ' + r[1] + '\n' + r[2] + '\n' + r[3] + '\n\n'
        self.qs1.setText(t)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
