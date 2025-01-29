class CategoryManager:
    def __init__(self):
        self.predefined_categories = ["Food", "Transport", "Entertainment", "Utilities", "Others"]

    def list_categories(self):
        print("\nAvailable Categories:")
        for category in self.predefined_categories:
            print(f"- {category}")

    def is_valid_category(self, category):
        return category in self.predefined_categories

if __name__ == "__main__":
    category_manager = CategoryManager()

    while True:
        print("\nCategory Manager")
        print("1. List Categories")
        print("2. Validate Category")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            category_manager.list_categories()

        elif choice == "2":
            category = input("Enter a category to validate: ")
            if category_manager.is_valid_category(category):
                print(f"'{category}' is a valid category.")
            else:
                print(f"'{category}' is not a valid category.")

        elif choice == "3":
            print("Exiting Category Manager.")
            break

        else:
            print("Invalid choice. Please try again.")
