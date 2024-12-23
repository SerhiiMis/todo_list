import { useState } from "react";

const TaskInput = ({ onAddTask }) => {
  const [task, setTask] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (task.trim()) {
      onAddTask(task.trim());
    }
    setTask("");
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={task}
          onChange={(e) => setTask(e.target.value)}
          placeholder="Enter your task"
        />
        <button type="submit">Add Task</button>
      </form>
    </div>
  );
};

export default TaskInput;
