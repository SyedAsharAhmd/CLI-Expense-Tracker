import json
import datetime

def load_expenses():
    try:
        with open('expenses.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    


def save_expenses():
    data = []
    for expense in expenses:
        data.append({
            'id': expense['id'],
            'amount': expense['amount'],
            'category': expense['category'],
            'description': expense['description'],
            'date': expense['date']
        })
    with open('expenses.json', 'w') as f:
        json.dump(data, f, indent=4)


def add_expense():
    try:
        amount = float(input("Enter the amount: ")) 
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return
    if amount <= 0:
        print("Amount must be greater than zero.")
        return 
    highest_id = max([expense['id'] for expense in expenses], default=0)
    id = highest_id + 1 
    category = input("Enter the category: ")
    if category.strip() == "":
        print("Category cannot be empty.")
        return
    description = input("Enter the description: ")
    if description.strip() == "":
        print("Description cannot be empty.")
        return
    date = input("Enter the date (YYYY-MM-DD): ")
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    expense = { 
        'id': id,
        'amount': amount,
        'category': category,
        'description': description,
         'date': date 
    }
    expenses.append(expense)
    save_expenses()


def delete_expense():
    try:
        id = int(input("Enter the ID of the expense to delete: "))
    except ValueError:
        print("Invalid ID. Please enter a valid number.")
        return
    for expense in expenses:
        if expense['id'] == id:
            expenses.remove(expense)
            print(f"Expense with ID {id} deleted.")
            break
    else:
        print(f"No expense found with ID {id}.")
    save_expenses()




def filter_expenses():
    choice = input("Filter by category or date? (c/d): ")
    if choice == 'c':
        category = input("Enter the category to filter by: ")
        filtered_expenses = [expense for expense in expenses if expense['category'] == category]
        if not filtered_expenses:
                print("No expenses found.")
        for expense in filtered_expenses:
            print(f"ID: {expense['id']}, Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}, Date: {expense['date']}")
    elif choice == 'd':
        date = input("Enter the date to filter by (YYYY-MM-DD): ")
        filtered_expenses = [expense for expense in expenses if expense['date'].split()[0] == date]
        if not filtered_expenses:
                print("No expenses found.")
        for expense in filtered_expenses:
            print(f"ID: {expense['id']}, Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}, Date: {expense['date']}")
    else:
            print("Invalid choice. Please enter 'c' or 'd'.")


def view_expenses():
    for expense in expenses:
        print(f"ID: {expense['id']}, Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}, Date: {expense['date']}")

 

def total_expenses():
    total = 0
    for expense in expenses:
        total += expense['amount']
    print(f"Total expenses: {total}")
    spending_by_category = {}
    for expense in expenses:
        category = expense['category']
        spending_by_category[category] = spending_by_category.get(category, 0) + expense['amount']
    print(f"Spending by category: {spending_by_category}")
    highest_expense = max(expenses, key=lambda x: x['amount'])
    print(f"Highest expense: ID {highest_expense['id']}, Amount: {highest_expense['amount']}, Category: {highest_expense['category']}, Description: {highest_expense['description']}, Date: {highest_expense['date']}")




expenses = load_expenses()
while True:
    print("\nMENU-:")
    print("1.Add Expense")
    print("2.View Expense")
    print("3.Delete Expense")
    print("4.Filter Expense")
    print("5.Total Expense")
    print("6.Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        delete_expense()
    elif choice == "4":
        filter_expenses()
    elif choice == "5":
        total_expenses()
    elif choice == "6":
        print("Program Ended..")        
        break
    else:
        print("Invalid Choice!!")



