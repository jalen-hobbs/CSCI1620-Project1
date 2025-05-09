# Form implementation generated from reading ui file 'ATMui.ui'
#
# Created by: PyQt6 UI code generator 6.9.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ATM(object):
    def setupUi(self, ATM):
        ATM.setObjectName("ATM")
        ATM.setFixedSize(480, 640)
        font = QtGui.QFont()
        font.setFamily("Futura")
        ATM.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=ATM)
        self.centralwidget.setObjectName("centralwidget")
        self.windowLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.windowLabel.setGeometry(QtCore.QRect(70, 10, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(24)
        self.windowLabel.setFont(font)
        self.windowLabel.setObjectName("windowLabel")
        self.firstNameLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.firstNameLabel.setGeometry(QtCore.QRect(20, 80, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(18)
        self.firstNameLabel.setFont(font)
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.lastNameLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.lastNameLabel.setGeometry(QtCore.QRect(20, 120, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(18)
        self.lastNameLabel.setFont(font)
        self.lastNameLabel.setObjectName("lastNameLabel")
        self.pinLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.pinLabel.setGeometry(QtCore.QRect(20, 160, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(18)
        self.pinLabel.setFont(font)
        self.pinLabel.setObjectName("pinLabel")
        self.pinBox = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.pinBox.setGeometry(QtCore.QRect(130, 160, 113, 31))
        self.pinBox.setText("")
        self.pinBox.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.pinBox.setReadOnly(False)
        self.pinBox.setClearButtonEnabled(False)
        self.pinBox.setObjectName("pinBox")
        self.lastNameBox = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lastNameBox.setGeometry(QtCore.QRect(130, 120, 311, 31))
        self.lastNameBox.setObjectName("lastNameBox")
        self.firstNameBox = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.firstNameBox.setGeometry(QtCore.QRect(130, 80, 311, 31))
        self.firstNameBox.setObjectName("firstNameBox")
        self.searchButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(172, 210, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.searchButton.setFont(font)
        self.searchButton.setObjectName("searchButton")
        self.accountStatusLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.accountStatusLabel.setGeometry(QtCore.QRect(39, 270, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(18)
        self.accountStatusLabel.setFont(font)
        self.accountStatusLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.accountStatusLabel.setObjectName("accountStatusLabel")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 310, 441, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.questionLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.questionLabel.setEnabled(False)
        self.questionLabel.setGeometry(QtCore.QRect(40, 330, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(16)
        self.questionLabel.setFont(font)
        self.questionLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.questionLabel.setWordWrap(True)
        self.questionLabel.setObjectName("questionLabel")
        self.withdrawRadio = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.withdrawRadio.setEnabled(False)
        self.withdrawRadio.setGeometry(QtCore.QRect(280, 430, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(16)
        font.setUnderline(False)
        self.withdrawRadio.setFont(font)
        self.withdrawRadio.setCheckable(False)
        self.withdrawRadio.setObjectName("withdrawRadio")
        self.depositRadio = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.depositRadio.setEnabled(False)
        self.depositRadio.setGeometry(QtCore.QRect(140, 430, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(16)
        font.setUnderline(False)
        self.depositRadio.setFont(font)
        self.depositRadio.setCheckable(False)
        self.depositRadio.setObjectName("depositRadio")
        self.amountLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.amountLabel.setEnabled(False)
        self.amountLabel.setGeometry(QtCore.QRect(20, 470, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(18)
        self.amountLabel.setFont(font)
        self.amountLabel.setObjectName("amountLabel")
        self.amountBox = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.amountBox.setEnabled(False)
        self.amountBox.setGeometry(QtCore.QRect(130, 470, 311, 31))
        self.amountBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.amountBox.setReadOnly(True)
        self.amountBox.setObjectName("amountBox")
        self.enterButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.enterButton.setEnabled(False)
        self.enterButton.setGeometry(QtCore.QRect(70, 570, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.enterButton.setFont(font)
        self.enterButton.setObjectName("enterButton")
        self.clearButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(280, 570, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.clearButton.setFont(font)
        self.clearButton.setObjectName("clearButton")
        self.balanceLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.balanceLabel.setEnabled(False)
        self.balanceLabel.setGeometry(QtCore.QRect(40, 510, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(16)
        self.balanceLabel.setFont(font)
        self.balanceLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.balanceLabel.setWordWrap(True)
        self.balanceLabel.setObjectName("balanceLabel")
        self.savingsRadio = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.savingsRadio.setEnabled(False)
        self.savingsRadio.setGeometry(QtCore.QRect(280, 390, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(16)
        font.setUnderline(True)
        self.savingsRadio.setFont(font)
        self.savingsRadio.setCheckable(False)
        self.savingsRadio.setObjectName("savingsRadio")
        self.buttonGroup = QtWidgets.QButtonGroup(ATM)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.savingsRadio)
        self.checkingRadio = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.checkingRadio.setEnabled(False)
        self.checkingRadio.setGeometry(QtCore.QRect(80, 390, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(16)
        font.setUnderline(True)
        self.checkingRadio.setFont(font)
        self.checkingRadio.setCheckable(False)
        self.checkingRadio.setObjectName("checkingRadio")
        self.buttonGroup.addButton(self.checkingRadio)
        ATM.setCentralWidget(self.centralwidget)

        self.retranslateUi(ATM)
        QtCore.QMetaObject.connectSlotsByName(ATM)
        ATM.setTabOrder(self.firstNameBox, self.lastNameBox)
        ATM.setTabOrder(self.lastNameBox, self.pinBox)
        ATM.setTabOrder(self.pinBox, self.searchButton)
        ATM.setTabOrder(self.searchButton, self.checkingRadio)
        ATM.setTabOrder(self.checkingRadio, self.savingsRadio)
        ATM.setTabOrder(self.savingsRadio, self.depositRadio)
        ATM.setTabOrder(self.depositRadio, self.withdrawRadio)
        ATM.setTabOrder(self.withdrawRadio, self.amountBox)
        ATM.setTabOrder(self.amountBox, self.enterButton)
        ATM.setTabOrder(self.enterButton, self.clearButton)

    def retranslateUi(self, ATM):
        _translate = QtCore.QCoreApplication.translate
        ATM.setWindowTitle(_translate("ATM", "ATM"))
        self.windowLabel.setText(_translate("ATM", "Bank of Computer Science ATM"))
        self.firstNameLabel.setText(_translate("ATM", "First Name"))
        self.lastNameLabel.setText(_translate("ATM", "Last Name"))
        self.pinLabel.setText(_translate("ATM", "Enter PIN"))
        self.searchButton.setText(_translate("ATM", "SEARCH"))
        self.accountStatusLabel.setText(_translate("ATM", "Please enter your account information."))
        self.questionLabel.setText(_translate("ATM", "What would you like to do?"))
        self.withdrawRadio.setText(_translate("ATM", "Withdraw"))
        self.depositRadio.setText(_translate("ATM", "Deposit"))
        self.amountLabel.setText(_translate("ATM", "Amount      $"))
        self.enterButton.setText(_translate("ATM", "ENTER"))
        self.clearButton.setText(_translate("ATM", "CLEAR"))
        self.balanceLabel.setText(_translate("ATM", "Awaiting account details."))
        self.savingsRadio.setText(_translate("ATM", "Adjust Savings"))
        self.checkingRadio.setText(_translate("ATM", "Adjust Checking"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ATM = QtWidgets.QMainWindow()
    ui = Ui_ATM()
    ui.setupUi(ATM)
    ATM.show()
    sys.exit(app.exec())
