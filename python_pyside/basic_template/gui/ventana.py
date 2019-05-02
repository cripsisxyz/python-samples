# -*- coding: utf-8 -*-

#
# Created: Thu May 02 13:13:44 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1175, 243)
        self.BotonEjecutar = QtGui.QPushButton(Form)
        self.BotonEjecutar.setGeometry(QtCore.QRect(10, 100, 441, 41))
        self.BotonEjecutar.setObjectName("BotonEjecutar")
        self.CampoLog = QtGui.QPlainTextEdit(Form)
        self.CampoLog.setGeometry(QtCore.QRect(470, 20, 691, 201))
        self.CampoLog.setReadOnly(True)
        self.CampoLog.setObjectName("CampoLog")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "PyQT Sample", None, QtGui.QApplication.UnicodeUTF8))
        self.BotonEjecutar.setText(QtGui.QApplication.translate("Form", "Ejecutar acción", None, QtGui.QApplication.UnicodeUTF8))

