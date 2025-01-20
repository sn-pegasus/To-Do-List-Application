import os
import json

# File to save tasks
FILE_NAME = "tasks.json"

# Load tasks from the file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {"pending": [], "completed": []}

# Save tasks to the file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)

# Add a new task
def add_task(tasks):
    task = input("Enter the task description: ")
    tasks["pending"].append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added!")

# View tasks
def view_tasks(tasks):
    print("\nPending Tasks:")
    for i, task in enumerate(tasks["pending"], 1):
        print(f"{i}. {task}")

    print("\nCompleted Tasks:")
    for i, task in enumerate(tasks["completed"], 1):
        print(f"{i}. {task}")

# Mark task as completed
def complete_task(tasks):
    view_tasks(tasks)
    index = int(input("\nEnter the task number to mark as completed: ")) - 1
    if 0 <= index < len(tasks["pending"]):
        task = tasks["pending"].pop(index)
        tasks["completed"].append(task)
        save_tasks(tasks)
        print(f"Task '{task}' marked as completed!")
    else:
        print("Invalid task number!")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    index = int(input("\nEnter the task number to delete: ")) - 1
    if 0 <= index < len(tasks["pending"]):
        task = tasks["pending"].pop(index)
        save_tasks(tasks)
        print(f"Task '{task}' deleted!")
    elif 0 <= index - len(tasks["pending"]) < len(tasks["completed"]):
        task = tasks["completed"].pop(index - len(tasks["pending"]))
        save_tasks(tasks)
        print(f"Task '{task}' deleted!")
    else:
        print("Invalid task number!")

# Main menu
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
