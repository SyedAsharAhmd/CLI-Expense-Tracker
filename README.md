# CLI Expense Tracker

A simple command-line Expense Tracker built with Python. The application allows users to add, view, filter, summarize, and delete expenses. Expense data is stored locally in a JSON file so it remains available after restarting the application.

## Features

* Add an expense with:

  * Amount
  * Category
  * Description
  * Date
* View all expenses
* Filter expenses by:

  * Category
  * Date
* View spending summary:

  * Total spending
  * Spending by category
  * Highest expense
* Delete an expense by ID
* Save expenses locally using a JSON file
* Load existing expenses when the application starts
* Basic input validation

## Requirements

* Python 3.x

No external Python packages are required.

## How to Run

1. Make sure Python 3 is installed.
2. Open a terminal in the project directory.
3. Run:

```bash
python expense_tracker.py
```

The application will create/use `expenses.json` to store expense data.

## How the Application Works

When the application starts, it loads existing expenses from `expenses.json`.

The expenses are stored in Python as a list of dictionaries. Each expense contains:

```text
id
amount
category
description
date
```

The user interacts with the application through a CLI menu.

When an expense is added or deleted, the updated list is saved back to `expenses.json`.

The application uses functions to separate different responsibilities:

* `load_expenses()` loads data from the JSON file.
* `save_expenses()` saves the current expenses to the JSON file.
* `add_expense()` collects and validates expense information.
* `view_expenses()` displays all expenses.
* `filter_expenses()` filters expenses by category or date.
* `total_expenses()` calculates spending statistics.
* `delete_expense()` removes an expense by its ID.

The program continues running in a `while` loop until the user selects the Exit option.

## Validation and Edge Cases

The application handles several basic invalid inputs and edge cases, including:

* Non-numeric expense amounts
* Zero or negative amounts
* Empty categories
* Empty descriptions
* Invalid date formats
* Missing `expenses.json` file
* Non-existing expense IDs
* Invalid menu choices
* Invalid filter choices

## What I Researched

During development, I researched:

1. Python JSON file handling using `json.load()` and `json.dump()`.
2. Python exception handling using `try` and `except`.
3. Python date validation using the `datetime` module.
4. List comprehensions for filtering expenses.
5. Python's `max()` function and the `key` argument for finding the highest expense.

## 3 Things I Learned

### 1. Working with JSON

I learned how to load structured data from a JSON file into Python and save modified data back to the file. I also learned why the application needs to load the existing data before modifying and saving it.

### 2. Input Validation

I learned how `try` and `except` can prevent invalid user input from crashing the application. For example, converting an invalid amount to a float raises a `ValueError`, which can be handled gracefully.

### 3. Managing Program State

I learned how a list can be used as the application's current state and how different functions can modify or read that shared data. I also learned how to generate expense IDs based on existing IDs instead of simply using the number of expenses.

## Problems I Faced and How I Solved Them

### Problem 1: Expense data was not persisting correctly

Initially, I was loading the JSON data and then immediately writing it back to the file. I also had to make sure that changes such as adding or deleting an expense were followed by saving the updated list.

I solved this by using a separate `save_expenses()` function and calling it after changes to the expense list.

### Problem 2: Expense IDs could be duplicated

Initially, I generated IDs using the number of expenses plus one:

```python
id = len(expenses) + 1
```

This could create duplicate IDs after an expense was deleted.

I changed the logic to find the highest existing ID and add one to it. This keeps IDs unique even when an earlier expense is deleted.

## What I Would Improve With Another Day

If I had another day, I would improve the application by:

* Improving the CLI output and formatting.
* Allowing users to edit existing expenses.
* Adding more flexible date filtering, such as filtering between two dates.
* Adding sorting by amount or date.
* Improving error handling for corrupted JSON files.
* Separating the application into multiple modules as the project grows.
* Adding automated tests for the main functions and validation logic.

## Project Structure

```text
Expense Tracker/
│
├── expense_tracker.py
├── expenses.json
└── README.md
```

## Git Development

The project was developed incrementally using Git with meaningful commits for major stages of development.
