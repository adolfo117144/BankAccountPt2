from savings import Savings
from checking import Checking

savings1 = Savings("Alex", 5000, 10, "12345", "55555555", 2.0)
savings2 = Savings("Bob", 10000, 15, "67890", "12345678", 1.5)

savings1.interest_earned()
savings2.interest_earned()

print(savings1.print_customer_informaton())
print(savings2.print_customer_informaton())