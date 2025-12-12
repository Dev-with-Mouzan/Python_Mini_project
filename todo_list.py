import os

TODO_FILE = "todo_list.txt"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            print("\nYour Tasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
        elif choice == '2':
            new_task = input("Enter task description: ")
            tasks.append(new_task)
            save_tasks(tasks)
            print("Task added.")
        elif choice == '3':
            try:
                idx = int(input("Enter task number to remove: "))
                if 1 <= idx <= len(tasks):
                    removed = tasks.pop(idx - 1)
                    save_tasks(tasks)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input.")
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
