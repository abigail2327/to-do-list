
DATA_FILE = "todo_list.txt"

def load_tasks():
    try:
        with open(DATA_FILE, "r") as file:
            tasks = file.readlines()

        return [task.strip() for task in tasks]

    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def show_tasks(tasks):
    if len(tasks) == 0:
        print("Your to-do list is empty.")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(i + 1, tasks[i]) 
            # this numbers the list 


def main():
    tasks = load_tasks()

    while True:
        print("\n1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            task = input("Enter a task: ")

            if task != "":
                tasks.append(task)
                save_tasks(tasks)
                print("Task added!")
            else:
                print("Task cannot be empty.")

        elif choice == "3":
            show_tasks(tasks)

            if len(tasks) > 0:
                try:
                    number = int(input("Enter task number to delete: "))

                    if number >= 1 and number <= len(tasks):
                        removed = tasks.pop(number - 1)
                        save_tasks(tasks)
                        print("Removed:", removed)
                    else:
                        print("Invalid task number.")

                except ValueError:
                    print("Please enter a number.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()

