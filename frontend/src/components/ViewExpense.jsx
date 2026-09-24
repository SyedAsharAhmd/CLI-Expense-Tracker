function ViewExpense({ fetchExpenses }) {
  return (
    <div className="tool">
      <button className="btn" onClick={fetchExpenses}>
        Get Expenses
      </button>
    </div>
  );
}

export default ViewExpense;
