import { useState } from "react";

function GetExpenseById() {
  const [id, setId] = useState("");
  const [expense, setExpense] = useState(null);
  const [error, setError] = useState("");

  async function handleSubmit(event) {
    event.preventDefault();
    setError("");
    setExpense(null);

    const response = await fetch(`http://localhost:8000/expenses/${id}`);

    if (!response.ok) {
      const errorData = await response.json();
      setError(errorData.detail || "Failed to fetch expense");
      return;
    }

    const data = await response.json();
    setExpense(data);
  }

  return (
    <div className="tool tool-column">
      <form className="tool" onSubmit={handleSubmit}>
        <span className="tool-label">Find by ID</span>
        <input
          className="input input-narrow"
          placeholder="ID"
          value={id}
          onChange={(e) => setId(e.target.value)}
        />
        <button type="submit" className="btn">
          Get Expense
        </button>
      </form>
      {error && <p className="error-text">{error}</p>}
      {expense && (
        <div className="found-expense">
          <span className="badge">{expense.category}</span>
          <span>{expense.description}</span>
          <span>{expense.amount}</span>
          <span>{expense.date}</span>
        </div>
      )}
    </div>
  );
}

export default GetExpenseById;
