# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from gui.ventana import Ui_Form
from lib.trenlr import Habla
import sys

class Interfaz(QtGui.QWidget, Ui_Form):

	def __init__(self):
		super(Interfaz, self).__init__()
		self.setupUi(self)
		
		QtCore.QObject.connect(self.BotonEjecutar, QtCore.SIGNAL ('clicked()'), self.starter)
		
	def starter(self):
		
		_blabla = Habla()
		self.CampoLog.appendPlainText(_blabla.saludar())
	
if __name__ == "__main__":

	app = QtGui.QApplication(sys.argv)
	ui = Interfaz()
	ui.show()
	sys.exit(app.exec_())