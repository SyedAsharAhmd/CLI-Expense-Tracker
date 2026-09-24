import { useState } from "react";

function FilterExpense({ onFilter }) {
  const [category, setCategory] = useState("");
  const [date, setDate] = useState("");

  function handleSubmit(event) {
    event.preventDefault();
    onFilter(category, date);
  }

  function handleClear() {
    setCategory("");
    setDate("");
    onFilter("", "");
  }

  return (
    <form className="tool" onSubmit={handleSubmit}>
      <span className="tool-label">Filter</span>
      <input
        className="input"
        placeholder="Category"
        value={category}
        onChange={(e) => setCategory(e.target.value)}
      />
      <input
        className="input"
        placeholder="Date (DD/MM/YYYY)"
        value={date}
        onChange={(e) => setDate(e.target.value)}
      />
      <button type="submit" className="btn">
        Filter
      </button>
      <button type="button" className="btn btn-text" onClick={handleClear}>
        Clear
      </button>
    </form>
  );
}

export default FilterExpense;
