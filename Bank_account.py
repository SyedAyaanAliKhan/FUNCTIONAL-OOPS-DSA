class BankAccount:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self._balance = 0




    def deposit(self, amount):
        if amount <=0:
            raise ValueError("Deposit amount cannot be zero")
        else:
            self._balance += amount
        return amount
    

    def withdraw(self, amount):
        if amount <=0:
            raise ValueError("Withdrawn amount cannot be equal to 0")
        if amount>self._balance:
            raise ValueError("Insufficient funds")
        else:
            self._balance -= amount
        return f"Remaining amount: {self._balance}"

    
    
    def show_balance(self):
        return self._balance
    

account = BankAccount("Ayaan")

while True:
    print("Welcome to xyz Bank")
    print("1.Deposit" \
    "      2.Withdraw" \
    "      3.Show Balance" \
    "      4.Exit")

    try:
        user_input = int(input("Choose an option: "))
        if user_input == 1:
            dep_amnt = int(input("Enter the amount you want to deposit: "))
            print(account.deposit(dep_amnt))
        elif user_input == 2:
            wtdrw_amnt = int(input("Enter the amount you want to withdraw: "))
            print(account.withdraw(wtdrw_amnt))
        elif user_input == 3:
            print(account.show_balance())
        elif user_input == 4:
            break
        else:
            print("Please choose the right option")
    except ValueError as e:
        print(f"Error: {e}")