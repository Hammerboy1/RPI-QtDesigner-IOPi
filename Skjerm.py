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
        self.Test2 = QtWidgets.QPushButton(Form)
        self.Test2.setGeometry(QtCore.QRect(270, 232, 91, 41))
        self.Test2.setObjectName("Test2")
        self.Test1 = QtWidgets.QPushButton(Form)
        self.Test1.setGeometry(QtCore.QRect(110, 230, 111, 41))
        self.Test1.setObjectName("Test1")
        self.label_1 = QtWidgets.QLabel(Form)
        self.label_1.setGeometry(QtCore.QRect(170, 60, 121, 111))
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Test2.setText(_translate("Form", "Test 2"))
        self.Test1.setText(_translate("Form", "Test 1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

