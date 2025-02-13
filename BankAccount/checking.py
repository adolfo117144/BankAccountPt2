from bankaccount import BankAccount


class Checking(BankAccount):

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit

    def transfer(self, amount, recipient):
        if amount > self.transfer_limit:
            print(f"Transfer failed! Amount exceeds limit of ${self.transfer_limit:.2f}")
        elif self.current_balance - amount < self.minimum_balance:
            print("Transfer failed! Not enough balance.")
        else:
            self.current_balance -= amount
            recipient.current_balance += amount
            print(f"Transferred ${amount:.2f} to {recipient.customer_name}. New balance: ${self.current_balance:.2f}")

