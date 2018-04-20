# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Skjerm.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(463, 346)
        self.Red = QtWidgets.QPushButton(Form)
        self.Red.setGeometry(QtCore.QRect(270, 232, 91, 41))
        self.Red.setObjectName("Red")
        self.Green = QtWidgets.QPushButton(Form)
        self.Green.setGeometry(QtCore.QRect(90, 232, 111, 41))
        self.Green.setObjectName("Green")
        self.label_1 = QtWidgets.QLabel(Form)
        self.label_1.setGeometry(QtCore.QRect(170, 60, 121, 111))
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Red.setText(_translate("Form", "Red"))
        self.Green.setText(_translate("Form", "Green"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

