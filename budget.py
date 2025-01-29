import csv


class BudgetManager:
    def __init__(self, budget_file="budget.csv"):
        self.budget_file = budget_file
        self.budget_data = self.load_budget()

    def load_budget(self):
        try:
            with open(self.budget_file, mode="r") as file:
                reader = csv.DictReader(file)
                return {row["category"]: float(row["amount"]) for row in reader}
        except FileNotFoundError:
            print("No budget file found. Starting with empty budgets.")
            return {}

    def save_budget(self):
        with open(self.budget_file, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["category", "amount"])
            writer.writeheader()
            for category, amount in self.budget_data.items():
                writer.writerow({"category": category, "amount": amount})

    def set_budget(self, category, amount):
        self.budget_data[category] = float(amount)
        self.save_budget()
        print(f"Budget set for category '{category}' to {amount}.")

    def get_budget(self, category):
        return self.budget_data.get(category, 0)

    def is_over_budget(self, category, total_spent):
        budget = self.get_budget(category)
        return total_spent > budget if budget else False

    def notify_over_budget(self, expense_data):
        over_budget_categories = []
        for category in expense_data.index:
            total_spent = expense_data[category]
            if self.is_over_budget(category, total_spent):
                over_budget_categories.append(category)
        return over_budget_categories
