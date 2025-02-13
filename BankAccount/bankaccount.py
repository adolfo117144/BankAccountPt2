class BankAccount:
    bank_title = "Chase"
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self._account_number = account_number
        self.__routing_number = routing_number
        self.current_balance = current_balance
        self.customer_name = customer_name
        self.minimum_balance = minimum_balance

    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            print("New Current Balance: {}".format(self.current_balance + amount))
        else:
            print("No New Balance")

    def withdraw(self, amount):
        withdrawal = self.current_balance - amount
        if withdrawal < self.minimum_balance:
            print("Withdraw failed!")
        else:
            self.current_balance -= amount
            print("Withdraw successful, New Balance: {}".format(withdrawal))

    def print_customer_informaton(self):
        return '{} has a balance of {} - {}'.format(self.customer_name, self.current_balance, self.bank_title)