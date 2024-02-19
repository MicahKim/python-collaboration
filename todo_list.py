#todo_list.py

#Define class todo_list to manage tasks
#Initialize empty list of tasks
#Create methods to add, view, mark complete, and delete tasks
    #for view tasks iterate over each task and print details
    #for mark as complete, check for valid task index and change to complete
#define main function to run the todo list
    #include UI 

class todo_list:
    def __init__(todo):
        todo.tasks = []

    def addtask(todo, task):
        todo.tasks.append({"task": task, "complete": False})

    def viewtasks(todo):
        if not todo.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(todo.tasks, 1):
                status = "Complete" if task["complete"] else "Incomplete"
                print(f"{i}. {task['task']} - {status}")

    def markcomplete(todo, task_index):
        if 1 <= task_index <= len(todo.tasks):
            todo.tasks[task_index - 1]["complete"] = True
        else:
            print("Invalid task index.")

    def deletetask(todo, task_index):
        if 1 <= task_index <= len(todo.tasks):
            del todo.tasks[task_index - 1]
        else:
            print("Invalid task index.")

def main():
    todolist = todo_list()
    while True:
        print("\n1. Add Task\n2. View Task List\n3. Mark Task as Complete\n4. Delete Task\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todolist.addtask(task)
        elif choice == "2":
            todolist.viewtasks()
        elif choice == "3":
            task_index = int(input("Enter task number to mark as complete: "))
            todolist.markcomplete(task_index)
        elif choice == "4":
            task_index = int(input("Enter the task number to delete: "))
            todolist.deletetask(task_index)
        elif choice == "5":
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()

