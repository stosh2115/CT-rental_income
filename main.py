class Property:
    def __init__(self, name):
        self.name = name
        self.expenses = []
        self.incomes = []

    def add_expense(self, amount, expense_type):
        expense = {"amount": amount, "type": expense_type}
        self.expenses.append(expense)
        print(f"{self.name}, you have added an expense of {amount} for {expense_type}!")

    def add_income(self, amount, income_type):
        income = {"amount": amount, "type": income_type}
        self.incomes.append(income)
        print(f"{self.name}, you have added an income of {amount} for {income_type}!")

    def view_expense(self):
        for expense in self.expenses:
            print(f"{expense['type']} has {expense['amount']} ")

    def view_income(self):
        for income in self.incomes:
            print(f"{income['type']} has {income['amount']} ")


class User:
    def __init__(self, username):
        self.username = username
        self.properties = []

    def add_property(self, property_name):
        new_property = Property(property_name)
        self.properties.append(new_property)
        print(f"{self.username}, you have added a new property named {property_name}.")

    def view_properties(self):
        print(f"These are the properties that you have entered:")
        for new_property in self.properties:
            print(f"Property: {new_property.name}")

    def main_menu(self):
        username = input("What is your Username? ")
        user = User(username)
        while True:
            print("\nWelcome to Bigger Pockets. This is where you'll find financial freedom!")
            print("Please choose the following:")
            print("A. Add Property")
            print("B. Add Expense")
            print("C. Add Income")
            print("D. View Properties")
            print("E. View Expenses")
            print("F. View Incomes")
            print("G. Exit")
            choice = input("Please choose the following A-G: ").upper()

            if choice == 'A':
                property_name = input("Enter property name: ")
                user.add_property(property_name)
            elif choice == 'B':
                property_index = int(input("Enter the property index: "))
                amount = float(input("Enter the expense amount: "))
                expense_type = input("Enter the expense type: ")
                user.properties[property_index].add_expense(amount, expense_type)
            elif choice == 'C':
                property_index = int(input("Enter the property index: "))
                amount = float(input("Enter the income amount: "))
                income_type = input("Enter the income type: ")
                user.properties[property_index].add_income(amount, income_type)
            elif choice == 'D':
                user.view_properties()
            elif choice == 'E':
                property_index = int(input("Enter the property index: "))
                user.properties[property_index].view_expense()
            elif choice == 'F':
                property_index = int(input("Enter the property index: "))
                user.properties[property_index].view_income()
            elif choice == 'G':
                print("You have signed out of Bigger pockets :(")
                break
            else:
                print("Invalid choice. Please enter a letter between A and G.")


user = User("")
user.main_menu()