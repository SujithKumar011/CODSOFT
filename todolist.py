import os
import pickle
from datetime import datetime

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "timestamp": datetime.now()})

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Invalid index.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task['task']} ({task['timestamp']})")

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.tasks, file)

    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'rb') as file:
                self.tasks = pickle.load(file)

def main():
    todo_list = ToDoList()

    filename = "todolist.pkl"

    if os.path.exists(filename):
        todo_list.load_from_file(filename)

    while True:
        print("\n1. Add Task\n2. Remove Task\n3. Display Tasks\n4. Save and Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            index = int(input("Enter the task index to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            todo_list.save_to_file(filename)
            print("To-Do List saved. Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
