import { useState } from "react";
import "./App.css";
import TaskInput from "./components/TaskInput/TaskInput";
import TaskList from "./components/TaskList/TaskList";
import QuoteOfTheDay from "./components/QuoteOfTheDay/QuoteOfTheDay";

function App() {
  const [tasks, setTasks] = useState([]);

  const addTask = (task) => {
    setTasks([...tasks, task]);
  };

  const removeTask = (index) => {
    setTasks(tasks.filter((__, i) => i !== index));
  };

  return (
    <>
      <h1>To-Do List</h1>

      <TaskInput onAddTask={addTask} />
      <TaskList tasks={tasks} onRemoveTask={removeTask} />
      <QuoteOfTheDay />
    </>
  );
}
export default App;
