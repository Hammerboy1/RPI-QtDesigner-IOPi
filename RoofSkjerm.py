# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RoofSkjerm.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(535, 375)
        self.Test2 = QtWidgets.QPushButton(Form)
        self.Test2.setGeometry(QtCore.QRect(140, 310, 111, 61))
        self.Test2.setObjectName("Test2")
        self.Test1 = QtWidgets.QPushButton(Form)
        self.Test1.setGeometry(QtCore.QRect(0, 310, 131, 61))
        self.Test1.setObjectName("Test1")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 531, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 2, 1, 1)
        self.Test3 = QtWidgets.QPushButton(Form)
        self.Test3.setGeometry(QtCore.QRect(260, 310, 111, 61))
        self.Test3.setObjectName("Test3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Test2.setText(_translate("Form", "Test 2"))
        self.Test1.setText(_translate("Form", "Test 1"))
        self.label_2.setText(_translate("Form", "Label_2"))
        self.label_4.setText(_translate("Form", "Label_4"))
        self.label_5.setText(_translate("Form", "Label_5"))
        self.label_8.setText(_translate("Form", "Label_8"))
        self.label_7.setText(_translate("Form", "Label_7"))
        self.label_3.setText(_translate("Form", "Labe_3"))
        self.label_6.setText(_translate("Form", "Label_6"))
        self.label_1.setText(_translate("Form", "Label_1"))
        self.label_9.setText(_translate("Form", "Label_9"))
        self.Test3.setText(_translate("Form", "Test 3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
