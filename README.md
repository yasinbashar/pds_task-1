# pds_task-1# Expense Tracker

This project is an Expense Tracker application that allows users to manage their expenses, analyze spending patterns, and visualize data. The application is built using Python and leverages libraries such as `pandas` and `matplotlib` for data manipulation and visualization.

## Features

- **Add Expense**: Add a new expense entry with date, category, description, and amount.
- **Update Expense**: Update an existing expense entry.
- **Delete Expense**: Delete an expense entry by date or category.
- **Display Expenses**: Display all recorded expenses.
- **Analyze Expenses**: Analyze expenses by category and visualize the data using bar charts, line charts, and pie charts.
- **Budget Management**: Set and manage budgets for different categories and receive alerts when spending exceeds the budget.

## Modules

### 1. `expense_tracker.py`

This is the main module that provides the core functionality of the Expense Tracker application. It includes methods to add, update, delete, display, and analyze expenses.

### 2. `category_manager.py`

Manages predefined categories for expenses. It includes methods to list available categories and validate if a category is valid.

### 3. `expense_analysis.py`

Provides methods to analyze expenses, including total spending by category, category with the highest and lowest spending, and computing total expenses based on different frequencies (daily, weekly, monthly).

### 4. `data_visualization.py`

Handles data visualization using `matplotlib`. It includes methods to generate bar charts, line charts, and pie charts for visualizing spending patterns.

### 5. `budget.py`

Manages budgets for different categories. It includes methods to set, get, and save budgets, as well as notify when spending exceeds the budget.

## Usage

1. **Run the Expense Tracker**:
    ```sh
    python expense_tracker.py
    ```

2. **Add an Expense**:
    ```sh
    python expense_tracker.py --add --date YYYY-MM-DD --category CATEGORY --description "DESCRIPTION" --amount AMOUNT
    ```

3. **Update an Expense**:
    ```sh
    python expense_tracker.py --update --date YYYY-MM-DD --category CATEGORY --description "NEW_DESCRIPTION" --amount NEW_AMOUNT
    ```

4. **Delete an Expense**:
    ```sh
    python expense_tracker.py --delete --date YYYY-MM-DD
    ```

5. **Display All Expenses**:
    ```sh
    python expense_tracker.py --display
    ```

6. **Analyze Expenses**:
    ```sh
    python expense_analysis.py --analyze --frequency daily|weekly|monthly
    ```

7. **Visualize Expenses**:
    ```sh
    python data_visualization.py --visualize --type bar|line|pie
    ```

8. **Manage Budgets**:
    ```sh
    python budget.py --set --category CATEGORY --amount AMOUNT
    python budget.py --get --category CATEGORY
    ```

## Requirements

- Python 3.x
- pandas
- matplotlib

Install the required libraries using:
```sh
pip install pandas matplotlib
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## Contact

For any questions or inquiries, please contact [your-email@example.com].