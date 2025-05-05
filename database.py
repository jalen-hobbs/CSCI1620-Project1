import csv

def databaseRead(first_name : str, last_name : str, pin : str) -> "Account Balances | str (error)":
    """
    Function that will read the database.csv file and return account details OR error message.

    :param first_name: First name of account holder. Passed from the account object.
    :param last_name: Last name of account holder. Passed from the account object.
    :param pin: PIN of account holder. Passed from the account object.

    :return: If valid name and PIN, account details; "InvalidPIN" if the account exists but no pin;
             or None if no account exists.
    """

    database = list(csv.reader(open("database.csv", "r")))
    for row in range(len(database) - 1, 0 , -1):
        if database[row][0] == first_name and database[row][1] == last_name:
            if pin == database[row][2]:
                return 'Found', float(database[row][3]), float(database[row][4]), float(database[row][5])
            else:
                return "InvalidPIN"
    return None

def databaseWrite(first_name : str, last_name : str, pin : str, checking : float,
                  savings : float, dep_count : int) -> None:
    """
    Function that will rewrite database.csv with updated information from parameters given.

    :param first_name: First name of account holder. Passed from the account object.
    :param last_name: Last name of account holder. Passed from the account object.
    :param pin: PIN of account holder. Passed from the account object.
    :param checking: Checking balance to update to.
    :param savings: Savings balance to update to.
    :param dep_count: Savings deposit count to update to (for interest payout).

    :return: None.
    """

    old_base = list(csv.reader(open("database.csv", 'r')))
    account_row = 0
    with open('.venv/database.csv', 'w') as new_base:
        writer = csv.writer(new_base)
        for row in range(len(old_base) - 1, 0, -1):
            if old_base[row][0] == first_name and old_base[row][1] == last_name and old_base[row][2] == pin:
                account_row = row

        writer.writerow(['FirstName','LastName','PIN','Checking','Savings','SavingsDepositCount'])
        for row in range(1, len(old_base)):
            if row != account_row:
                writer.writerow(old_base[row])
            else:
                writer.writerow([first_name, last_name, pin, checking, savings, dep_count])