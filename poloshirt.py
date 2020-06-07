# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\emree\Desktop\logindesignpoloshirt.ui'
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


class Ui_PoloshirtWindow(QWidget):
    POLOSHİRTID, POLOSHİRTISIM, POLOSHİRTFIYAT, RESIMURL = range(4)

    def setupUi(self, PoloshirtWindow):
        PoloshirtWindow.setObjectName("PoloshirtWindow")
        PoloshirtWindow.resize(997, 704)
        PoloshirtWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(PoloshirtWindow)
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
        self.poloshirtisimlineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.poloshirtisimlineEdit.setFont(font)
        self.poloshirtisimlineEdit.setObjectName("poloshirtisimlineEdit")
        self.gridLayout_3.addWidget(self.poloshirtisimlineEdit, 1, 1, 1, 1)
        self.poloshirtisimlabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.poloshirtisimlabel.setFont(font)
        self.poloshirtisimlabel.setObjectName("poloshirtisimlabel")
        self.gridLayout_3.addWidget(self.poloshirtisimlabel, 1, 0, 1, 1)
        self.poloshirtfyatlabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.poloshirtfyatlabel.setFont(font)
        self.poloshirtfyatlabel.setObjectName("poloshirtfyatlabel")
        self.gridLayout_3.addWidget(self.poloshirtfyatlabel, 2, 0, 1, 1)
        self.poloshirtidlineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.poloshirtidlineEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.poloshirtidlineEdit.setFont(font)
        self.poloshirtidlineEdit.setObjectName("poloshirtidlineEdit")
        self.gridLayout_3.addWidget(self.poloshirtidlineEdit, 0, 1, 1, 1)
        self.poloshirtidlabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.poloshirtidlabel.setFont(font)
        self.poloshirtidlabel.setObjectName("poloshirtidlabel")
        self.gridLayout_3.addWidget(self.poloshirtidlabel, 0, 0, 1, 1)
        self.poloshirtfiyatlineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.poloshirtfiyatlineEdit.setFont(font)
        self.poloshirtfiyatlineEdit.setObjectName("poloshirtfiyatlineEdit")
        self.gridLayout_3.addWidget(self.poloshirtfiyatlineEdit, 2, 1, 1, 1)
        self.poloshirtresimurllineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.poloshirtresimurllineEdit.setFont(font)
        self.poloshirtresimurllineEdit.setObjectName("poloshirtresimurllineEdit")
        self.gridLayout_3.addWidget(self.poloshirtresimurllineEdit, 3, 1, 1, 1)
        self.poloshirtresimurllabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.poloshirtresimurllabel.setFont(font)
        self.poloshirtresimurllabel.setObjectName("poloshirtresimurllabel")
        self.gridLayout_3.addWidget(self.poloshirtresimurllabel, 3, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(419, 410, 211, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.poloshirteklebuton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.poloshirteklebuton.setFont(font)
        self.poloshirteklebuton.setObjectName("poloshirteklebuton")
        self.verticalLayout.addWidget(self.poloshirteklebuton)
        self.poloshirtduzenlebuton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.poloshirtduzenlebuton.setFont(font)
        self.poloshirtduzenlebuton.setObjectName("poloshirtduzenlebuton")
        self.verticalLayout.addWidget(self.poloshirtduzenlebuton)
        self.poloshirtsilbuton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.poloshirtsilbuton.setFont(font)
        self.poloshirtsilbuton.setObjectName("poloshirtsilbuton")
        self.verticalLayout.addWidget(self.poloshirtsilbuton)
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
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 70, 170, 51))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setObjectName("label_3")
        PoloshirtWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PoloshirtWindow)
        self.statusbar.setObjectName("statusbar")
        PoloshirtWindow.setStatusBar(self.statusbar)
        self.actionPoloshirt = QtWidgets.QAction(PoloshirtWindow)
        self.actionPoloshirt.setObjectName("actionPoloshirt")
        self.actionPoloshirt = QtWidgets.QAction(PoloshirtWindow)
        self.actionPoloshirt.setObjectName("actionPoloshirt")
        self.actionPoloshirt = QtWidgets.QAction(PoloshirtWindow)
        self.actionPoloshirt.setObjectName("actionPoloshirt")
        self.actioncgiyim = QtWidgets.QAction(PoloshirtWindow)
        self.actioncgiyim.setObjectName("actioncgiyim")
        self.retranslateUi(PoloshirtWindow)
        QtCore.QMetaObject.connectSlotsByName(PoloshirtWindow)

        #SORT  SIRALAMA
        self.treeWidget.setSortingEnabled(True)

        #only int
        self.onlyInt = QIntValidator()
        self.poloshirtfiyatlineEdit.setValidator(self.onlyInt)

        # bu kısmı kullan nolur
        model = self.treetablemodelyaratma(self)
        self.treetablemodelyaratma2(model)
        self.treeWidget.setModel(model)

        # Buton clickleri
        self.treeWidget.doubleClicked.connect(self.on_doubleClicked)
        self.poloshirteklebuton.clicked.connect(self.eklebuton)
        self.poloshirtsilbuton.clicked.connect(self.silbuton)
        self.poloshirtduzenlebuton.clicked.connect(self.duzenlebuton)

    def treetablemodelyaratma(self, parent):
        model = QStandardItemModel(0, 4, parent)
        model.setHeaderData(self.POLOSHİRTID, Qt.Horizontal, "Poloshirt id")
        model.setHeaderData(self.POLOSHİRTISIM, Qt.Horizontal, "Poloshirt isim")
        model.setHeaderData(self.POLOSHİRTFIYAT, Qt.Horizontal, "Poloshirt fiyat")
        model.setHeaderData(self.RESIMURL, Qt.Horizontal, "Poloshirt Resimurl")

        return model

    def on_doubleClicked(self, index):
        item = self.treeWidget.currentIndex()
        item2 = item.model().itemFromIndex(index).text()

        self.poloshirtidlineEdit.setText(item2)

        # tabloyu update etme yöntemı
        self.updateview()

    def eklebuton(self):
        if (self.poloshirtfiyatlineEdit.text() =="" or self.poloshirtisimlineEdit.text()=="" or self.poloshirtresimurllineEdit.text()==""):
            return
        else:
            conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="bilisim_proje_odevi")
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            query = "INSERT INTO `poloshirt` (poloshirt_isim, poloshirt_fiyat,poloshirt_resimurl) VALUES (%s,%s,%s)"

            val = (self.poloshirtisimlineEdit.text(), self.poloshirtfiyatlineEdit.text(), self.poloshirtresimurllineEdit.text())
            cursor.execute(query, val)
            conn.commit()
            # tabloyu update etme yöntemı
            self.updateview()
            self.poloshirtfiyatlineEdit.clear()
            self.poloshirtisimlineEdit.clear()
            self.poloshirtresimurllineEdit.clear()
            self.poloshirtidlineEdit.clear()
    def silbuton(self):
        if (self.poloshirtidlineEdit.text()==""):
            return
        else:

            conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="bilisim_proje_odevi")
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            query = "DELETE FROM `poloshirt` where id=%s"

            val = (self.poloshirtidlineEdit.text())
            cursor.execute(query,val)
            conn.commit()
            self.updateview()
            self.poloshirtidlineEdit.clear()

    def duzenlebuton(self):
        if (self.poloshirtidlineEdit.text()==""or self.poloshirtfiyatlineEdit.text() == "" or self.poloshirtisimlineEdit.text() == "" or self.poloshirtresimurllineEdit.text() == ""):
            return
        else:
            conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="bilisim_proje_odevi")
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            query = "UPDATE `poloshirt` SET poloshirt_isim=%s,poloshirt_fiyat=%s,poloshirt_resimurl=%s  where id=%s"

            val = (self.poloshirtisimlineEdit.text(),self.poloshirtfiyatlineEdit.text(),self.poloshirtresimurllineEdit.text(),self.poloshirtidlineEdit.text())
            cursor.execute(query, val)
            conn.commit()
            self.updateview()
            self.poloshirtidlineEdit.clear()
            self.poloshirtfiyatlineEdit.clear()
            self.poloshirtisimlineEdit.clear()
            self.poloshirtresimurllineEdit.clear()
            self.poloshirtidlineEdit.clear()

    def updateview(self):
        model = self.treetablemodelyaratma(self)
        self.treeWidget.setModel(model)
        self.treetablemodelyaratma2(model)

    def treetablemodelyaratma2(self, model):
        conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="bilisim_proje_odevi")

        cursor = conn.cursor(pymysql.cursors.DictCursor)

        query = "SELECT * FROM `poloshirt`"
        cursor.execute(query)

        data = cursor.fetchall()

        for row in data:
            model.insertRow(0)
            model.setData(model.index(0, self.POLOSHİRTID), row['id'])
            model.setData(model.index(0, self.POLOSHİRTISIM), row['poloshirt_isim'])
            model.setData(model.index(0, self.POLOSHİRTFIYAT), row['poloshirt_fiyat'])
            model.setData(model.index(0, self.RESIMURL), row['poloshirt_resimurl'])

    def retranslateUi(self, PoloshirtWindow):
        _translate = QtCore.QCoreApplication.translate
        PoloshirtWindow.setWindowTitle(_translate("PoloshirtWindow", "Poloshirtwindow"))
        self.poloshirtisimlabel.setText(_translate("PoloshirtWindow", "Poloshirt isim:"))
        self.poloshirtfyatlabel.setText(_translate("PoloshirtWindow", "Poloshirt Fiyat:"))
        self.poloshirtidlabel.setText(_translate("PoloshirtWindow", "ID:"))
        self.poloshirtresimurllabel.setText(_translate("PoloshirtWindow", "Resim_Url"))
        self.poloshirteklebuton.setText(_translate("PoloshirtWindow", "Ekle"))
        self.poloshirtduzenlebuton.setText(_translate("PoloshirtWindow", "Düzenle"))
        self.poloshirtsilbuton.setText(_translate("PoloshirtWindow", "Sil"))

        self.label.setText(_translate("PoloshirtWindow", "TAYFUN TESKTİL ÜRÜN DÜZENLEME"))
        self.label_3.setText(_translate("PoloshirtWindow", "POLOSHİRT"))
        self.actionPoloshirt.setText(_translate("PoloshirtWindow", "Poloshirt"))
        self.actionPoloshirt.setText(_translate("PoloshirtWindow", "Poloshirt"))
        self.actionPoloshirt.setText(_translate("PoloshirtWindow", "Poloshirt"))
        self.actioncgiyim.setText(_translate("PoloshirtWindow", "İcgiyim"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    PoloshirtWindow = QtWidgets.QMainWindow()
    ui = Ui_PoloshirtWindow()
    ui.setupUi(PoloshirtWindow)
    PoloshirtWindow.show()
    sys.exit(app.exec_())
