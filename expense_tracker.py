from datetime import datetime



expenses= [
    {"id": 1, 'amount': 50, 'category': 'Food', 'description': 'Lunch', 'date': datetime.now()},
    {"id": 2, 'amount': 100, 'category': 'Transport', 'description': 'Taxi', 'date': datetime.now()},
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
    category = input("Enter the category to filter by: ")
    filtered_expenses = [expense for expense in expenses if expense['category'] == category]
    for expense in filtered_expenses:
        print(f"ID: {expense['id']}, Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}, Date: {expense['date']}")

    

def view_expenses():
    for expense in expenses:
        print(f"ID: {expense['id']}, Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}, Date: {expense['date']}")
view_expenses()