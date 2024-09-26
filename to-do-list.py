def main():
    tasks = []

    while True:
        print("To-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == '1':
            task = input("Enter the task: ")
            tasks.append(task)
            print(f"Task '{task}' added!\n")

        elif choice == '2':
            if not tasks:
                print("No tasks in your to-do list.\n")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                print()

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid option! Please try again.\n")

if __name__ == "__main__":
    main()