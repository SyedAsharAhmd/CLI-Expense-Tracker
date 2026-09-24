import ExpenseForm from "./components/ExpenseForm";
import ViewExpense from "./components/ViewExpense";
import Summary from "./components/Summary";
import FilterExpense from "./components/FilterExpense";
import GetExpenseById from "./components/GetExpenseById";
import { useState } from "react";
import "./App.css";

function App() {
  const [expenses, setExpenses] = useState([]);
  const [filterMessage, setFilterMessage] = useState("");

  async function fetchExpenses() {
    setFilterMessage("");
    const response = await fetch("http://localhost:8000/expenses/view");
    const data = await response.json();
    setExpenses(data);
  }

  async function fetchFilteredExpenses(category, date) {
    setFilterMessage("");
    const params = new URLSearchParams();
    if (category) params.set("category", category);
    if (date) params.set("date", date);

    const response = await fetch(
      `http://localhost:8000/expenses?${params.toString()}`
    );
    const data = await response.json();

    setExpenses(data);
    setFilterMessage(data.length === 0 ? "No expenses match that filter." : "");
  }

  async function deleteExpense(id) {
    const response = await fetch(`http://localhost:8000/expenses/${id}`, {
      method: "DELETE",
    });

    if (!response.ok) {
      return;
    }

    setExpenses((prev) => prev.filter((expense) => expense.id !== id));
  }

  return (
    <div className="page">
      <header className="page-header">
        <h1>Expense Tracker</h1>
      </header>

      <Summary />

      <section className="toolbar">
        <ViewExpense fetchExpenses={fetchExpenses} />
        <FilterExpense onFilter={fetchFilteredExpenses} />
        <GetExpenseById />
      </section>

      <section className="expenses">
        <h2>Expenses</h2>

        {filterMessage && <p className="empty-state">{filterMessage}</p>}

        {expenses.length === 0 && !filterMessage ? (
          <p className="empty-state">
            No expenses to show yet. Click "Get Expenses" above, or add one below.
          </p>
        ) : (
          <div className="table-wrap">
            <table className="expense-table">
              <thead>
                <tr>
                  <th>ID</th>
                  <th className="amount-col">Amount</th>
                  <th>Category</th>
                  <th>Description</th>
                  <th>Date</th>
                  <th></th>
                </tr>
              </thead>
              <tbody>
                {expenses.map((expense) => (
                  <tr key={expense.id}>
                    <td>{expense.id}</td>
                    <td className="amount-col">{expense.amount}</td>
                    <td>
                      <span className="badge">{expense.category}</span>
                    </td>
                    <td>{expense.description}</td>
                    <td>{expense.date}</td>
                    <td>
                      <button
                        className="btn-danger"
                        onClick={() => deleteExpense(expense.id)}
                      >
                        Delete
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </section>

      <ExpenseForm onExpenseAdded={fetchExpenses} />
    </div>
  );
}
export default App;
