from datetime import datetime



expenses= [
    {"id": 1, 'amount': 50, 'category': 'Food', 'description': 'Lunch', 'date': "22/6/2024 12:30:00"},
    {"id": 2, 'amount': 100, 'category': 'Transport', 'description': 'Taxi', 'date': "22/6/2024 13:00:00"},
]

def add_expense():
    amount = float(input("Enter the amount: "))
    id = len(expenses) + 1
    category = input("Enter the category: ")
    description = input("Enter the description: ")
    date = input("Enter the date: ")
    
    expense = {
        'id': id,
        'amount': amount,
        'category': category,
        'description': description,
         'date': date 
    }
    expenses.append(expense)


add_expense()


def filter_expenses():
    choice = input("Filter by category or date? (c/d): ")
    if choice == 'c':
        category = input("Enter the category to filter by: ")
        filtered_expenses = [expense for expense in expenses if expense['category'] == category]
        for expense in filtered_expenses:
            print(f"ID: {expense['id']}, Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}, Date: {expense['date']}")
    elif choice == 'd':
        date = input("Enter the date to filter by (YYYY-MM-DD): ")
        filtered_expenses = [expense for expense in expenses if expense['date'].split()[0] == date]
        for expense in filtered_expenses:
            print(f"ID: {expense['id']}, Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}, Date: {expense['date']}")
    if not filtered_expenses:
        print("No expenses found")
filter_expenses()
def view_expenses():
    for expense in expenses:
        print(f"ID: {expense['id']}, Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}, Date: {expense['date']}")
view_expenses()