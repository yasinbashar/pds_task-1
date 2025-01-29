import csv
import pandas as pd
import matplotlib.pyplot as plt
from category_manager import CategoryManager
from expense_analysis import ExpenseAnalysis 
from data_visualization import DataVisualization
from budget import BudgetManager


class ExpenseTracker:
    def __init__(self, data_file="expenses.csv"):
        self.data_file = data_file
        self.headers = ["date", "category", "description", "amount"]
        self.data = self.load_data()

    def load_data(self):
        try:
            return pd.read_csv(self.data_file)
        except FileNotFoundError:
            print("No expense file found. Starting with an empty dataset.")
            return pd.DataFrame(columns=self.headers)

    def save_data(self):
        self.data.to_csv(self.data_file, index=False)

    def add_expense(self, date, category, description, amount):
        new_expense = {"date": date, "category": category, "description": description, "amount": float(amount)}
        self.data = pd.concat([self.data, pd.DataFrame([new_expense])], ignore_index=True)
        self.save_data()
        print("Expense added successfully.")


    def update_expense(self, date, category, new_description=None, new_amount=None):
        mask = (self.data["date"] == date) & (self.data["category"] == category)
        if mask.any():
            if new_description:
                self.data.loc[mask, "description"] = new_description
            if new_amount:
                self.data.loc[mask, "amount"] = float(new_amount)
            self.save_data()
            print("Expense updated successfully.")
        else:
            print("No matching expense found.")

    def delete_expense(self, date=None, category=None):
        if date:
            self.data = self.data[self.data["date"] != date]
        if category:
            self.data = self.data[self.data["category"] != category]
        self.save_data()
        print("Expense(s) deleted successfully.")

    def display_expenses(self):
        print(self.data)

    def analyze_expenses(self):
        if self.data.empty:
            print("No expenses to analyze.")
            return

        summary = self.data.groupby("category")["amount"].sum()
        print("\nExpense Analysis by Category:")
        print(summary)

        # Plotting
        summary.plot(kind="bar", title="Expenses by Category", ylabel="Total Amount", xlabel="Category")
        plt.show()

if __name__ == "__main__":
    tracker = ExpenseTracker()
    category_manager = CategoryManager()
    analyzer = ExpenseAnalysis()
    visualizer = DataVisualization()
    budget_manager = BudgetManager()


    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. Update Expense")
        print("3. Delete Expense")
        print("4. Display Expenses")
        print("5. Analyze Expenses")
        print("6. Total spending by category")
        print("7. Category with highest and lowest spending")
        print("8. Total expenses")
        print("9. Spending per category(Bar Chart)")
        print("10. Daily Expenses(Line Chart)")
        print("11. Spending by category(Pie Chart)")
        print("12. Set Monthly Budget")
        print("13. Check Budget Alerts")
        print("14. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category_manager.list_categories()
            category = input("Enter category: ")
            if not category_manager.is_valid_category(category):
                print("Invalid category! Please choose from the available categories.")
                continue
            description = input("Enter description: ")
            amount = input("Enter amount: ")
            tracker.add_expense(date, category, description, amount)

        elif choice == "2":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            new_description = input("Enter new description (leave blank to skip): ") or None
            new_amount = input("Enter new amount (leave blank to skip): ")
            new_amount = float(new_amount) if new_amount else None
            tracker.update_expense(date, category, new_description, new_amount)

        elif choice == "3":
            date = input("Enter date to delete expenses (leave blank to skip): ") or None
            category = input("Enter category to delete expenses (leave blank to skip): ") or None
            tracker.delete_expense(date, category)

        elif choice == "4":
            tracker.display_expenses()

        elif choice == "5":
            tracker.analyze_expenses()
        elif choice == "6":  # Example menu option for analysis
            analyzer.total_spending_by_category()
        elif choice == "7":
            analyzer.category_with_highest_and_lowest_spending()
        elif choice == "8":
            frequency = input("Enter frequency (daily, weekly, monthly): ")
            analyzer.compute_total_expenses(frequency)
        elif choice == "9":  # Example for bar chart
            visualizer.bar_chart_spending_per_category()
        elif choice == "10":  # Example for line chart
            try:
                month = int(input("Enter month as a number (1-12) or press Enter to skip: ") or 0)
                visualizer.line_chart_daily_expenses(month if month else None)
            except ValueError:
                print("Invalid input for month.")
        elif choice == "11":  # Example for pie chart
            visualizer.pie_chart_spending_by_category()
        elif choice == "12":
            category_manager.list_categories()
            category = input("Enter category to set budget for: ")
            if not category_manager.is_valid_category(category):
                print("Invalid category! Please choose from the available categories.")
                continue
            try:
                budget = float(input(f"Enter budget amount for '{category}': "))
                budget_manager.set_budget(category, budget)
            except ValueError:
                print("Invalid budget amount. Please enter a numeric value.")
        elif choice == "13":
            if tracker.data.empty:
               print("No expenses to check against budget.")
               continue
            expense_summary = tracker.data.groupby("category")["amount"].sum()
            over_budget_categories = budget_manager.notify_over_budget(expense_summary)
            if over_budget_categories:
                print("⚠️ Over-Budget Alerts:")
                for category in over_budget_categories:
                    total_spent = expense_summary[category]
                    budget = budget_manager.get_budget(category)
                    print(f"Category '{category}' exceeded the budget of {budget}. Total spent: {total_spent}.")
            else:
                print("✅ All spending is within the budget.")
                
        elif choice == "14":
            print("Exiting Expense Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

