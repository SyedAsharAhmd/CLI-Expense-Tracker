
expenses = [
	{ "id" : 1, "amount": 100, "category": "food", "description" : "banana", "date" : "16/09/2026"},
	{ "id"  : 2, "amount": 50, "category": "Animal", "description" : "bat" , "date"  : "15/09/2026"}
]

def add_expense():
	try:
		amount = float(input("Enter amount: "))
	except TypeError:
		print("invalid amount")
		return
	if amount == "":
		print("Enter an Amount to proceed")
		return
	category = input("Enter Category: ")
	if category == "":
		print("Enter a Category to proceed")
		return
	description = input("Enter Description: ")
	if description == "":
		print("Enter a Description to proceed")
		return
	date = input("Enter Date: ")
	if print == "":
		print("Enter Description to proceed")
		return
	id = len(expenses) + 1

	expense = {
		'id' : id ,
		'amount' : amount ,
		'category' : category ,
		'description' : description ,
		'date' : date
	}
	expenses.append(expenses)

def view_expense():
	for expense in expenses:
		print(f"ID: {expense['id']}, Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}, Date: {expense['date']}")

def filter_expense():
	filtered_expense = [expense for expense in expenses if expense["category"]=="category"]
	if filter == "c":
		filter_date()
	elif filter == "d":
		filter_category()



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
			view_expense()
		elif choice == "3":
			filter_expense()
		elif choice == "4":
			print("showing")
		elif choice == "5":
			print("deletion")
		elif choice == "6":
			break
		else:
			print("Choose the number in between 1 and 6")

if __name__ == "__main__":
    main()