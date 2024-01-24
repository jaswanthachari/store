from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QDialog,QApplication,QMessageBox
import sys

Username = "1"
username1 = "Jaswanth","jaswanth","JASWANTH"
password = "1"

class login(QDialog):

    def __init__(self):
        super(login,self).__init__()

        self.tabWidget = None
        self.setFixedHeight(320)
        self.setFixedWidth(350)

        label_font = QtGui.QFont()
        label_font.setPointSize(8)
        label_font.setFamily("Arial Black")

        line_Edit = QtGui.QFont()
        line_Edit.setPointSize(15)

        self.username_label = QtWidgets.QLabel(self)
        self.username_label.setText("USERNAME : ")
        self.username_label.setGeometry(60,100,90,30)
        self.username_label.setFont(label_font)

        self.username_lE = QtWidgets.QLineEdit(self)
        self.username_lE.setGeometry(160,100,130,30)
        self.username_lE.setFont(line_Edit)

        self.Password_label = QtWidgets.QLabel(self)
        self.Password_label.setText("PASSWORD : ")
        self.Password_label.setGeometry(60, 150, 90, 30)
        self.Password_label.setFont(label_font)


        self.Password_LE = QtWidgets.QLineEdit(self)
        self.Password_LE.setGeometry(160, 156, 130, 30)
        self.Password_LE.setEchoMode(QtWidgets.QLineEdit.Password)


        self.login_BTN = QtWidgets.QPushButton(self)
        self.login_BTN.setGeometry(90,200,90,30)
        self.login_BTN.setText("Login")
        self.login_BTN.clicked.connect(self.verify)


        tab = QtWidgets.QLabel
        tab.setStyleSheet(self,"background-image: url(Royal.jfif)")





    def verify(self):
        pasword = self.Password_LE.text()
        user = self.username_lE.text()
        if pasword==password and user==Username or user==username1:
            print("Correct")
            self.login_BTN.clicked.connect(self.nextpage)
        else:
            self.login_BTN.clicked.connect(self.error)

    def error(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Error 404 Not Found")
        msg.setText("Your Password or username is not correct!")
        msg.exec()

    def nextpage(self):
        self.destroy()
        self.w = WelcomePage()
        self.w.show()

class WelcomePage(QDialog):

    def __init__(self):
        super(WelcomePage,self).__init__()

        self.setFixedHeight(500)
        self.setFixedWidth(800)

        label_font = QtGui.QFont()
        label_font.setPointSize(17)
        label_font.setFamily("Arial Black")

        label = QtWidgets.QLabel
        label.setStyleSheet(self, "background-image: url(car4.PNG)")

        BTN_font = QtGui.QFont()
        BTN_font.setPointSize(14)
        BTN_font.setFamily("Stencil")

        self.text_label = QtWidgets.QLabel(self)
        self.text_label.setText("Welcome To SSSJBH Stores  ")
        self.text_label.setGeometry(230,100,400,30)
        self.text_label.setFont(label_font)


        self.Purchase_BTN = QtWidgets.QPushButton(self)
        self.Purchase_BTN.setGeometry(90,200,200,30)
        self.Purchase_BTN.setText("Purchases")
        self.Purchase_BTN.setFont(BTN_font)


        self.Sale_BTN = QtWidgets.QPushButton(self)
        self.Sale_BTN.setGeometry(90, 300, 200, 30)
        self.Sale_BTN.setText("Sell Now ")
        self.Sale_BTN.setFont(BTN_font)

        self.TotalSales_BTN = QtWidgets.QPushButton(self)
        self.TotalSales_BTN.setGeometry(460, 200, 200, 30)
        self.TotalSales_BTN.setText("Total Sales ")
        self.TotalSales_BTN.setFont(BTN_font)

        self.itemStock_BTN = QtWidgets.QPushButton(self)
        self.itemStock_BTN.setGeometry(460, 300, 200, 30)
        self.itemStock_BTN.setText("Add Item Stock ")
        self.itemStock_BTN.setFont(BTN_font)

        self.Admin_BTN = QtWidgets.QPushButton(self)
        self.Admin_BTN.setGeometry(570, 450, 200, 30)
        self.Admin_BTN.setText("Add Admin")
        self.Admin_BTN.setFont(BTN_font)

        self.Admin_BTN.clicked.connect(self.Adminpage)
        self.Purchase_BTN.clicked.connect(self.purchasepage)



    def Adminpage(self):
        self.destroy()
        self.A = admin()
        self.A.show()

    def purchasepage(self):
        self.destroy()
        self.p = Purchases()
        self.p.show()

class admin(QDialog):

    def __init__(self):
        super(admin,self).__init__()

        self.setFixedHeight(320)
        self.setFixedWidth(400)

        label_font = QtGui.QFont()
        label_font.setPointSize(8)
        label_font.setFamily("Arial Black")

        BTN_font = QtGui.QFont()
        BTN_font.setPointSize(10)
        BTN_font.setFamily("Stencil")



        self.username_label = QtWidgets.QLabel(self)
        self.username_label.setText("USERNAME : ")
        self.username_label.setGeometry(60,100,90,30)
        self.username_label.setFont(label_font)

        self.username_lE = QtWidgets.QLineEdit(self)
        self.username_lE.setGeometry(230,100,130,30)

        self.Password_label = QtWidgets.QLabel(self)
        self.Password_label.setText("PASSWORD : ")
        self.Password_label.setGeometry(60, 150, 90, 30)
        self.Password_label.setFont(label_font)


        self.Password_LE = QtWidgets.QLineEdit(self)
        self.Password_LE.setGeometry(230, 156, 130, 30)
        self.Password_LE.setEchoMode(QtWidgets.QLineEdit.Password)

        self.ConfirmPassword_label = QtWidgets.QLabel(self)
        self.ConfirmPassword_label.setText(" CONFIRM PASSWORD : ")
        self.ConfirmPassword_label.setGeometry(60, 200, 150, 30)
        self.ConfirmPassword_label.setFont(label_font)

        self.ConfirmPassword_LE = QtWidgets.QLineEdit(self)
        self.ConfirmPassword_LE.setGeometry(230, 200, 130, 30)
        self.ConfirmPassword_LE.setEchoMode(QtWidgets.QLineEdit.Password)

        self.Signup_BTN = QtWidgets.QPushButton(self)
        self.Signup_BTN.setGeometry(140,260,90,30)
        self.Signup_BTN.setText("SIGN UP")
        self.Signup_BTN.clicked.connect(self.checkpswd)

        self.Back_BTN = QtWidgets.QPushButton(self)
        self.Back_BTN.setGeometry(30, 30, 50, 40)
        self.Back_BTN.setText("Back")
        self.Back_BTN.setFont(BTN_font)

        if self.Back_BTN.clicked:
            self.Back_BTN.clicked.connect(self.welcompage)

    def welcompage(self):
        self.destroy()
        self.p = WelcomePage()
        self.p.show()




    def Correct(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Success")
        msg.setText("PASSWORD IS SET ! ")
        msg.exec()

    def error(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Error 404 Not Found")
        msg.setText("Your Passwords didn't Match")
        msg.exec()

    def checkpswd(self):
        if self.Password_LE.text() == self.ConfirmPassword_LE.text():
            print("Password is set .")
            self.Signup_BTN.clicked.connect(self.Correct)
        elif self.Password_LE.text() != self.ConfirmPassword_LE.text():
            print("Password did not Match .")
            self.Signup_BTN.clicked.connect(self.error)

class Purchases(QDialog):

    def __init__(self):
        super(Purchases,self).__init__()

        self.setFixedHeight(1000)
        self.setFixedWidth(1900)

        label_font = QtGui.QFont()
        label_font.setPointSize(12)
        label_font.setFamily("Arial Black")
        label = QtWidgets.QLabel
        label.setStyleSheet(self, "background-image: url(wp4795094-general-store-wallpapers.jpg)")

        main_font = QtGui.QFont()
        main_font.setPointSize(25)
        main_font.setFamily("Cooper Black")

        BTN_font = QtGui.QFont()
        BTN_font.setPointSize(14)
        BTN_font.setFamily("Stencil")

        self.text_label = QtWidgets.QLabel(self)
        self.text_label.setText("PURCHASES")
        self.text_label.setGeometry(950,30,290,30)
        self.text_label.setFont(main_font)

        LABEL_Y = 100

        self.ItemNo_label = QtWidgets.QLabel(self)
        self.ItemNo_label.setText("Item no")
        self.ItemNo_label.setGeometry(100, 100, 100, 30)
        self.ItemNo_label.setFont(label_font)



        self.SNAme_label = QtWidgets.QLabel(self)
        self.SNAme_label.setText("Name Of the supplier ")
        self.SNAme_label.setGeometry(250, 100, 190, 30)
        self.SNAme_label.setFont(label_font)



        self.SPhone_label = QtWidgets.QLabel(self)
        self.SPhone_label.setText("Phone number ")
        self.SPhone_label.setGeometry(500, 100, 140, 30)
        self.SPhone_label.setFont(label_font)



        self.Parti_label = QtWidgets.QLabel(self)
        self.Parti_label.setText("Particulars")
        self.Parti_label.setGeometry(700, 100, 140, 30)
        self.Parti_label.setFont(label_font)



        self.Price_label = QtWidgets.QLabel(self)
        self.Price_label.setText("PRICE")
        self.Price_label.setGeometry(950, 100, 140, 30)
        self.Price_label.setFont(label_font)



        self.Quantity_label = QtWidgets.QLabel(self)
        self.Quantity_label.setText("QUANTITY")
        self.Quantity_label.setGeometry(1150, 100, 100, 30)
        self.Quantity_label.setFont(label_font)


        self.TAmt_label = QtWidgets.QLabel(self)
        self.TAmt_label.setText("TOTAL AMOUNT ")
        self.TAmt_label.setGeometry(1300, 100, 140, 30)
        self.TAmt_label.setFont(label_font)

        self.Back_BTN = QtWidgets.QPushButton(self)
        self.Back_BTN.setGeometry(30, 30, 200, 30)
        self.Back_BTN.setText("Back")
        self.Back_BTN.setFont(BTN_font)

        if self.Back_BTN.clicked:
            self.Back_BTN.clicked.connect(self.welcompage)

    def welcompage(self):
        self.destroy()
        self.p = WelcomePage()
        self.p.show()



app = QApplication(sys.argv)
l = login()
l.show()
app.exec_()

