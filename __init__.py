from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from PyQt5.QtWidgets import QMessageBox, QWidget
from bilisimsistemlerianalizi.tshirt import Ui_TshirtWindow
from bilisimsistemlerianalizi.pantolon import Ui_PantolonWindow
from bilisimsistemlerianalizi.poloshirt import Ui_PoloshirtWindow
from bilisimsistemlerianalizi.icgiyim import Ui_IcgiyimWindow




class Ui_MainWindow(object):

    def opentshirt(self):
        self.tshirtwindow = QtWidgets.QMainWindow()
        self.ui = Ui_TshirtWindow()
        self.ui.setupUi(self.tshirtwindow)
        self.tshirtwindow.show()
    def openpantolon(self):
        self.pantolonwindow = QtWidgets.QMainWindow()
        self.ui = Ui_PantolonWindow()
        self.ui.setupUi(self.pantolonwindow)
        self.pantolonwindow.show()
    def openicgiyim(self):
        self.icgiyimwindow = QtWidgets.QMainWindow()
        self.ui = Ui_IcgiyimWindow()
        self.ui.setupUi(self.icgiyimwindow)
        self.icgiyimwindow.show()
    def openpoloshirt(self):
        self.poloshirtwindow = QtWidgets.QMainWindow()
        self.ui = Ui_PoloshirtWindow()
        self.ui.setupUi(self.poloshirtwindow)
        self.poloshirtwindow.show()


    def loginform(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(160, 100, 421, 291))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.g_box = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.g_box.setContentsMargins(0, 0, 0, 0)
        self.g_box.setObjectName("g_box")
        self.sifrelabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sifrelabel.setFont(font)
        self.sifrelabel.setObjectName("sifrelabel")
        self.g_box.addWidget(self.sifrelabel, 2, 0, 1, 1)
        self.kullaniciadilinedit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.kullaniciadilinedit.setFont(font)
        self.kullaniciadilinedit.setObjectName("kullaniciadilinedit")
        self.g_box.addWidget(self.kullaniciadilinedit, 0, 1, 1, 1)
        self.sifrelineedit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.sifrelineedit.setObjectName("sifrelineedit")
        self.g_box.addWidget(self.sifrelineedit, 2, 1, 1, 1)
        self.kullaniciadilabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.kullaniciadilabel.setFont(font)
        self.kullaniciadilabel.setObjectName("kullaniciadilabel")
        self.g_box.addWidget(self.kullaniciadilabel, 0, 0, 1, 1)
        self.Logingirisbuton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Logingirisbuton.setFont(font)
        self.Logingirisbuton.setObjectName("Logingirisbuton")
        self.g_box.addWidget(self.Logingirisbuton, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuUrunler = QtWidgets.QMenu(self.menubar)
        self.menuUrunler.setObjectName("menuUrunler")
        self.menuMusteriler = QtWidgets.QMenu(self.menubar)
        self.menuMusteriler.setObjectName("menuMusteriler")
        self.menuSiparisler = QtWidgets.QMenu(self.menubar)
        self.menuSiparisler.setObjectName("menuSiparisler")
        self.menuSiteAyarlar = QtWidgets.QMenu(self.menubar)
        self.menuSiteAyarlar.setObjectName("menuSiteAyarlar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionTshirt = QtWidgets.QAction(MainWindow)
        self.actionTshirt.setObjectName("actionTshirt")
        self.actionPantolon = QtWidgets.QAction(MainWindow)
        self.actionPantolon.setObjectName("actionPantolon")
        self.actionPoloshirt = QtWidgets.QAction(MainWindow)
        self.actionPoloshirt.setObjectName("actionPoloshirt")
        self.actioncgiyim = QtWidgets.QAction(MainWindow)
        self.actioncgiyim.setObjectName("actioncgiyim")
        self.menuUrunler.addAction(self.actionTshirt)
        self.menuUrunler.addAction(self.actionPantolon)
        self.menuUrunler.addAction(self.actionPoloshirt)
        self.menuUrunler.addAction(self.actioncgiyim)
        self.menubar.addAction(self.menuUrunler.menuAction())
        self.menubar.addAction(self.menuMusteriler.menuAction())
        self.menubar.addAction(self.menuSiparisler.menuAction())
        self.menubar.addAction(self.menuSiteAyarlar.menuAction())
        self.menubar.setVisible(False)


        self.Loginform2(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def Loginform2(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sifrelabel.setText(_translate("MainWindow", "Şifre:"))
        self.kullaniciadilabel.setText(_translate("MainWindow", "Kullanıcı adı:"))
        self.Logingirisbuton.setText(_translate("MainWindow", "Giriş"))
        self.menuUrunler.setTitle(_translate("MainWindow", "Ürünler"))
        self.menuMusteriler.setTitle(_translate("MainWindow", "Müsteriler"))
        self.menuSiparisler.setTitle(_translate("MainWindow", "Siparisler"))
        self.menuSiteAyarlar.setTitle(_translate("MainWindow", "Site Ayarları"))
        self.actionTshirt.setText(_translate("MainWindow", "Tshirt"))
        self.actionPantolon.setText(_translate("MainWindow", "Pantolon"))
        self.actionPoloshirt.setText(_translate("MainWindow", "Poloshirt"))
        self.actioncgiyim.setText(_translate("MainWindow", "İcgiyim"))
        self.Logingirisbuton.clicked.connect(self.click)
        self.actionTshirt.triggered.connect(self.opentshirt)
        self.actionPantolon.triggered.connect(self.openpantolon)
        self.actioncgiyim.triggered.connect(self.openicgiyim)
        self.actionPoloshirt.triggered.connect(self.openpoloshirt)

    def click(self):

        username = str(self.kullaniciadilinedit.text())
        password = str(self.sifrelineedit.text())

        conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="bilisim_proje_odevi")

        cursor = conn.cursor(pymysql.cursors.DictCursor)

        query = "select * from yonetici_girisi where Kullanici_adi='{}' and Sifre='{}'".format(username, password)
        cursor.execute(query)
        data = cursor.fetchall()
        admin = False
        for row in data:
            admin = True
        conn.close()
        if admin:
            # Messagebox
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Başarılı")
            msg.setText("Başarıyla Giriş Yaptınız...")
            msg.buttonClicked.connect(self.basariligirisbutonok)
            msg.exec_()


        else:
            #Messagebox
            msg = QMessageBox()
            msg.setWindowTitle("Giriş yapılamadı.")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Hatalı Giriş yaptınız")
            msg.exec_()

    def basariligirisbutonok(self):
        self.remove_all_widget()
        self.menubar.setVisible(True)



    def remove_all_widget(self):
        for i in reversed(range(self.g_box.count())):
            widgetToRemove = self.g_box.itemAt(i).widget()
            self.g_box.removeWidget(widgetToRemove)
            widgetToRemove.setParent(None)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.loginform(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
