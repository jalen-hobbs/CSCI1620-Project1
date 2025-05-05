from PyQt6.QtWidgets import *
from atmGUI import *
from account import *


# noinspection PyInconsistentReturns,DuplicatedCode
class Logic(QMainWindow, Ui_ATM):
    def __init__(self) -> None:
        """
        Initializes the GUI and the logic behind it.

        :return: None
        """
        super().__init__()
        self.setupUi(self)
        self.__member = None
        '''self.__member type should be BankMember object. Created when 'search' method is ran.'''

        self.searchButton.clicked.connect(lambda: self.search())
        self.enterButton.clicked.connect(lambda: self.enterFunction())
        self.clearButton.clicked.connect(lambda: self.clearFunction())

    def clearCache(self) -> None:
        """
        Clears the selected account from the cache.

        :return: None
        """
        self.__member = None
        self.amountBox.setText("")
        self.balanceLabel.setText("Awaiting account details.")
        self.questionLabel.setText("What would you like to do?")

    def search(self) -> None:
        """
        Searches for the bank member and creates a BankMember object. Called when the search button is pressed.
        Displays information about the account.

        :return: None
        """
        try:
            self.guiAccountModification(False)
            self.clearCache()

            first_name = self.firstNameBox.text().strip().upper()
            last_name = self.lastNameBox.text().strip().upper()
            pin = self.pinBox.text().strip()

            self.__member = BankMember(first_name, last_name, pin)
            if self.__member.get_MemberStatus() == 'Found':
                self.accountStatusLabel.setText(f'Hello {first_name} {last_name}!')
                self.updateAccountBalance()
                self.guiAccountModification(True)
            elif self.__member.get_MemberStatus() == 'None':
                self.accountStatusLabel.setText('Account not found. Please try again.')
            elif self.__member.get_MemberStatus() == 'InvalidPIN':
                self.accountStatusLabel.setText('Incorrect PIN.')
        except FileNotFoundError:
            self.accountStatusLabel.setText('ERROR: Database file not found!')
            print('Error generated! Database file not found!')

    def updateAccountBalance(self) -> None:
        """
        Method to update the account balance label.

        :return: None
        """
        checking_balance = self.__member.get_CheckingBalance()
        savings_balance = self.__member.get_SavingsBalance()
        total_balance = checking_balance + savings_balance
        self.balanceLabel.setText(f'Account balance- Checking: ${checking_balance:.2f} | '
                                  f'Savings: ${savings_balance:.2f} | Total: ${total_balance:.2f}')

    def enterFunction(self) -> None:
        """
        Will execute account changes based on the user's input. Called when the enter button is pressed.
        Handled using methods of BankMember class.

        :return: None
        """
        mod_type : str = ""
        selected_account : str = ""
        try:
            if self.checkingRadio.isChecked() == False and self.savingsRadio.isChecked() == False:
                raise Exception("Must select an account type to proceed")
            if self.depositRadio.isChecked() == False and self.withdrawRadio.isChecked() == False:
                raise Exception("Must select an action to proceed. (Deposit or Withdrawal)")

            amount = float(self.amountBox.text().strip())

            if self.depositRadio.isChecked(): mod_type = "deposit"
            if self.withdrawRadio.isChecked(): mod_type = "withdraw"
            if self.checkingRadio.isChecked(): selected_account = "checking"
            if self.savingsRadio.isChecked(): selected_account = "savings"

            if mod_type == "deposit":
                result = self.__member.deposit(amount, selected_account)
                if result:
                    self.updateAccountBalance()
                    self.questionLabel.setText("Deposit successful!")
            elif mod_type == "withdraw":
                result = self.__member.withdraw(amount, selected_account)
                if result:
                    self.updateAccountBalance()
                    self.questionLabel.setText("Withdrawal successful!")
                else:
                    if selected_account == 'checking':
                        self.questionLabel.setText("Not enough funds to withdraw the amount specified. Please try again!")
                    elif selected_account == 'savings':
                        self.questionLabel.setText("Not enough funds to withdraw the amount specified. Savings account minimum is $100.")
                    else:
                        raise Exception()

        except ValueError:
            print(f'Error generated! User entered invalid data form in balance box.')
            self.questionLabel.setText("ERROR: You must enter a number!")
        except Exception as e:
            print(f'Error generated! {e}')
            self.questionLabel.setText(f"ERROR: {e}!")

    def clearFunction(self) -> None:
        """
        Will reset the GUI to its original state. Called when the clear button is pressed.
        Also runs the clearCache method.

        :return: None
        """
        self.clearCache()
        self.guiAccountModification(False)
        self.firstNameBox.setText("")
        self.lastNameBox.setText("")
        self.pinBox.setText("")
        self.amountBox.setText("")
        self.firstNameBox.setFocus()
        self.accountStatusLabel.setText("Please enter your account information.")

    def guiAccountModification(self, option : bool) -> None:
        """
        Method to enable/disable the account modification GUI elements.

        :param option: Boolean value to enable/disable the GUI elements.

        :return: None
        """
        if option:
            self.withdrawRadio.setCheckable(True)
            self.depositRadio.setCheckable(True)
            self.checkingRadio.setCheckable(True)
            self.savingsRadio.setCheckable(True)
            self.amountBox.setReadOnly(False)
            self.enterButton.setEnabled(True)
            self.questionLabel.setEnabled(True)
            self.withdrawRadio.setEnabled(True)
            self.depositRadio.setEnabled(True)
            self.checkingRadio.setEnabled(True)
            self.savingsRadio.setEnabled(True)
            self.amountBox.setEnabled(True)
            self.amountLabel.setEnabled(True)
            self.balanceLabel.setEnabled(True)
        else:
            self.withdrawRadio.setCheckable(False)
            self.depositRadio.setCheckable(False)
            self.checkingRadio.setCheckable(False)
            self.savingsRadio.setCheckable(False)
            self.amountBox.setReadOnly(True)
            self.enterButton.setEnabled(False)
            self.questionLabel.setEnabled(False)
            self.withdrawRadio.setEnabled(False)
            self.depositRadio.setEnabled(False)
            self.checkingRadio.setEnabled(False)
            self.savingsRadio.setEnabled(False)
            self.amountBox.setEnabled(False)
            self.amountLabel.setEnabled(False)
            self.balanceLabel.setEnabled(False)