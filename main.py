# Task Manager - Simple CLI Application
# This program allows users to add, view, update,
# complete and delete their daily tasks.

tasks = []


# Add a new task
def add_task():
    title = input("Enter task title: ").strip()

    if not title:
        print("Error: Task title cannot be empty.")
        return

    task = {
        "title": title,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")


# Display all tasks
def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\n--- Your Tasks ---")

    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['title']} - {status}")


# Update an existing task
def update_task():
    if not tasks:
        print("No tasks available to update.")
        return

    view_tasks()

    try:
        task_number = int(input("Enter task number to update: "))

        if task_number < 1 or task_number > len(tasks):
            print("Error: Invalid task number.")
            return

        new_title = input("Enter new task title: ").strip()

        if not new_title:
            print("Error: Task title cannot be empty.")
            return

        tasks[task_number - 1]["title"] = new_title
        print("Task updated successfully!")

    except ValueError:
        print("Error: Please enter a valid number.")


# Mark a task as completed
def complete_task():
    if not tasks:
        print("No tasks available to complete.")
        return

    view_tasks()

    try:
        task_number = int(input("Enter task number to complete: "))

        if task_number < 1 or task_number > len(tasks):
            print("Error: Invalid task number.")
            return

        tasks[task_number - 1]["completed"] = True
        print("Task marked as completed!")

    except ValueError:
        print("Error: Please enter a valid number.")


# Delete a task
def delete_task():
    if not tasks:
        print("No tasks available to delete.")
        return

    view_tasks()

    try:
        task_number = int(input("Enter task number to delete: "))

        if task_number < 1 or task_number > len(tasks):
            print("Error: Invalid task number.")
            return

        deleted_task = tasks.pop(task_number - 1)
        print(f"Task '{deleted_task['title']}' deleted successfully!")

    except ValueError:
        print("Error: Please enter a valid number.")


# Main menu
def main():
    while True:
        print("\n==============================")
        print("       TASK MANAGER")
        print("==============================")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. Exit")
        print("==============================")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            update_task()

        elif choice == "4":
            complete_task()

        elif choice == "5":
            delete_task()

        elif choice == "6":
            print("Thank you for using Task Manager!")
            break

        else:
            print("Error: Please choose a number between 1 and 6.")


# Start the application
if __name__ == "__main__":
    main()
