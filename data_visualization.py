import pandas as pd
import matplotlib.pyplot as plt

class DataVisualization:
    def __init__(self, data_file="expenses.csv"):
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        try:
            data = pd.read_csv(self.data_file)
            data["date"] = pd.to_datetime(data["date"])
            return data
        except FileNotFoundError:
            print("No expense file found. Visualization cannot proceed.")
            return pd.DataFrame(columns=["date", "category", "description", "amount"])

    def bar_chart_spending_per_category(self):
        if self.data.empty:
            print("No expenses to visualize.")
            return

        category_totals = self.data.groupby("category")["amount"].sum()
        category_totals.plot(kind="bar", title="Spending per Category", color="skyblue")
        plt.ylabel("Total Spending")
        plt.xlabel("Category")
        plt.tight_layout()
        plt.show()

    def line_chart_daily_expenses(self, month=None):
        if self.data.empty:
            print("No expenses to visualize.")
            return

        if month:
            self.data = self.data[self.data["date"].dt.month == month]

        daily_totals = self.data.groupby(self.data["date"].dt.date)["amount"].sum()
        daily_totals.plot(kind="line", title="Daily Expenses", marker="o", color="green")
        plt.ylabel("Spending")
        plt.xlabel("Date")
        plt.tight_layout()
        plt.show()

    def pie_chart_spending_by_category(self):
        if self.data.empty:
            print("No expenses to visualize.")
            return

        category_totals = self.data.groupby("category")["amount"].sum()
        category_totals.plot(kind="pie", title="Spending Distribution by Category", autopct="%1.1f%%", startangle=140)
        plt.ylabel("")  # Removes the default ylabel
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    visualizer = DataVisualization()

    while True:
        print("\nData Visualization")
        print("1. Bar Chart: Spending per Category")
        print("2. Line Chart: Daily Expenses over a Month")
        print("3. Pie Chart: Percentage Distribution of Spending by Category")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            visualizer.bar_chart_spending_per_category()

        elif choice == "2":
            try:
                month = int(input("Enter month as a number (1-12) or press Enter to skip: ") or 0)
                visualizer.line_chart_daily_expenses(month if month else None)
            except ValueError:
                print("Invalid input for month.")

        elif choice == "3":
            visualizer.pie_chart_spending_by_category()

        elif choice == "4":
            print("Exiting Data Visualization.")
            break

        else:
            print("Invalid choice. Please try again.")
