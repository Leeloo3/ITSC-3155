class BankAccount:
    title_of_bank = "Shaw Bank"

    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            print(f"${amount} deposited to {self.customer_name}'s account. "
                  f"Updated balance: ${self.current_balance}.")
        else:
            print("Must deposit a positive amount.")

    def withdraw(self, amount):
        if amount > 0:
            if self.current_balance - amount >= self.minimum_balance:
                self.current_balance -= amount
                print(f"${amount} withdrawn from {self.customer_name}'s account. "
                      f"Updated balance: ${self.current_balance}.")
            else:
                print(f"Cannot verify ${amount} withdrawal from {self.customer_name}'s account.\n"
                      f" Balance cannot go below the minimum threshold (${self.minimum_balance}).")
        else:
            print("Must withdraw a positive amount.")

    def print_customer_information(self):
        print(f"Bank: {BankAccount.title_of_bank}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Current Balance: ${self.current_balance}")


class Savings(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.__interest_rate = interest_rate

    def apply_interest(self):
        interest = self.current_balance * self.__interest_rate
        if interest > 0:
            self.deposit(interest)
            print(f"Interest applied to {self.customer_name}'s account: "
                  f"${interest: .2f}. New balance: ${self.current_balance: .2f}.")


class Checking(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance)
        self._transfer_limit = transfer_limit

    def transfer(self, amount, recipient_account):
        if amount > self._transfer_limit:
            print(f"Cannot transfer ${amount} to {recipient_account.customer_name}'s account. "
                  f"Exceeds transfer limit of ${self._transfer_limit}.")
        else:
            if self.current_balance - amount >= self.minimum_balance:
                self.withdraw(amount)
                recipient_account.deposit(amount)
                print(f"${amount} transferred to {recipient_account.customer_name}'s account. "
                      f"Updated balance: ${self.current_balance: .2f}.")
            else:
                print(f"Cannot transfer ${amount} to {recipient_account.customer_name}'s account.\n"
                      f" Balance cannot go below the minimum threshold (${self.minimum_balance}).")
