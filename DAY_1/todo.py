
def display_list(todo_list):
    print("To-Do List:")
    if not todo_list:
        print("Your to-do list is empty!")
    else:
        for index, task in enumerate(todo_list):
            print(f"{index + 1}. {task}")


def add_task(todo_list, task):
    todo_list.append(task)
    print(f"'{task}' added to your to-do list!")


def remove_task(todo_list, task_index):
    if task_index >= len(todo_list) or task_index < 0:
        print("Invalid task index!")
    else:
        removed_task = todo_list.pop(task_index)
        print(f"'{removed_task}' removed from your to-do list!")


def main():
    todo_list = []

    while True:
        print("\n1. Add Task\n2. Display Tasks\n3. Remove Task\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(todo_list, task)
        elif choice == '2':
            display_list(todo_list)
        elif choice == '3':
            task_index = int(input("Enter the index of the task to remove: ")) - 1
            remove_task(todo_list, task_index)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
