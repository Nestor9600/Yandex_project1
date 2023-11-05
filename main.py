import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlite3
from PyQt5 import uic


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 1000, 1000)
        self.setWindowTitle("Тренажер для ФизТеха по физике")

        self.pixmap = QPixmap("fon.jpg")
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(1000, 1000)
        self.image.setPixmap(self.pixmap)

        self.button_1 = QPushButton(self)
        self.button_1.setStyleSheet(
            "background-color: {}; color: {};".format("#004444", "#FFFFFF")
        )
        self.button_1.move(350, 300)
        self.button_1.resize(300, 200)
        self.button_1.setText("Начать подготовку!")
        self.button_1.setFont(QFont("Times", 15))
        self.button_1.clicked.connect(self.show_prod)

    def show_prod(self):
        self.close()
        self.w = Prod()
        self.w.show()


class Prod(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 1000, 1000)
        self.setWindowTitle("Выбери, что хочешь")

        self.pixmap = QPixmap("fon1.jpg")
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(1000, 1000)
        self.image.setPixmap(self.pixmap)

        self.button_phizics = QPushButton(self)
        self.button_phizics.move(350, 150)
        self.button_phizics.resize(300, 200)
        self.button_phizics.setStyleSheet(
            "background-color: {}; color: {};".format("#880000", "#FFFFFF")
        )
        self.button_phizics.setText("Я плохо знаю физику")
        self.button_phizics.setFont(QFont("Times", 15))
        self.button_phizics.clicked.connect(self.run1)

        self.button_maths = QPushButton(self)
        self.button_maths.move(350, 450)
        self.button_maths.resize(300, 200)
        self.button_maths.setStyleSheet(
            "background-color: {}; color: {};".format("#880000", "#FFFFFF")
        )
        self.button_maths.setText("Я знаю физику,\nно есть куда расти")
        self.button_maths.setFont(QFont("Times", 15))
        self.button_maths.clicked.connect(self.run2)

        self.button_back = QPushButton(self)
        self.button_back.move(0, 850)
        self.button_back.resize(150, 150)
        self.button_back.setStyleSheet(
            "background-color: {}; color: {};".format("#880000", "#FFFFFF")
        )
        self.button_back.setText("Вернуться\nназад")
        self.button_back.setFont(QFont("Times", 15))
        self.button_back.clicked.connect(self.runback)

    def runback(self):
        self.close()
        self.w = Example()
        self.w.show()

    def run1(self):
        self.close()
        self.subject = "phizics"
        self.w = Prod1(self.subject)
        self.w.show()

    def run2(self):
        self.close()
        self.subject = "math"
        self.w = Prod1(self.subject)
        self.w.show()


class Prod1(QWidget):
    def __init__(self, subject):
        self.subject = subject
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 1000, 1000)
        self.setWindowTitle("Выбери свой класс")

        self.pixmap = QPixmap("fon1.jpg")
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(1000, 1000)
        self.image.setPixmap(self.pixmap)

        self.button_9 = QPushButton(self)
        self.button_9.move(350, 100)
        self.button_9.resize(300, 200)
        self.button_9.setStyleSheet(
            "background-color: {}; color: {};".format("#880000", "#FFFFFF")
        )
        self.button_9.setText("Учусь в 9 классе")
        self.button_9.setFont(QFont("Times", 15))
        self.button_9.clicked.connect(self.run9)

        self.button_10 = QPushButton(self)
        self.button_10.move(350, 400)
        self.button_10.resize(300, 200)
        self.button_10.setStyleSheet(
            "background-color: {}; color: {};".format("#880000", "#FFFFFF")
        )
        self.button_10.setText("Учусь в 10 классе")
        self.button_10.setFont(QFont("Times", 15))
        self.button_10.clicked.connect(self.run10)

        self.button_11 = QPushButton(self)
        self.button_11.move(350, 700)
        self.button_11.resize(300, 200)
        self.button_11.setStyleSheet(
            "background-color: {}; color: {};".format("#880000", "#FFFFFF")
        )
        self.button_11.setText("Учусь в 11 классе")
        self.button_11.setFont(QFont("Times", 15))
        self.button_11.clicked.connect(self.run11)

        self.button_back = QPushButton(self)
        self.button_back.move(0, 850)
        self.button_back.resize(150, 150)
        self.button_back.setStyleSheet(
            "background-color: {}; color: {};".format("#880000", "#FFFFFF")
        )
        self.button_back.setText("Вернуться\nназад")
        self.button_back.setFont(QFont("Times", 15))
        self.button_back.clicked.connect(self.runback)

    def runback(self):
        self.close()
        self.w = Prod()
        self.w.show()

    def run9(self):
        if self.subject == "phizics":
            self.theme, ok_pressed = QInputDialog.getItem(
                self,
                "Выбери",
                "Тема, которую хочешь изучать",
                (
                    "Механика, 9 класс",
                    "Тепловые явления, 9 класс",
                    "Электричество, 9 класс",
                    "Оптика, 9 класс",
                ),
                1,
                False,
            )
            if ok_pressed:
                self.close()
                self.w = Prod2(self.theme, self.subject)
                self.w.show()
        else:
            self.theme = "Математическая физика"
            self.close()
            self.w = Prod2(self.theme, self.subject)
            self.w.show()

    def run10(self):
        if self.subject == "phizics":
            self.theme, ok_pressed = QInputDialog.getItem(
                self,
                "Выбери",
                "Тема, которую хочешь изучать",
                (
                    "Механика, 10 класс",
                    "Молекулярная физика и термодинамика, 10 класс",
                    "Электростатика, 10 класс",
                    "Электрический ток, 10 класс",
                    "Оптика, 10 класс",
                ),
                1,
                False,
            )
            if ok_pressed:
                self.close()
                self.w = Prod2(self.theme, self.subject)
                self.w.show()
        else:
            self.theme = "Математическая физика"
            self.close()
            self.w = Prod2(self.theme, self.subject)
            self.w.show()

    def run11(self):
        if self.subject == "phizics":
            self.theme, ok_pressed = QInputDialog.getItem(
                self,
                "Выбери",
                "Тема, которую хочешь изучать",
                (
                    "Механика, 11 класс",
                    "Молекулярная физика и термодинамика, 11 класс",
                    "Электричество и магнетизм, 11 класс",
                    "Оптика, 11 класс",
                    "Атомы, ядра, кванты, 11 класс",
                ),
                1,
                False,
            )
            if ok_pressed:
                self.close()
                self.w = Prod2(self.theme, self.subject)
                self.w.show()
        else:
            self.theme = "Математическая физика"
            self.close()
            self.w = Prod2(self.theme, self.subject)
            self.w.show()


class Prod2(QWidget):
    def __init__(self, theme, subject):
        self.theme = theme
        self.subject = subject
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 1000, 1000)
        self.setWindowTitle('Тренажер по теме "{}"'.format(self.theme))

        self.pixmap = QPixmap("fon1.jpg")
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(1000, 1000)
        self.image.setPixmap(self.pixmap)

        self.button_1 = QPushButton(self)
        self.button_1.move(150, 300)
        self.button_1.resize(100, 100)
        self.button_1.setStyleSheet(
            "background-color: {}; color: {};".format("#880000", "#FFFFFF")
        )
        self.button_1.setText("1")
        self.button_1.setFont(QFont("Times", 15))
        self.button_1.clicked.connect(self.run1)

        self.button_2 = QPushButton(self)
        self.button_2.move(300, 300)
        self.button_2.resize(100, 100)
        self.button_2.setStyleSheet(
            "background-color: {}; color: {};".format("#880000", "#FFFFFF")
        )
        self.button_2.setText("2")
        self.button_2.setFont(QFont("Times", 15))
        self.button_2.clicked.connect(self.run2)

        self.button_3 = QPushButton(self)
        self.button_3.move(450, 300)
        self.button_3.resize(100, 100)
        self.button_3.setStyleSheet(
            "background-color: {}; color: {};".format("#880000", "#FFFFFF")
        )
        self.button_3.setText("3")
        self.button_3.setFont(QFont("Times", 15))
        self.button_3.clicked.connect(self.run3)

        self.button_4 = QPushButton(self)
        self.button_4.move(600, 300)
        self.button_4.resize(100, 100)
        self.button_4.setStyleSheet(
            "background-color: {}; color: {};".format("#880000", "#FFFFFF")
        )
        self.button_4.setText("4")
        self.button_4.setFont(QFont("Times", 15))
        self.button_4.clicked.connect(self.run4)

        self.button_5 = QPushButton(self)
        self.button_5.move(750, 300)
        self.button_5.resize(100, 100)
        self.button_5.setStyleSheet(
            "background-color: {}; color: {};".format("#880000", "#FFFFFF")
        )
        self.button_5.setText("5")
        self.button_5.setFont(QFont("Times", 15))
        self.button_5.clicked.connect(self.run5)

        self.button_6 = QPushButton(self)
        self.button_6.move(150, 600)
        self.button_6.resize(100, 100)
        self.button_6.setStyleSheet(
            "background-color: {}; color: {};".format("#880000", "#FFFFFF")
        )
        self.button_6.setText("6")
        self.button_6.setFont(QFont("Times", 15))
        self.button_6.clicked.connect(self.run6)

        self.button_7 = QPushButton(self)
        self.button_7.move(300, 600)
        self.button_7.resize(100, 100)
        self.button_7.setStyleSheet(
            "background-color: {}; color: {};".format("#880000", "#FFFFFF")
        )
        self.button_7.setText("7")
        self.button_7.setFont(QFont("Times", 15))
        self.button_7.clicked.connect(self.run7)

        self.button_8 = QPushButton(self)
        self.button_8.move(450, 600)
        self.button_8.resize(100, 100)
        self.button_8.setStyleSheet(
            "background-color: {}; color: {};".format("#880000", "#FFFFFF")
        )
        self.button_8.setText("8")
        self.button_8.setFont(QFont("Times", 15))
        self.button_8.clicked.connect(self.run8)

        self.button_9 = QPushButton(self)
        self.button_9.move(600, 600)
        self.button_9.resize(100, 100)
        self.button_9.setStyleSheet(
            "background-color: {}; color: {};".format("#880000", "#FFFFFF")
        )
        self.button_9.setText("9")
        self.button_9.setFont(QFont("Times", 15))
        self.button_9.clicked.connect(self.run9)

        self.button_10 = QPushButton(self)
        self.button_10.move(750, 600)
        self.button_10.resize(100, 100)
        self.button_10.setStyleSheet(
            "background-color: {}; color: {};".format("#880000", "#FFFFFF")
        )
        self.button_10.setText("10")
        self.button_10.setFont(QFont("Times", 15))
        self.button_10.clicked.connect(self.run10)

        self.button_back = QPushButton(self)
        self.button_back.move(0, 850)
        self.button_back.resize(150, 150)
        self.button_back.setStyleSheet(
            "background-color: {}; color: {};".format("#880000", "#FFFFFF")
        )
        self.button_back.setText("Вернуться\nназад")
        self.button_back.setFont(QFont("Times", 15))
        self.button_back.clicked.connect(self.runback)

    def runback(self):
        self.close()
        self.w = Prod1(self.subject)
        self.w.show()

    def run1(self):
        con = sqlite3.connect("films_db.sqlite")
        cur = con.cursor()
        self.exercise = cur.execute(
            """SELECT exercise FROM subjects WHERE theme = ? AND number = 1""",
            (self.theme,),
        ).fetchone()
        self.answer = cur.execute(
            """SELECT answer FROM subjects WHERE theme = ? AND number = 1""",
            (self.theme,),
        ).fetchone()
        con.close()
        self.close()
        self.w = Prod3(self.exercise, self.theme, self.answer, self.subject)
        self.w.show()

    def run2(self):
        con = sqlite3.connect("films_db.sqlite")
        cur = con.cursor()
        self.exercise = cur.execute(
            """SELECT exercise FROM subjects WHERE theme = ? AND number = 2""",
            (self.theme,),
        ).fetchone()
        self.answer = cur.execute(
            """SELECT answer FROM subjects WHERE theme = ? AND number = 2""",
            (self.theme,),
        ).fetchone()
        con.close()
        self.close()
        self.w = Prod3(self.exercise, self.theme, self.answer, self.subject)
        self.w.show()

    def run3(self):
        con = sqlite3.connect("films_db.sqlite")
        cur = con.cursor()
        self.exercise = cur.execute(
            """SELECT exercise FROM subjects WHERE theme = ? AND number = 3""",
            (self.theme,),
        ).fetchone()
        self.answer = cur.execute(
            """SELECT answer FROM subjects WHERE theme = ? AND number = 3""",
            (self.theme,),
        ).fetchone()
        con.close()
        self.close()
        self.w = Prod3(self.exercise, self.theme, self.answer, self.subject)
        self.w.show()

    def run4(self):
        con = sqlite3.connect("films_db.sqlite")
        cur = con.cursor()
        self.exercise = cur.execute(
            """SELECT exercise FROM subjects WHERE theme = ? AND number = 4""",
            (self.theme,),
        ).fetchone()
        self.answer = cur.execute(
            """SELECT answer FROM subjects WHERE theme = ? AND number = 4""",
            (self.theme,),
        ).fetchone()
        con.close()
        self.close()
        self.w = Prod3(self.exercise, self.theme, self.answer, self.subject)
        self.w.show()

    def run5(self):
        con = sqlite3.connect("films_db.sqlite")
        cur = con.cursor()
        self.exercise = cur.execute(
            """SELECT exercise FROM subjects WHERE theme = ? AND number = 5""",
            (self.theme,),
        ).fetchone()
        self.answer = cur.execute(
            """SELECT answer FROM subjects WHERE theme = ? AND number = 5""",
            (self.theme,),
        ).fetchone()
        con.close()
        self.close()
        self.w = Prod3(self.exercise, self.theme, self.answer, self.subject)
        self.w.show()

    def run6(self):
        con = sqlite3.connect("films_db.sqlite")
        cur = con.cursor()
        self.exercise = cur.execute(
            """SELECT exercise FROM subjects WHERE theme = ? AND number = 6""",
            (self.theme,),
        ).fetchone()
        self.answer = cur.execute(
            """SELECT answer FROM subjects WHERE theme = ? AND number = 6""",
            (self.theme,),
        ).fetchone()
        con.close()
        self.close()
        self.w = Prod3(self.exercise, self.theme, self.answer, self.subject)
        self.w.show()

    def run7(self):
        con = sqlite3.connect("films_db.sqlite")
        cur = con.cursor()
        self.exercise = cur.execute(
            """SELECT exercise FROM subjects WHERE theme = ? AND number = 7""",
            (self.theme,),
        ).fetchone()
        self.answer = cur.execute(
            """SELECT answer FROM subjects WHERE theme = ? AND number = 7""",
            (self.theme,),
        ).fetchone()
        con.close()
        self.close()
        self.w = Prod3(self.exercise, self.theme, self.answer, self.subject)
        self.w.show()

    def run8(self):
        con = sqlite3.connect("films_db.sqlite")
        cur = con.cursor()
        self.exercise = cur.execute(
            """SELECT exercise FROM subjects WHERE theme = ? AND number = 8""",
            (self.theme,),
        ).fetchone()
        self.answer = cur.execute(
            """SELECT answer FROM subjects WHERE theme = ? AND number = 8""",
            (self.theme,),
        ).fetchone()
        con.close()
        self.close()
        self.w = Prod3(self.exercise, self.theme, self.answer, self.subject)
        self.w.show()

    def run9(self):
        con = sqlite3.connect("films_db.sqlite")
        cur = con.cursor()
        self.exercise = cur.execute(
            """SELECT exercise FROM subjects WHERE theme = ? AND number = 9""",
            (self.theme,),
        ).fetchone()
        self.answer = cur.execute(
            """SELECT answer FROM subjects WHERE theme = ? AND number = 9""",
            (self.theme,),
        ).fetchone()
        con.close()
        self.close()
        self.w = Prod3(self.exercise, self.theme, self.answer, self.subject)
        self.w.show()

    def run10(self):
        con = sqlite3.connect("films_db.sqlite")
        cur = con.cursor()
        self.exercise = cur.execute(
            """SELECT exercise FROM subjects WHERE theme = ? AND number = 10""",
            (self.theme,),
        ).fetchone()
        self.answer = cur.execute(
            """SELECT answer FROM subjects WHERE theme = ? AND number = 10""",
            (self.theme,),
        ).fetchone()
        con.close()
        self.close()
        self.w = Prod3(self.exercise, self.theme, self.answer, self.subject)
        self.w.show()


class Prod3(QWidget):
    def __init__(self, exercise, theme, answer, subject):
        self.exercise = exercise
        self.theme = theme
        self.answer = answer
        self.subject = subject
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 1500, 1000)
        self.setWindowTitle('Тренажер по теме "{}"'.format(self.theme))

        self.pixmap = QPixmap("fon4.jpg")
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(1500, 1000)
        self.image.setPixmap(self.pixmap)

        self.label = QLabel(self)
        self.label.setText("{}".format(self.exercise[0]))
        self.label.setStyleSheet("color: {};".format("#FFFFFF"))
        self.label.move(80, 100)
        self.label.setFont(QFont("Times", 13))

        self.button_1 = QPushButton(self)
        self.button_1.move(1350, 850)
        self.button_1.resize(150, 150)
        self.button_1.setStyleSheet(
            "background-color: {}; color: {};".format("#880000", "#FFFFFF")
        )
        self.button_1.setText("Посмотреть\nответ")
        self.button_1.setFont(QFont("Times", 15))
        self.button_1.clicked.connect(self.run1)

        self.button_2 = QPushButton(self)
        self.button_2.move(0, 850)
        self.button_2.resize(150, 150)
        self.button_2.setStyleSheet(
            "background-color: {}; color: {};".format("#880000", "#FFFFFF")
        )
        self.button_2.setText("Вернуться\nназад")
        self.button_2.setFont(QFont("Times", 15))
        self.button_2.clicked.connect(self.run2)

        self.button_3 = QPushButton(self)
        self.button_3.move(700, 850)
        self.button_3.resize(150, 150)
        self.button_3.setStyleSheet(
            "background-color: {}; color: {};".format("#880000", "#FFFFFF")
        )
        self.button_3.setText("Я\nзабыл\nтеорию")
        self.button_3.setFont(QFont("Times", 15))
        self.button_3.clicked.connect(self.run3)

    def run1(self):
        self.button_1.setText("{}".format(self.answer[0]))
        self.button_1.setFont(QFont("Times", 15))

    def run2(self):
        self.close()
        self.w = Prod2(self.theme, self.subject)
        self.w.show()

    def run3(self):
        self.close()
        self.w = Prod4(self.exercise, self.theme, self.answer, self.subject)
        self.w.show()


class Prod4(QWidget):
    def __init__(self, exercise, theme, answer, subject):
        self.exercise = exercise
        self.theme = theme
        self.answer = answer
        self.subject = subject
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(50, 50, 1500, 1310)
        self.setWindowTitle('Теория по теме "{}"'.format(self.theme))

        self.pixmap = QPixmap("fon4.jpg")
        self.image = QLabel(self)
        self.image.move(0, 310)
        self.image.resize(1500, 1260)
        self.image.setPixmap(self.pixmap)

        if self.subject == "phizics":
            self.pixmap1 = QPixmap("fon5.jpg")
            self.image1 = QLabel(self)
            self.image1.move(0, 0)
            self.image1.resize(1500, 1160)
            self.image1.setPixmap(self.pixmap1)

        else:
            self.pixmap2 = QPixmap("fon7.jpg")
            self.image2 = QLabel(self)
            self.image2.move(0, 0)
            self.image2.resize(1500, 1160)
            self.image2.setPixmap(self.pixmap2)

        self.button_back = QPushButton(self)
        self.button_back.move(0, 1160)
        self.button_back.resize(150, 150)
        self.button_back.setStyleSheet(
            "background-color: {}; color: {};".format("#880000", "#FFFFFF")
        )
        self.button_back.setText("Вернуться\nназад")
        self.button_back.setFont(QFont("Times", 15))
        self.button_back.clicked.connect(self.runback)

    def runback(self):
        self.close()
        self.w = Prod3(self.exercise, self.theme, self.answer, self.subject)
        self.w.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
