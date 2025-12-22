"""
PERSONAL BUDGET SUMMARY

1.Start
2.Display a welcome message 
3.Ask user to enter name and work type
4.Ask user to enter income
5.Ask the user to enter their expense
 -Transport
 -Airtime
 -Food
 -Gifts
6.Calculate total expense
7.Calculate the remaining balance
8.Display the savings ratio
9.Display 
-user name with welcome message
-Total income
-Total expense
-Total remaining balance
-savings ration
10.End
"""


print("=== PERSONAL BUDGET PLANNER ===")
#eception customized error
class InvalidInputError(Exception):
    """Custom Exception from invalid input"""

class BudgetCalculator:
    def __init__(self):
        self.name = ""
        self.income = 0.0
        self.expenses = {}


    def get_valid_number(self, prompt):
      try:
       while True:
        value = input(prompt)

        if value.replace(".", "", 1).isdigit():
            return float(value)
        else:
            raise InvalidInputError("Enter a valid input")  ##Another way to use cusomixed exceptions

      except InvalidInputError as e:
       print(e)


    def get_user_details(self):
       self.name = input("Please Enter your name ")
       self.income = self.get_valid_number("Enter your monthly salary: GHS")



    def get_expenses(self):
        expense_categories = ["Transport", "Food", "Gifts", "Entertainment"]
        print("\n --- Enter your Expense ----")

        for category in expense_categories:
            try:
                self.expenses[category] = self.get_valid_number(f"Enter your {category} expense: GHS")
            except Exception:
               print("Error Entering Expense, Please try again")


    def calculate_budget(self):
        expenses = sum(self.expenses.values())
        balance = self.income - expenses

        try:
           savings_ratio = (balance / self.income) * 100 if self.income > 0 else 0
        except ZeroDivisionError:
           savings_ratio = 0  
        return expenses, balance, savings_ratio


    def display_summary(self, expenses, balance, savings_ratio):
        print(f"\n === PERSONAL BUDGET FOR {self.name.upper()} ===")
        print(f"Your total monthly income is {self.income:.2f} GHS")
        print(f"Your total monthly expense is {expenses:.2f} GHS")
        print(f"Your total balance is {balance:.2f} GHS")
        print(f"Your Savings ratio is {savings_ratio:.2f}%")

        if savings_ratio < 10:
            print("You are saving too low! Try reducing your expnses")
        elif savings_ratio < 30:
            print("You're saving fairly! Keep improving")
        else:
          print("Great job! You are saving well")


    def show_expense_breakdown(self):
        choice = input(
            "\n Would you like to see a breakdown of your expense? (yes/no)").strip().lower()
        if choice == "yes":
            total = sum(self.expenses.values())
            print("\n Expense Breakdown: ")
            for category, amount in self.expenses.items():
                percent = (amount / total) * 100
                print(f"{category}: ${amount:.2f}    ({percent:.2f}%)")


def main():
        calculator = BudgetCalculator()
        calculator.get_user_details()
        calculator.get_expenses()
        expenses, balance, savings_ratio = calculator.calculate_budget()
        calculator.display_summary(expenses, balance, savings_ratio)
        calculator.show_expense_breakdown()
        print("Thank you for using the personal budget tool")



if __name__ == "__main__":
   main()

