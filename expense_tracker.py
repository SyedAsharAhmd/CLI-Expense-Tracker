import json
from datetime import datetime

expenses = []
def save_expenses():
	with open("expenses.json" , 'w')as f:
		json.dump(expenses, f)

def load_expenses():
	global expenses
	with open("expenses.json" , 'r')as f:
		expenses = json.load(f)



def add_expense():

	amount = input("Enter amount: ")	
	if not amount:
		print("Enter an Amount to proceed")
		return
	try:
		amount = float(amount)
	except ValueError:
		print("invalid amount")
		return
	category = input("Enter Category: ")
	if not category:
		print("Enter a Category to proceed")
		return
	description = input("Enter Description: ")
	if not description:
		print("Enter a Description to proceed")
		return
	date = input("Enter Date (DD/MM/YYYY): ")
	format_pattern = "%d/%m/%Y"
	try:
		datetime.strptime(date, format_pattern)
	except ValueError:
		print("Invalid Date format")
		return
	if not date:
		print("Enter date to proceed")
		return
	highest_id = max(expense["id"] for expense in expenses) if expenses else 0
	id = highest_id + 1
	expense = {
		'id' : id ,
		'amount' : amount ,
		'category' : category ,
		'description' : description ,
		'date' : date
	}
	expenses.append(expense)
	save_expenses()


def view_expenses():
	for expense in expenses:
		print(f" Id: {expense['id']}, Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}, Date: {expense['date']}")

def filter_expense():
	filtered_expenses = input("Filter by category or date (c or d)")
	if filtered_expenses == "c":
		filtered_cat =input("Enter the category: ")
		filtered_cat =[expense for expense in expenses if expense.get("category") == filtered_cat]
		print(filtered_cat.lower)
	elif filtered_expenses == "d":
		filtered_date =input("Enter the date (DD/MM/YYYY): ")
		filtered_date =[expense for expense in expenses if expense.get("date") == filtered_date]
		print(filtered_date)
	else:
		print("Please choose either c or d")
		return

def total_expenses():
	total = 0
	for expense in expenses:
		total += expense['amount']
	print(f"Total of expenses is {total}")
	highest_expense = 0
	highest_expense = max(expense['amount'] for expense in expenses)
	print(f"Highest expense is {highest_expense} ")
	spending_by_category = {}
	for expense in expenses:
		category = expense['category']
		amount = expense ['amount']
		spending_by_category[category]= spending_by_category.get(category , 0) + amount
	print(f"Spending by category = {spending_by_category}")
	save_expenses()
	





def delete_expenses():
	
	delete_expense = (input("Type the ID of the expense to delete: "))
	try:
		delete_expense = int(delete_expense)
	except ValueError:
		print('Invalid value')
		return


	for expense in expenses:
		if delete_expense == expense['id']:
			expenses.remove(expense)	
			break
	else:
		print(f"No expense found with ID {delete_expense}")
	save_expenses()


load_expenses()




def show_menu():
    print("""
    Expense Tracker

    1. Add Expense
    2. View Expenses
    3. Filter Expenses
    4. Show Summary
    5. Delete Expense
    6. Exit
    """)

def main():
	while True:
		show_menu()
		choice =input("Enter your choice (1-6): ")
		if choice == "1":
			add_expense()
		elif choice == "2":
			view_expenses()
		elif choice == "3":
			filter_expense()
		elif choice == "4":
			total_expenses()
		elif choice == "5":
			delete_expenses()
		elif choice == "6":
			break
		else:
			print("Choose the number in between 1 and 6")

if __name__ == "__main__":
    main()

