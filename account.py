from database import *

class BankMember:
    def __init__(self, first_name : str, last_name : str, pin : str) -> None:
        """
        Initializes the BankMember object. Checks if the account exists in the database.

        :param first_name: First name of account holder to search database.csv for.
        :param last_name: Last name of account holder to search database.csv for.
        :param pin: PIN of the account holder to search database.csv for.

        :return: None.
        """
        self.__member_first_name : str = first_name
        self.__member_last_name : str = last_name
        self.__member_pin : str = pin
        self.__checking_account_balance : float = 0
        self.__savings_account_balance : float = 0
        self.__savings_deposit_count : int = 0

        self.__SavingsMinimum : int = 100
        self.__SavingsRate : float = 0.02

        self.__member_status = ''
        self.__database_check = databaseRead(self.__member_first_name, self.__member_last_name, self.__member_pin)

        if self.__database_check == 'InvalidPIN':
            self.__member_status = 'InvalidPIN'
        elif self.__database_check is None:
            self.__member_status = 'None'
        elif self.__database_check[0] == 'Found':
            self.__member_status = 'Found'
            self.__checking_account_balance = self.__database_check[1]
            self.__savings_account_balance = self.__database_check[2]
            self.__savings_deposit_count = self.__database_check[3]

    def saveChanges(self) -> None:
        """
        Saves changes made to the account to the database.csv file.

        :return: None
        """
        databaseWrite(self.__member_first_name, self.__member_last_name, self.__member_pin,
                      self.__checking_account_balance, self.__savings_account_balance, self.__savings_deposit_count)
        self.refreshData()

    def refreshData(self) -> None:
        """
        Refreshes the data in the object to what is in the database.csv file.

        :return: None
        """
        self.__database_check = databaseRead(self.__member_first_name, self.__member_last_name, self.__member_pin)
        self.__checking_account_balance = self.__database_check[1]
        self.__savings_account_balance = self.__database_check[2]
        self.__savings_deposit_count = self.__database_check[3]

    def get_CheckingBalance(self) -> float:
        """
        Gets the balance of the checking account for the member.

        :return: Checking account balance (float)
        """
        return self.__checking_account_balance

    def get_SavingsBalance(self) -> float:
        """
        Gets the balance of the savings account for the member.

        :return: Savings account balance (float)
        """
        return self.__savings_account_balance

    def get_SavingsDepositCount(self) -> int:
        """
        Gets the number of times the savings account has been deposited.

        :return: Number of deposits in savings account (int)
        """
        return self.__savings_deposit_count

    def set_CheckingBalance(self, amount : float) -> None:
        """
        Sets the balance of the checking account for the member to the given amount.

        :param amount: The amount to set the checking balance to. (float)

        :return: None
        """
        self.__checking_account_balance = amount
        self.saveChanges()

    def set_SavingsBalance(self, amount : float) -> None:
        """
        Sets the balance of the savings account for the member to the given amount.

        :param amount: The amount to set the savings balance to. (float)

        :return: None
        """
        self.__savings_account_balance = amount if amount >= self.__SavingsMinimum else self.__SavingsRate
        self.saveChanges()

    def set_SavingsDepositCount(self, amount : int) -> None:
        """
        Sets the number of times the savings account has been deposited.

        :param amount: The amount to set the savings deposit count to. (int)

        :return: None.
        """
        self.__savings_deposit_count = amount
        self.saveChanges()

    def apply_SavingsInterest(self) -> None:
        """
        Method to apply interest to the savings account.
        Automatically called when the savings deposit count is divisible by 5.

        :return: None
        """
        self.refreshData()
        balance_with_interest = self.get_SavingsBalance() * (1 + self.__SavingsRate)
        self.set_SavingsBalance(balance_with_interest)

    def get_MemberStatus(self) -> str:
        """
        Gets the status of the member (found, invalid pin, none, etc.).

        :return: Member status (str)
        """
        return self.__member_status

    ## Deposit / Withdraw Methods

    def deposit(self, amount : float, account : str) -> bool:
        """
        Method to deposit money into a specific account. Should be the only method used to deposit money.

        :param amount: Amount of money to deposit.
        :param account: Account to deposit money into (checking or savings).

        :return: True if successful, False if not.
        """
        if account == 'checking':
            if amount > 0:
                self.refreshData()
                self.set_CheckingBalance(self.get_CheckingBalance() + amount)
                return True
        elif account == 'savings':
            if amount > 0:
                self.refreshData()
                self.set_SavingsBalance(self.get_SavingsBalance() + amount)
                self.set_SavingsDepositCount(self.get_SavingsDepositCount() + 1)
                if self.get_SavingsDepositCount() % 5 == 0:
                    self.apply_SavingsInterest()
                return True
        return False

    def withdraw(self, amount : float, account : str) -> bool:
        """
        Method to withdraw money from a specific account. Should be the only method used to withdraw money.

        :param amount: Amount of money to withdraw.
        :param account: Account to withdraw money from (checking or savings).

        :return: True if successful, False if not.
        """
        if account == 'checking':
            if 0 < amount <= self.get_CheckingBalance():
                self.refreshData()
                self.set_CheckingBalance(self.get_CheckingBalance() - amount)
                return True
        elif account == 'savings':
            if amount <= 0 or self.get_SavingsBalance() - amount < self.__SavingsMinimum:
                return False
            self.refreshData()
            self.set_SavingsBalance(self.get_SavingsBalance() - amount)
            return True
        return False