import pandas as pd
import numpy as np

class ExpenseAnalysis:
    def __init__(self, data_file="expenses.csv"):
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        try:
            return pd.read_csv(self.data_file)
        except FileNotFoundError:
            print("No expense file found. Starting with an empty dataset.")
            return pd.DataFrame(columns=["date", "category", "description", "amount"])

    def total_spending_by_category(self):
        if self.data.empty:
            print("No expenses to analyze.")
            return

        total_by_category = self.data.groupby("category")["amount"].sum()
        print("\nTotal Spending by Category:")
        print(total_by_category)

    def category_with_highest_and_lowest_spending(self):
        if self.data.empty:
            print("No expenses to analyze.")
            return

        total_by_category = self.data.groupby("category")["amount"].sum()
        highest = total_by_category.idxmax()
        lowest = total_by_category.idxmin()
        print("\nCategory with Highest Spending:")
        print(f"{highest}: {total_by_category[highest]}")
        print("\nCategory with Lowest Spending:")
        print(f"{lowest}: {total_by_category[lowest]}")

    def compute_total_expenses(self, frequency="daily"):
        if self.data.empty:
            print("No expenses to analyze.")
            return

        self.data["date"] = pd.to_datetime(self.data["date"])
        self.data = self.data.sort_values("date")

        if frequency == "daily":
            total_expenses = self.data.groupby(self.data["date"].dt.date)["amount"].sum()
        elif frequency == "weekly":
            total_expenses = self.data.groupby(self.data["date"].dt.isocalendar().week)["amount"].sum()
        elif frequency == "monthly":
            total_expenses = self.data.groupby(self.data["date"].dt.to_period("M"))["amount"].sum()
        else:
            print("Invalid frequency. Choose from 'daily', 'weekly', or 'monthly'.")
            return

        print(f"\nTotal Expenses ({frequency.capitalize()}):")
        print(total_expenses)

if __name__ == "__main__":
    analyzer = ExpenseAnalysis()

    while True:
        print("\nExpense Analysis")
        print("1. Total Spending by Category")
        print("2. Category with Highest and Lowest Spending")
        print("3. Compute Total Expenses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            analyzer.total_spending_by_category()

        elif choice == "2":
            analyzer.category_with_highest_and_lowest_spending()

        elif choice == "3":
            frequency = input("Enter frequency (daily, weekly, monthly): ")
            analyzer.compute_total_expenses(frequency)

        elif choice == "4":
            print("Exiting Expense Analysis.")
            break

        else:
            print("Invalid choice. Please try again.")
