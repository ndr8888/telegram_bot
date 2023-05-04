import sqlite3

from PyQt5 import QtCore, QtWidgets

from db_data import db_session
from db_data.courses_0 import Courses0
from db_data.courses_1 import Courses1
from db_data.courses_5 import Courses5
from db_data.questions import Questions
from game.game import run_game

import paramiko
import os

host = '188.120.250.240'
user = 'root'
password = '8e6KfyEzVfFO'
port = 22
remotepath = '/project/telegram_bot/telegram_bot_for_Bytic/db_data/questions_and_courses.db'
localpath = os.getcwd() + '/db_data/questions_and_courses.db'


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1034, 634)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1041, 651))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(-10, -50, 1101, 771))
        self.label.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.505382, y1:0.267, x2:0.506, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(248, 255, 247, 255));")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1031, 71))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(10, 120, 411, 31))
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(430, 120, 591, 31))
        self.label_8.setObjectName("label_8")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(10, 180, 411, 131))
        self.textEdit.setObjectName("textEdit")
        self.qs = QtWidgets.QTextBrowser(self.tab)
        self.qs.setGeometry(QtCore.QRect(430, 180, 591, 261))
        self.qs.setObjectName("qs")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 411, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(10, 320, 411, 21))
        self.label_4.setObjectName("label_4")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 350, 411, 191))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(10, 550, 411, 51))
        self.pushButton.setStyleSheet("background-color: rgba(210, 220, 210, 150);\n"
                                      "border: 1px solid rgba(210, 220, 210, 180);\n"
                                      "border-radius: 10px;\n"
                                      "color: black;\n"
                                      "font-weight: bold;\n"
                                      "font-size: 16px;\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 550, 591, 51))
        self.pushButton_2.setStyleSheet("background-color: rgba(210, 220, 210, 150);\n"
                                        "border: 1px solid rgba(210, 220, 210, 180);\n"
                                        "border-radius: 10px;\n"
                                        "color: black;\n"
                                        "font-weight: bold;\n"
                                        "font-size: 16px;\n"
                                        "")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_game = QtWidgets.QPushButton(self.tab)
        self.pushButton_game.setGeometry(QtCore.QRect(10, 10, 141, 51))
        self.pushButton_game.setStyleSheet("background-color: rgba(210, 220, 210, 150);\n"
                                           "border: 1px solid rgba(210, 220, 210, 180);\n"
                                           "border-radius: 10px;\n"
                                           "color: black;\n"
                                           "font-weight: bold;\n"
                                           "font-size: 16px;\n"
                                           "")
        self.pushButton_game.setObjectName("pushButton_game")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(430, 450, 591, 21))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(430, 480, 591, 21))
        self.label_9.setObjectName("label_9")
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setGeometry(QtCore.QRect(430, 510, 591, 31))
        self.spinBox.setObjectName("spinBox")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(-10, -20, 1101, 771))
        self.label_6.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.505382, y1:0.267, x2:0.506, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(248, 255, 247, 255));")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(0, 0, 1031, 71))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(0, 80, 411, 31))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(440, 80, 591, 31))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(10, 110, 411, 20))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(430, 110, 601, 20))
        self.label_14.setObjectName("label_14")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(430, 140, 591, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton.setStyleSheet("font-weight: bold;")
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton1.setStyleSheet("font-weight: bold;")
        self.radioButton1.setObjectName("radioButton1")
        self.horizontalLayout.addWidget(self.radioButton1)
        self.radioButton2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton2.setStyleSheet("font-weight: bold;")
        self.radioButton2.setObjectName("radioButton2")
        self.horizontalLayout.addWidget(self.radioButton2)
        self.qs1 = QtWidgets.QTextBrowser(self.tab_2)
        self.qs1.setGeometry(QtCore.QRect(430, 180, 591, 261))
        self.qs1.setObjectName("qs1")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(430, 450, 591, 21))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(430, 480, 591, 21))
        self.label_16.setObjectName("label_16")
        self.spinBox1 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox1.setGeometry(QtCore.QRect(430, 510, 591, 31))
        self.spinBox1.setObjectName("spinBox1")
        self.pushButton_21 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_21.setGeometry(QtCore.QRect(430, 550, 591, 51))
        self.pushButton_21.setStyleSheet("background-color: rgba(210, 220, 210, 150);\n"
                                         "border: 1px solid rgba(210, 220, 210, 180);\n"
                                         "border-radius: 10px;\n"
                                         "color: black;\n"
                                         "font-weight: bold;\n"
                                         "font-size: 16px;\n"
                                         "")
        self.pushButton_21.setObjectName("pushButton_21")
        self.textEdit1 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit1.setGeometry(QtCore.QRect(10, 140, 411, 41))
        self.textEdit1.setObjectName("textEdit1")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(10, 190, 411, 21))
        self.label_17.setObjectName("label_17")
        self.textEdit_21 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_21.setGeometry(QtCore.QRect(10, 220, 411, 191))
        self.textEdit_21.setObjectName("textEdit_21")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(10, 410, 411, 21))
        self.label_18.setObjectName("label_18")
        self.textEdit31 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit31.setGeometry(QtCore.QRect(10, 440, 411, 31))
        self.textEdit31.setObjectName("textEdit31")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(10, 480, 411, 21))
        self.label_19.setObjectName("label_19")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 510, 411, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkBox.setStyleSheet("font-weight: bold;")
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.checkBox1 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkBox1.setStyleSheet("font-weight: bold;")
        self.checkBox1.setObjectName("checkBox1")
        self.horizontalLayout_2.addWidget(self.checkBox1)
        self.checkBox2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkBox2.setStyleSheet("font-weight: bold;")
        self.checkBox2.setObjectName("checkBox2")
        self.horizontalLayout_2.addWidget(self.checkBox2)
        self.pushButton1 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton1.setGeometry(QtCore.QRect(10, 550, 411, 51))
        self.pushButton1.setStyleSheet("background-color: rgba(210, 220, 210, 150);\n"
                                       "border: 1px solid rgba(210, 220, 210, 180);\n"
                                       "border-radius: 10px;\n"
                                       "color: black;\n"
                                       "font-weight: bold;\n"
                                       "font-size: 16px;\n"
                                       "")
        self.pushButton1.setObjectName("pushButton1")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)
        self.pushButton_game.clicked.connect(self.start_game)
        self.radioButton.clicked.connect(self.questions_update1)
        self.radioButton1.clicked.connect(self.questions_update1)
        self.radioButton2.clicked.connect(self.questions_update1)
        self.pushButton1.clicked.connect(self.add1)
        self.pushButton_21.clicked.connect(self.delete1)

        transport = paramiko.Transport((host, port))
        transport.connect(username=user, password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)

        sftp.get(remotepath, localpath)

        sftp.close()
        transport.close()

        self.questions_update()
        self.questions_update1()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;"
                                                " font-weight:600; color:#1a271a;\">Изменение базы данных</span></p>"
                                                "</body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;"
                                                " font-weight:600;\">Добавить</span></p></body></html>"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;"
                                                " font-weight:600;\">Содержимое базы данных:</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;"
                                                " color:#1a271a;\">Вопрос:</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;"
                                                " color:#1a271a;\">Ответ:</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Добавить"))
        self.pushButton_2.setText(_translate("Form", "Удалить"))
        self.pushButton_game.setText(_translate("Form", "Игра"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;"
                                                " font-weight:600;\">Удалить</span></p><p align=\"center\"><br/></p>"
                                                "</body></html>"))
        self.label_9.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;"
                                                "\">Введите номер вопроса:</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Вопросы и ответы"))
        self.label_10.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;"
                                                 " font-weight:600; color:#1a271a;\">Изменение курсов</span></p></body>"
                                                 "</html>"))
        self.label_11.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;"
                                                 " font-weight:600;\">Добавить</span></p></body></html>"))
        self.label_12.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;"
                                                 " font-weight:600;\">Содержимое базы данных:</span></p></body>"
                                                 "</html>"))
        self.label_13.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;"
                                                 "\">Название:</span></p></body></html>"))
        self.label_14.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;"
                                                 "\">Выберите группу курсов:</span></p></body></html>"))
        self.radioButton.setText(_translate("Form", "Дошкольники"))
        self.radioButton1.setText(_translate("Form", "1-4 классы"))
        self.radioButton2.setText(_translate("Form", "5-11 классы"))
        self.label_15.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;"
                                                 " font-weight:600;\">Удалить</span></p><p align=\"center\"><br/></p>"
                                                 "</body></html>"))
        self.label_16.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;"
                                                 "\">Введите номер вопроса:</span></p></body></html>"))
        self.pushButton_21.setText(_translate("Form", "Удалить"))
        self.label_17.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;"
                                                 "\">Описание:</span></p></body></html>"))
        self.label_18.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;"
                                                 "\">Ссылка на курс:</span></p></body></html>"))
        self.label_19.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;"
                                                 "\">Выберите группу курсов:</span></p></body></html>"))
        self.checkBox.setText(_translate("Form", "Дошкольники"))
        self.checkBox1.setText(_translate("Form", "1-4 классы"))
        self.checkBox2.setText(_translate("Form", "5-11 классы"))
        self.pushButton1.setText(_translate("Form", "Добавить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Курсы"))

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
            qa.name = self.textEdit1.toPlainText()
            qa.description = self.textEdit_21.toPlainText()
            qa.link = self.textEdit31.toPlainText()
            qa.id = qid + 1
            db_sess.add(qa)
            db_sess.commit()
        self.textEdit1.setText('')
        self.textEdit_21.setText('')
        self.textEdit31.setText('')
        self.questions_update1()

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

        transport = paramiko.Transport((host, port))
        transport.connect(username=user, password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)

        sftp.put(localpath, remotepath)

        sftp.close()
        transport.close()

    def questions_update1(self):
        conn = sqlite3.connect('db_data/questions_and_courses.db')
        cur = conn.cursor()
        if self.radioButton.isChecked():
            course_num = '0'
        elif self.radioButton1.isChecked():
            course_num = '1'
        elif self.radioButton2.isChecked():
            course_num = '5'
        else:
            course_num = '0'
        res = cur.execute(f'SELECT * FROM courses{course_num}').fetchall()
        t = ''
        for r in res:
            t += str(r[0]) + '. ' + r[1] + '\n' + r[2] + '\n' + r[3] + '\n\n'
        self.qs1.setText(t)

        transport = paramiko.Transport((host, port))
        transport.connect(username=user, password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)

        sftp.put(localpath, remotepath)

        sftp.close()
        transport.close()

    def start_game(self):
        run_game()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())