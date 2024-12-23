const TaskList = ({ tasks, onRemoveTask }) => {
  return (
    <div>
      <ul>
        {tasks.map((task, index) => (
          <li key={index}>
            <span>{task}</span>
            <button onClick={() => onRemoveTask(index)}>Remove</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TaskList;
