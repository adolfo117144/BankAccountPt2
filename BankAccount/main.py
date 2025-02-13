from savings import Savings
from checking import Checking

savings1 = Savings("Alex", 5000, 10, "12345", "55555555", 2.0)
savings2 = Savings("Bob", 10000, 15, "67890", "12345678", 1.5)

savings1.interest_earned()
savings2.interest_earned()

print(savings1.print_customer_informaton())
print(savings2.print_customer_informaton())

checking1 = Checking("John", 3000, 100, "111222", "55555555", 1500)
checking2 = Checking("Jane", 6000, 200, "555666", "12345678", 2000)

checking1.deposit(500)
checking1.withdraw(1000)
checking1.transfer(1200, checking2)

print(checking1.print_customer_informaton())
print(checking2.print_customer_informaton())