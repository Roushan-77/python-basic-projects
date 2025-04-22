FILENAME = "tasks.txt"


def show_tasks():
    try:
        with open(FILENAME, "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found.")
            else:
                for i, task in enumerate(tasks):
                    print(f"{i+1}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks found.")

def add_task(task):
    with open(FILENAME, "a") as file:
        file.write(task + "\n")
    print(f"Added: {task}")


def delete_task(index):
    try:
        with open(FILENAME, "r") as file:
            tasks = file.readlines()

        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            with open(FILENAME, "w") as file:
                file.writelines(tasks)
            print(f"Deleted: {removed.strip()}")
        else:
            print("Invalid task number.")
    except FileNotFoundError:
        print("No tasks to delete.")

def main():
    while True:
        print("\nSimple To-Do List")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            task = input("Enter new task: ")
            add_task(task)
        elif choice == "3":
            show_tasks()
            try:
                index = int(input("Enter task number to delete: ")) - 1
                delete_task(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main() 