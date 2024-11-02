# The-ToDoList

A simple yet powerful command-line todo list application built with Python. This application allows users to manage their tasks with features like adding, viewing, completing, and deleting tasks, all while maintaining data persistence between sessions.

## Features

- **Task Management**
  - Add new tasks
  - View all tasks or individual tasks
  - Mark tasks as complete
  - Delete tasks
  - Automatic task numbering

- **User-Friendly Interface**
  - Clear menu system
  - Error handling
  - Input validation
  - Formatted task display

- **Data Persistence**
  - Tasks automatically saved to JSON file
  - Tasks loaded on program start
  - Structured data storage

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Shinichi23/The-ToDoList
```
2. Navigate to the project directory:
```bash
cd The-ToDoList
```
3. Run the program:
```bash
python todo.py
```

## Usage
# The app presents a menu with the following options:

- Add Tasks
- View Tasks
- Complete Tasks
- Delete Tasks
- Exit

**Adding Tasks**

- Select option 1
- Enter task description
- Choose to add more tasks or return to menu

**Viewing Tasks**

- Select option 2
- View all tasks by typing 'tasks'
- View individual task by entering task number
- Tasks display includes:
  - Task number
  - Description
  - Completion status
  - Date added

**Completing Tasks**

- Select option 3
- Enter task number to mark as complete
- Already completed tasks will be indicated

**Deleting Tasks**

- Select option 4
- Enter task number to delete
- Confirm deletion

## Data Storage
- Tasks are stored in a tasks.json.

## Requirements

Python 3.x
No external packages required (uses only built-in libraries)

## Contributing
Feel free to fork this project and submit pull requests with improvements!

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Taha.C**