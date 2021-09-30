class Account:
    def __init__(self, owner: str, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        # self.amount += amount
        self._transactions.append(amount)

    @property
    def balance(self):
        return sum(self._transactions) + self.amount

    @staticmethod
    def validate_transaction(account: 'Account', amount_to_add):
        if account.balance + amount_to_add < 0:
            raise ValueError("sorry cannot go in debt!")
        account.add_transaction(amount_to_add)
        return f'New balance: {account.balance}'

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f'Account({self.owner}, {self.amount})'

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __add__(self, other):
        new_acc = Account(self.owner + "&" + other.owner, self.amount + other.amount)
        new_acc._transactions = self._transactions + other._transactions
        return new_acc


# def main():
#     def test_add_transaction():
#         acc = Account('john die ', amount=20)
#         acc.add_transaction(20)
#         acc.add_transaction(10)
#
#         print(acc._transactions, 'Should be [20, 10]')
#
#     def test_balance():
#         acc = Account('john die ', amount=20)
#         acc.add_transaction(20)
#         acc.add_transaction(10)
#         print(acc.balance, 'should be 50')
#
#     def test_safe_transaction():
#         acc = Account('john die ', amount=0)
#         acc.add_transaction(-10)
#         print(acc.balance, 'Shout be -10')
#         try:
#             acc.validate_transaction(acc, -10)
#         except ValueError:
#             print('transaction failed')
#
#     def test_account_to_string():
#         acc = Account('bob', amount=20)
#         print(str(acc), 'should be "Account of bob with starting amount: 20"')
#
#     def test_account_to_repr():
#         acc = Account('bob', amount=20)
#         print(repr(acc), f'Account(bob, 20)')
#
#     def test_len_account():
#         acc = Account('mery', amount=20)
#         acc.add_transaction(20)
#         acc.add_transaction(10)
#         print(len(acc), 'should be 2')
#
#     def test_iteration_account():
#         acc = Account('mery', amount=20)
#         acc.add_transaction(10)
#         acc.add_transaction(15)
#         acc.add_transaction(20)
#         print(list(acc), 'Should be [10, 15, 20]')
#
#     def test_index_account():
#         acc = Account('mery', amount=20)
#         acc.add_transaction(10)
#         acc.add_transaction(15)
#         acc.add_transaction(20)
#         print(acc[1], 'Should be 15')
#
#     test_add_transaction()
#     test_balance()
#     test_safe_transaction()
#     test_account_to_string()
#     test_account_to_repr()
#     test_len_account()
#     test_iteration_account()
#     test_index_account()
#
# if __name__ == "__main__":
#     main()


acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)
