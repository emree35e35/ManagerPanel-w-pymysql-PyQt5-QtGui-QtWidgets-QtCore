# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\emree\Desktop\logindesignicgiyim.ui'
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


class Ui_IcgiyimWindow(QWidget):
    ICGIYIMID, ICGIYIMISIM, ICGIYIMFIYAT, RESIMURL = range(4)

    def setupUi(self, IcgiyimWindow):
        IcgiyimWindow.setObjectName("IcgiyimWindow")
        IcgiyimWindow.resize(997, 704)
        IcgiyimWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(IcgiyimWindow)
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
        self.icgiyimisimlineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.icgiyimisimlineEdit.setFont(font)
        self.icgiyimisimlineEdit.setObjectName("icgiyimisimlineEdit")
        self.gridLayout_3.addWidget(self.icgiyimisimlineEdit, 1, 1, 1, 1)
        self.icgiyimisimlabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.icgiyimisimlabel.setFont(font)
        self.icgiyimisimlabel.setObjectName("icgiyimisimlabel")
        self.gridLayout_3.addWidget(self.icgiyimisimlabel, 1, 0, 1, 1)
        self.icgiyimfyatlabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.icgiyimfyatlabel.setFont(font)
        self.icgiyimfyatlabel.setObjectName("icgiyimfyatlabel")
        self.gridLayout_3.addWidget(self.icgiyimfyatlabel, 2, 0, 1, 1)
        self.icgiyimidlineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.icgiyimidlineEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.icgiyimidlineEdit.setFont(font)
        self.icgiyimidlineEdit.setObjectName("icgiyimidlineEdit")
        self.gridLayout_3.addWidget(self.icgiyimidlineEdit, 0, 1, 1, 1)
        self.icgiyimidlabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.icgiyimidlabel.setFont(font)
        self.icgiyimidlabel.setObjectName("icgiyimidlabel")
        self.gridLayout_3.addWidget(self.icgiyimidlabel, 0, 0, 1, 1)
        self.icgiyimfiyatlineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.icgiyimfiyatlineEdit.setFont(font)
        self.icgiyimfiyatlineEdit.setObjectName("icgiyimfiyatlineEdit")
        self.gridLayout_3.addWidget(self.icgiyimfiyatlineEdit, 2, 1, 1, 1)
        self.icgiyimresimurllineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.icgiyimresimurllineEdit.setFont(font)
        self.icgiyimresimurllineEdit.setObjectName("icgiyimresimurllineEdit")
        self.gridLayout_3.addWidget(self.icgiyimresimurllineEdit, 3, 1, 1, 1)
        self.icgiyimresimurllabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.icgiyimresimurllabel.setFont(font)
        self.icgiyimresimurllabel.setObjectName("icgiyimresimurllabel")
        self.gridLayout_3.addWidget(self.icgiyimresimurllabel, 3, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(419, 410, 211, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.icgiyimeklebuton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.icgiyimeklebuton.setFont(font)
        self.icgiyimeklebuton.setObjectName("icgiyimeklebuton")
        self.verticalLayout.addWidget(self.icgiyimeklebuton)
        self.icgiyimduzenlebuton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.icgiyimduzenlebuton.setFont(font)
        self.icgiyimduzenlebuton.setObjectName("icgiyimduzenlebuton")
        self.verticalLayout.addWidget(self.icgiyimduzenlebuton)
        self.icgiyimsilbuton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.icgiyimsilbuton.setFont(font)
        self.icgiyimsilbuton.setObjectName("icgiyimsilbuton")
        self.verticalLayout.addWidget(self.icgiyimsilbuton)
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
        IcgiyimWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(IcgiyimWindow)
        self.statusbar.setObjectName("statusbar")
        IcgiyimWindow.setStatusBar(self.statusbar)
        self.actionIcgiyim = QtWidgets.QAction(IcgiyimWindow)
        self.actionIcgiyim.setObjectName("actionIcgiyim")
        self.actionIcgiyim = QtWidgets.QAction(IcgiyimWindow)
        self.actionIcgiyim.setObjectName("actionIcgiyim")
        self.actionPoloshirt = QtWidgets.QAction(IcgiyimWindow)
        self.actionPoloshirt.setObjectName("actionPoloshirt")
        self.actioncgiyim = QtWidgets.QAction(IcgiyimWindow)
        self.actioncgiyim.setObjectName("actioncgiyim")
        self.retranslateUi(IcgiyimWindow)
        QtCore.QMetaObject.connectSlotsByName(IcgiyimWindow)

        #SORT  SIRALAMA
        self.treeWidget.setSortingEnabled(True)

        #only int
        self.onlyInt = QIntValidator()
        self.icgiyimfiyatlineEdit.setValidator(self.onlyInt)

        # bu kısmı kullan nolur
        model = self.treetablemodelyaratma(self)
        self.treetablemodelyaratma2(model)
        self.treeWidget.setModel(model)

        # Buton clickleri
        self.treeWidget.doubleClicked.connect(self.on_doubleClicked)
        self.icgiyimeklebuton.clicked.connect(self.eklebuton)
        self.icgiyimsilbuton.clicked.connect(self.silbuton)
        self.icgiyimduzenlebuton.clicked.connect(self.duzenlebuton)

    def treetablemodelyaratma(self, parent):
        model = QStandardItemModel(0, 4, parent)
        model.setHeaderData(self.ICGIYIMID, Qt.Horizontal, "İçgiyim id")
        model.setHeaderData(self.ICGIYIMISIM, Qt.Horizontal, "İçgiyim isim")
        model.setHeaderData(self.ICGIYIMFIYAT, Qt.Horizontal, "İçgiyim fiyat")
        model.setHeaderData(self.RESIMURL, Qt.Horizontal, "İçgiyim Resimurl")

        return model

    def on_doubleClicked(self, index):
        item = self.treeWidget.currentIndex()
        item2 = item.model().itemFromIndex(index).text()

        self.icgiyimidlineEdit.setText(item2)

        # tabloyu update etme yöntemı
        self.updateview()

    def eklebuton(self):
        if (self.icgiyimfiyatlineEdit.text() =="" or self.icgiyimisimlineEdit.text()=="" or self.icgiyimresimurllineEdit.text()==""):
            return
        else:
            conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="bilisim_proje_odevi")
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            query = "INSERT INTO `icgiyim` (icgiyim_isim, icgiyim_fiyat,icgiyim_resimurl) VALUES (%s,%s,%s)"

            val = (self.icgiyimisimlineEdit.text(), self.icgiyimfiyatlineEdit.text(), self.icgiyimresimurllineEdit.text())
            cursor.execute(query, val)
            conn.commit()
            # tabloyu update etme yöntemı
            self.updateview()
            self.icgiyimfiyatlineEdit.clear()
            self.icgiyimisimlineEdit.clear()
            self.icgiyimresimurllineEdit.clear()
            self.icgiyimidlineEdit.clear()
    def silbuton(self):
        if (self.icgiyimidlineEdit.text()==""):
            return
        else:

            conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="bilisim_proje_odevi")
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            query = "DELETE FROM `icgiyim` where id=%s"

            val = (self.icgiyimidlineEdit.text())
            cursor.execute(query,val)
            conn.commit()
            self.updateview()
            self.icgiyimidlineEdit.clear()

    def duzenlebuton(self):
        if (self.icgiyimidlineEdit.text()==""or self.icgiyimfiyatlineEdit.text() == "" or self.icgiyimisimlineEdit.text() == "" or self.icgiyimresimurllineEdit.text() == ""):
            return
        else:
            conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="bilisim_proje_odevi")
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            query = "UPDATE `icgiyim` SET icgiyim_isim=%s,icgiyim_fiyat=%s,icgiyim_resimurl=%s  where id=%s"

            val = (self.icgiyimisimlineEdit.text(),self.icgiyimfiyatlineEdit.text(),self.icgiyimresimurllineEdit.text(),self.icgiyimidlineEdit.text())
            cursor.execute(query, val)
            conn.commit()
            self.updateview()
            self.icgiyimidlineEdit.clear()
            self.icgiyimfiyatlineEdit.clear()
            self.icgiyimisimlineEdit.clear()
            self.icgiyimresimurllineEdit.clear()
            self.icgiyimidlineEdit.clear()

    def updateview(self):
        model = self.treetablemodelyaratma(self)
        self.treeWidget.setModel(model)
        self.treetablemodelyaratma2(model)

    def treetablemodelyaratma2(self, model):
        conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="bilisim_proje_odevi")

        cursor = conn.cursor(pymysql.cursors.DictCursor)

        query = "SELECT * FROM `icgiyim`"
        cursor.execute(query)

        data = cursor.fetchall()

        for row in data:
            model.insertRow(0)
            model.setData(model.index(0, self.ICGIYIMID), row['id'])
            model.setData(model.index(0, self.ICGIYIMISIM), row['icgiyim_isim'])
            model.setData(model.index(0, self.ICGIYIMFIYAT), row['icgiyim_fiyat'])
            model.setData(model.index(0, self.RESIMURL), row['icgiyim_resimurl'])

    def retranslateUi(self, IcgiyimWindow):
        _translate = QtCore.QCoreApplication.translate
        IcgiyimWindow.setWindowTitle(_translate("IcgiyimWindow", "İçgiyim Form"))
        self.icgiyimisimlabel.setText(_translate("IcgiyimWindow", "Icgiyim isim:"))
        self.icgiyimfyatlabel.setText(_translate("IcgiyimWindow", "Icgiyim Fiyat:"))
        self.icgiyimidlabel.setText(_translate("IcgiyimWindow", "ID:"))
        self.icgiyimresimurllabel.setText(_translate("IcgiyimWindow", "Resim_Url"))
        self.icgiyimeklebuton.setText(_translate("IcgiyimWindow", "Ekle"))
        self.icgiyimduzenlebuton.setText(_translate("IcgiyimWindow", "Düzenle"))
        self.icgiyimsilbuton.setText(_translate("IcgiyimWindow", "Sil"))

        self.label.setText(_translate("IcgiyimWindow", "TAYFUN TESKTİL ÜRÜN DÜZENLEME"))
        self.label_3.setText(_translate("IcgiyimWindow", "ICGIYIM"))
        self.actionIcgiyim.setText(_translate("IcgiyimWindow", "Icgiyim"))
        self.actionIcgiyim.setText(_translate("IcgiyimWindow", "Icgiyim"))
        self.actionPoloshirt.setText(_translate("IcgiyimWindow", "Poloshirt"))
        self.actioncgiyim.setText(_translate("IcgiyimWindow", "İcgiyim"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    IcgiyimWindow = QtWidgets.QMainWindow()
    ui = Ui_IcgiyimWindow()
    ui.setupUi(IcgiyimWindow)
    IcgiyimWindow.show()
    sys.exit(app.exec_())
