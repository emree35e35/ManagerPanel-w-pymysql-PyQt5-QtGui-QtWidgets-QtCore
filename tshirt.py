# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\emree\Desktop\logindesigntshirt.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon

from PyQt5.QtCore import (QDate, QDateTime, QRegExp, QSortFilterProxyModel, Qt,
                          QTime)
from PyQt5.QtGui import QStandardItemModel,QIntValidator
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
                             QGroupBox, QHBoxLayout, QLabel, QLineEdit, QTreeView, QVBoxLayout,
                             QWidget)
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TshirtWindow(QWidget):
    TSHIRTID, TSHIRTISIM, TSHIRTFIYAT, RESIMURL = range(4)

    def setupUi(self, TshirtWindow):
        TshirtWindow.setObjectName("TshirtWindow")
        TshirtWindow.resize(997, 704)
        TshirtWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(TshirtWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 120, 791, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        # bukısım cok onemlı
        self.treeWidget = QTreeView(self.gridLayoutWidget)

        self.treeWidget.setEditTriggers(
            QtWidgets.QTableWidget.NoEditTriggers)
        # QtWidgets.QAbstractItemView.DoubleClicked | QtWidgets.QAbstractItemView.EditKeyPressed | QtWidgets.QAbstractItemView.SelectedClicked)
        self.treeWidget.setObjectName("treeWidget")
        self.gridLayout.addWidget(self.treeWidget, 0, 0, 2, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(60, 390, 341, 231))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tshirtisimlineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tshirtisimlineEdit.setFont(font)
        self.tshirtisimlineEdit.setObjectName("tshirtisimlineEdit")
        self.gridLayout_3.addWidget(self.tshirtisimlineEdit, 1, 1, 1, 1)
        self.tshirtisimlabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tshirtisimlabel.setFont(font)
        self.tshirtisimlabel.setObjectName("tshirtisimlabel")
        self.gridLayout_3.addWidget(self.tshirtisimlabel, 1, 0, 1, 1)
        self.tshirtfyatlabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tshirtfyatlabel.setFont(font)
        self.tshirtfyatlabel.setObjectName("tshirtfyatlabel")
        self.gridLayout_3.addWidget(self.tshirtfyatlabel, 2, 0, 1, 1)
        self.tshirtidlineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.tshirtidlineEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tshirtidlineEdit.setFont(font)
        self.tshirtidlineEdit.setObjectName("tshirtidlineEdit")
        self.gridLayout_3.addWidget(self.tshirtidlineEdit, 0, 1, 1, 1)
        self.tshirtidlabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tshirtidlabel.setFont(font)
        self.tshirtidlabel.setObjectName("tshirtidlabel")
        self.gridLayout_3.addWidget(self.tshirtidlabel, 0, 0, 1, 1)
        self.tshirtfiyatlineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tshirtfiyatlineEdit.setFont(font)
        self.tshirtfiyatlineEdit.setObjectName("tshirtfiyatlineEdit")
        self.gridLayout_3.addWidget(self.tshirtfiyatlineEdit, 2, 1, 1, 1)
        self.tshirtresimurllineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tshirtresimurllineEdit.setFont(font)
        self.tshirtresimurllineEdit.setObjectName("tshirtresimurllineEdit")
        self.gridLayout_3.addWidget(self.tshirtresimurllineEdit, 3, 1, 1, 1)
        self.tshirtresimurllabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tshirtresimurllabel.setFont(font)
        self.tshirtresimurllabel.setObjectName("tshirtresimurllabel")
        self.gridLayout_3.addWidget(self.tshirtresimurllabel, 3, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(419, 410, 211, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tshirteklebuton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tshirteklebuton.setFont(font)
        self.tshirteklebuton.setObjectName("tshirteklebuton")
        self.verticalLayout.addWidget(self.tshirteklebuton)
        self.tshirtduzenlebuton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tshirtduzenlebuton.setFont(font)
        self.tshirtduzenlebuton.setObjectName("tshirtduzenlebuton")
        self.verticalLayout.addWidget(self.tshirtduzenlebuton)
        self.tshirtsilbuton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tshirtsilbuton.setFont(font)
        self.tshirtsilbuton.setObjectName("tshirtsilbuton")
        self.verticalLayout.addWidget(self.tshirtsilbuton)
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(650, 500, 271, 31))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)


        font = QtGui.QFont()
        font.setPointSize(10)


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 20, 561, 51))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 70, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setObjectName("label_3")
        TshirtWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TshirtWindow)
        self.statusbar.setObjectName("statusbar")
        TshirtWindow.setStatusBar(self.statusbar)
        self.actionTshirt = QtWidgets.QAction(TshirtWindow)
        self.actionTshirt.setObjectName("actionTshirt")
        self.actionPantolon = QtWidgets.QAction(TshirtWindow)
        self.actionPantolon.setObjectName("actionPantolon")
        self.actionPoloshirt = QtWidgets.QAction(TshirtWindow)
        self.actionPoloshirt.setObjectName("actionPoloshirt")
        self.actioncgiyim = QtWidgets.QAction(TshirtWindow)
        self.actioncgiyim.setObjectName("actioncgiyim")
        self.retranslateUi(TshirtWindow)
        QtCore.QMetaObject.connectSlotsByName(TshirtWindow)

        #SORT  SIRALAMA
        self.treeWidget.setSortingEnabled(True)

        #only int
        self.onlyInt = QIntValidator()
        self.tshirtfiyatlineEdit.setValidator(self.onlyInt)

        # bu kısmı kullan nolur
        model = self.treetablemodelyaratma(self)
        self.treetablemodelyaratma2(model)
        self.treeWidget.setModel(model)

        # Buton clickleri
        self.treeWidget.doubleClicked.connect(self.on_doubleClicked)
        self.tshirteklebuton.clicked.connect(self.eklebuton)
        self.tshirtsilbuton.clicked.connect(self.silbuton)
        self.tshirtduzenlebuton.clicked.connect(self.duzenlebuton)

    def treetablemodelyaratma(self, parent):
        model = QStandardItemModel(0, 4, parent)
        model.setHeaderData(self.TSHIRTID, Qt.Horizontal, "Tshirt id")
        model.setHeaderData(self.TSHIRTISIM, Qt.Horizontal, "Tshirt isim")
        model.setHeaderData(self.TSHIRTFIYAT, Qt.Horizontal, "Tshirt fiyat")
        model.setHeaderData(self.RESIMURL, Qt.Horizontal, "Tshirt Resimurl")

        return model

    def on_doubleClicked(self, index):
        item = self.treeWidget.currentIndex()
        item2 = item.model().itemFromIndex(index).text()

        self.tshirtidlineEdit.setText(item2)

        # tabloyu update etme yöntemı
        self.updateview()

    def eklebuton(self):
        if (self.tshirtfiyatlineEdit.text() =="" or self.tshirtisimlineEdit.text()=="" or self.tshirtresimurllineEdit.text()==""):
            return
        else:
            conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="bilisim_proje_odevi")
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            query = "INSERT INTO `t-shirt` (tshirt_isim, tshirt_fiyat,tshirt_resimurl) VALUES (%s,%s,%s)"

            val = (self.tshirtisimlineEdit.text(), self.tshirtfiyatlineEdit.text(), self.tshirtresimurllineEdit.text())
            cursor.execute(query, val)
            conn.commit()
            # tabloyu update etme yöntemı
            self.updateview()
            self.tshirtfiyatlineEdit.clear()
            self.tshirtisimlineEdit.clear()
            self.tshirtresimurllineEdit.clear()
            self.tshirtidlineEdit.clear()
    def silbuton(self):
        if (self.tshirtidlineEdit.text()==""):
            return
        else:

            conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="bilisim_proje_odevi")
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            query = "DELETE FROM `t-shirt` where tshirt_id=%s"

            val = (self.tshirtidlineEdit.text())
            cursor.execute(query,val)
            conn.commit()
            self.updateview()
            self.tshirtidlineEdit.clear()

    def duzenlebuton(self):
        if (self.tshirtidlineEdit.text()==""or self.tshirtfiyatlineEdit.text() == "" or self.tshirtisimlineEdit.text() == "" or self.tshirtresimurllineEdit.text() == ""):
            return
        else:
            conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="bilisim_proje_odevi")
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            query = "UPDATE `t-shirt` SET tshirt_isim=%s,tshirt_fiyat=%s,tshirt_resimurl=%s  where tshirt_id=%s"

            val = (self.tshirtisimlineEdit.text(),self.tshirtfiyatlineEdit.text(),self.tshirtresimurllineEdit.text(),self.tshirtidlineEdit.text())
            cursor.execute(query, val)
            conn.commit()
            self.updateview()
            self.tshirtidlineEdit.clear()
            self.tshirtfiyatlineEdit.clear()
            self.tshirtisimlineEdit.clear()
            self.tshirtresimurllineEdit.clear()
            self.tshirtidlineEdit.clear()

    def updateview(self):
        model = self.treetablemodelyaratma(self)
        self.treeWidget.setModel(model)
        self.treetablemodelyaratma2(model)

    def treetablemodelyaratma2(self, model):
        conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="bilisim_proje_odevi")

        cursor = conn.cursor(pymysql.cursors.DictCursor)

        query = "SELECT * FROM `t-shirt`"
        cursor.execute(query)

        data = cursor.fetchall()

        for row in data:
            model.insertRow(0)
            model.setData(model.index(0, self.TSHIRTID), row['tshirt_id'])
            model.setData(model.index(0, self.TSHIRTISIM), row['tshirt_isim'])
            model.setData(model.index(0, self.TSHIRTFIYAT), row['tshirt_fiyat'])
            model.setData(model.index(0, self.RESIMURL), row['tshirt_resimurl'])

    def retranslateUi(self, TshirtWindow):
        _translate = QtCore.QCoreApplication.translate
        TshirtWindow.setWindowTitle(_translate("TshirtWindow", "Tshirtwindow"))
        self.tshirtisimlabel.setText(_translate("TshirtWindow", "Tshirt isim:"))
        self.tshirtfyatlabel.setText(_translate("TshirtWindow", "Tshirt Fiyat:"))
        self.tshirtidlabel.setText(_translate("TshirtWindow", "ID:"))
        self.tshirtresimurllabel.setText(_translate("TshirtWindow", "Resim_Url"))
        self.tshirteklebuton.setText(_translate("TshirtWindow", "Ekle"))
        self.tshirtduzenlebuton.setText(_translate("TshirtWindow", "Düzenle"))
        self.tshirtsilbuton.setText(_translate("TshirtWindow", "Sil"))

        self.label.setText(_translate("TshirtWindow", "TAYFUN TESKTİL ÜRÜN DÜZENLEME"))
        self.label_3.setText(_translate("TshirtWindow", "T-SHİRT"))
        self.actionTshirt.setText(_translate("TshirtWindow", "Tshirt"))
        self.actionPantolon.setText(_translate("TshirtWindow", "Pantolon"))
        self.actionPoloshirt.setText(_translate("TshirtWindow", "Poloshirt"))
        self.actioncgiyim.setText(_translate("TshirtWindow", "İcgiyim"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    TshirtWindow = QtWidgets.QMainWindow()
    ui = Ui_TshirtWindow()
    ui.setupUi(TshirtWindow)
    TshirtWindow.show()
    sys.exit(app.exec_())
