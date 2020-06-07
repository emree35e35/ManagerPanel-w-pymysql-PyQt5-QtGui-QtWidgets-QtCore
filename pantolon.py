# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\emree\Desktop\logindesignpantolon.ui'
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


class Ui_PantolonWindow(QWidget):
    PANTOLONID, PANTOLONISIM, PANTOLONFIYAT, RESIMURL = range(4)

    def setupUi(self, PantolonWindow):
        PantolonWindow.setObjectName("PantolonWindow")
        PantolonWindow.resize(997, 704)
        PantolonWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(PantolonWindow)
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
        self.pantolonisimlineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pantolonisimlineEdit.setFont(font)
        self.pantolonisimlineEdit.setObjectName("pantolonisimlineEdit")
        self.gridLayout_3.addWidget(self.pantolonisimlineEdit, 1, 1, 1, 1)
        self.pantolonisimlabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pantolonisimlabel.setFont(font)
        self.pantolonisimlabel.setObjectName("pantolonisimlabel")
        self.gridLayout_3.addWidget(self.pantolonisimlabel, 1, 0, 1, 1)
        self.pantolonfyatlabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pantolonfyatlabel.setFont(font)
        self.pantolonfyatlabel.setObjectName("pantolonfyatlabel")
        self.gridLayout_3.addWidget(self.pantolonfyatlabel, 2, 0, 1, 1)
        self.pantolonidlineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.pantolonidlineEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pantolonidlineEdit.setFont(font)
        self.pantolonidlineEdit.setObjectName("pantolonidlineEdit")
        self.gridLayout_3.addWidget(self.pantolonidlineEdit, 0, 1, 1, 1)
        self.pantolonidlabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pantolonidlabel.setFont(font)
        self.pantolonidlabel.setObjectName("pantolonidlabel")
        self.gridLayout_3.addWidget(self.pantolonidlabel, 0, 0, 1, 1)
        self.pantolonfiyatlineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pantolonfiyatlineEdit.setFont(font)
        self.pantolonfiyatlineEdit.setObjectName("pantolonfiyatlineEdit")
        self.gridLayout_3.addWidget(self.pantolonfiyatlineEdit, 2, 1, 1, 1)
        self.pantolonresimurllineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pantolonresimurllineEdit.setFont(font)
        self.pantolonresimurllineEdit.setObjectName("pantolonresimurllineEdit")
        self.gridLayout_3.addWidget(self.pantolonresimurllineEdit, 3, 1, 1, 1)
        self.pantolonresimurllabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pantolonresimurllabel.setFont(font)
        self.pantolonresimurllabel.setObjectName("pantolonresimurllabel")
        self.gridLayout_3.addWidget(self.pantolonresimurllabel, 3, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(419, 410, 211, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pantoloneklebuton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pantoloneklebuton.setFont(font)
        self.pantoloneklebuton.setObjectName("pantoloneklebuton")
        self.verticalLayout.addWidget(self.pantoloneklebuton)
        self.pantolonduzenlebuton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pantolonduzenlebuton.setFont(font)
        self.pantolonduzenlebuton.setObjectName("pantolonduzenlebuton")
        self.verticalLayout.addWidget(self.pantolonduzenlebuton)
        self.pantolonsilbuton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pantolonsilbuton.setFont(font)
        self.pantolonsilbuton.setObjectName("pantolonsilbuton")
        self.verticalLayout.addWidget(self.pantolonsilbuton)
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
        PantolonWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PantolonWindow)
        self.statusbar.setObjectName("statusbar")
        PantolonWindow.setStatusBar(self.statusbar)
        self.actionPantolon = QtWidgets.QAction(PantolonWindow)
        self.actionPantolon.setObjectName("actionPantolon")
        self.actionPantolon = QtWidgets.QAction(PantolonWindow)
        self.actionPantolon.setObjectName("actionPantolon")
        self.actionPoloshirt = QtWidgets.QAction(PantolonWindow)
        self.actionPoloshirt.setObjectName("actionPoloshirt")
        self.actioncgiyim = QtWidgets.QAction(PantolonWindow)
        self.actioncgiyim.setObjectName("actioncgiyim")
        self.retranslateUi(PantolonWindow)
        QtCore.QMetaObject.connectSlotsByName(PantolonWindow)

        #SORT  SIRALAMA
        self.treeWidget.setSortingEnabled(True)

        #only int
        self.onlyInt = QIntValidator()
        self.pantolonfiyatlineEdit.setValidator(self.onlyInt)

        # bu kısmı kullan nolur
        model = self.treetablemodelyaratma(self)
        self.treetablemodelyaratma2(model)
        self.treeWidget.setModel(model)

        # Buton clickleri
        self.treeWidget.doubleClicked.connect(self.on_doubleClicked)
        self.pantoloneklebuton.clicked.connect(self.eklebuton)
        self.pantolonsilbuton.clicked.connect(self.silbuton)
        self.pantolonduzenlebuton.clicked.connect(self.duzenlebuton)

    def treetablemodelyaratma(self, parent):
        model = QStandardItemModel(0, 4, parent)
        model.setHeaderData(self.PANTOLONID, Qt.Horizontal, "Pantolon id")
        model.setHeaderData(self.PANTOLONISIM, Qt.Horizontal, "Pantolon isim")
        model.setHeaderData(self.PANTOLONFIYAT, Qt.Horizontal, "Pantolon fiyat")
        model.setHeaderData(self.RESIMURL, Qt.Horizontal, "Pantolon Resimurl")

        return model

    def on_doubleClicked(self, index):
        item = self.treeWidget.currentIndex()
        item2 = item.model().itemFromIndex(index).text()

        self.pantolonidlineEdit.setText(item2)

        # tabloyu update etme yöntemı
        self.updateview()

    def eklebuton(self):
        if (self.pantolonfiyatlineEdit.text() =="" or self.pantolonisimlineEdit.text()=="" or self.pantolonresimurllineEdit.text()==""):
            return
        else:
            conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="bilisim_proje_odevi")
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            query = "INSERT INTO `pantolon` (pantolon_isim, pantolon_fiyat,pantolon_resimurl) VALUES (%s,%s,%s)"

            val = (self.pantolonisimlineEdit.text(), self.pantolonfiyatlineEdit.text(), self.pantolonresimurllineEdit.text())
            cursor.execute(query, val)
            conn.commit()
            # tabloyu update etme yöntemı
            self.updateview()
            self.pantolonfiyatlineEdit.clear()
            self.pantolonisimlineEdit.clear()
            self.pantolonresimurllineEdit.clear()
            self.pantolonidlineEdit.clear()
    def silbuton(self):
        if (self.pantolonidlineEdit.text()==""):
            return
        else:

            conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="bilisim_proje_odevi")
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            query = "DELETE FROM `pantolon` where pantolon_id=%s"

            val = (self.pantolonidlineEdit.text())
            cursor.execute(query,val)
            conn.commit()
            self.updateview()
            self.pantolonidlineEdit.clear()

    def duzenlebuton(self):
        if (self.pantolonidlineEdit.text()==""or self.pantolonfiyatlineEdit.text() == "" or self.pantolonisimlineEdit.text() == "" or self.pantolonresimurllineEdit.text() == ""):
            return
        else:
            conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="bilisim_proje_odevi")
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            query = "UPDATE `pantolon` SET pantolon_isim=%s,pantolon_fiyat=%s,pantolon_resimurl=%s  where pantolon_id=%s"

            val = (self.pantolonisimlineEdit.text(),self.pantolonfiyatlineEdit.text(),self.pantolonresimurllineEdit.text(),self.pantolonidlineEdit.text())
            cursor.execute(query, val)
            conn.commit()
            self.updateview()
            self.pantolonidlineEdit.clear()
            self.pantolonfiyatlineEdit.clear()
            self.pantolonisimlineEdit.clear()
            self.pantolonresimurllineEdit.clear()
            self.pantolonidlineEdit.clear()

    def updateview(self):
        model = self.treetablemodelyaratma(self)
        self.treeWidget.setModel(model)
        self.treetablemodelyaratma2(model)

    def treetablemodelyaratma2(self, model):
        conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="bilisim_proje_odevi")

        cursor = conn.cursor(pymysql.cursors.DictCursor)

        query = "SELECT * FROM `pantolon`"
        cursor.execute(query)

        data = cursor.fetchall()

        for row in data:
            model.insertRow(0)
            model.setData(model.index(0, self.PANTOLONID), row['pantolon_id'])
            model.setData(model.index(0, self.PANTOLONISIM), row['pantolon_isim'])
            model.setData(model.index(0, self.PANTOLONFIYAT), row['pantolon_fiyat'])
            model.setData(model.index(0, self.RESIMURL), row['pantolon_resimurl'])

    def retranslateUi(self, PantolonWindow):
        _translate = QtCore.QCoreApplication.translate
        PantolonWindow.setWindowTitle(_translate("PantolonWindow", "Pantolonwindow"))
        self.pantolonisimlabel.setText(_translate("PantolonWindow", "Pantolon isim:"))
        self.pantolonfyatlabel.setText(_translate("PantolonWindow", "Pantolon Fiyat:"))
        self.pantolonidlabel.setText(_translate("PantolonWindow", "ID:"))
        self.pantolonresimurllabel.setText(_translate("PantolonWindow", "Resim_Url"))
        self.pantoloneklebuton.setText(_translate("PantolonWindow", "Ekle"))
        self.pantolonduzenlebuton.setText(_translate("PantolonWindow", "Düzenle"))
        self.pantolonsilbuton.setText(_translate("PantolonWindow", "Sil"))

        self.label.setText(_translate("PantolonWindow", "TAYFUN TESKTİL ÜRÜN DÜZENLEME"))
        self.label_3.setText(_translate("PantolonWindow", "PANTOLON"))
        self.actionPantolon.setText(_translate("PantolonWindow", "Pantolon"))
        self.actionPantolon.setText(_translate("PantolonWindow", "Pantolon"))
        self.actionPoloshirt.setText(_translate("PantolonWindow", "Poloshirt"))
        self.actioncgiyim.setText(_translate("PantolonWindow", "İcgiyim"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    PantolonWindow = QtWidgets.QMainWindow()
    ui = Ui_PantolonWindow()
    ui.setupUi(PantolonWindow)
    PantolonWindow.show()
    sys.exit(app.exec_())
