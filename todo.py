import datetime


tasks = []

def addTask():

    while True:
        addTaskList = input("Add Task: ")
        tasks.append({
            "number": len(tasks) + 1,
            "description": addTaskList,
            "completed": False,
            "date_added": datetime.datetime.now()
        })

        print("Task added")

        addAnotherTask = input("Would you like to add another task ? Please answer 'Yes' or 'No':\n")
        if addAnotherTask.lower() != 'yes':
            print("Exiting task add.")
            return


def delTask():
    while True :
        delTaskList = input("Put the number of the task that you want to delete.if you want to quit write 'Q':\n")
        if delTaskList.lower() == "q":
            print("Thank you!")
            return "q"
        
        try:
            task = int(delTaskList)
            if 1 <= task <= len(tasks): 
                del tasks[task - 1]  
                print(f"Task {task} deleted.")
            else:
                print("Invalid task number.")
                continue
        except ValueError:
            print("Please enter a valid task number or 'Q' to exit.\n")
            continue    
            
        delAnotherTask = input("Would you like to delete another task ? Please answer 'Yes' or 'No':\n")
        if delAnotherTask.lower() != 'yes':
            print("Exiting task delete.")
            return "deleted"    
    
def viewTask():
    while True:
        while True:
            viewList = input("If you wanna see all your tasks write tasks else write the number of the task or 'q' to quit:\n")
            if viewList.lower() == "tasks":
               for task in tasks:
                print(f"Task #{task['number']}: {task['description']}")
                print(f"Status: {'✓ Done' if task['completed'] else '◯ Pending'}")
                print(f"Added: {task['date_added'].strftime('%Y-%m-%d %H:%M')}")
                print("-" * 40)
                return
            elif viewList.lower() == "q":
                return
            else:
                try:
                    task = int(viewList)  
                    if 1 <= task <= len(tasks):  
                        task = tasks[task - 1]
                        print(f"Task #{task['number']}: {task['description']}")
                        print(f"Status: {'✓ Done' if task['completed'] else '◯ Pending'}")
                        print(f"Added: {task['date_added'].strftime('%Y-%m-%d %H:%M')}")
                        print("-" * 40)
                        break
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number or 'tasks' to see all.\n")
    
        seeAnotherTask = input("Would you like to see another task ? Please answer 'Yes' or 'No':\n")
        if seeAnotherTask.lower() != 'yes':
            print("Exiting task view.")
            return "deleted"
            

def completeTask():

    while True:

        task_to_complete = input("Enter task number to mark as complete (or 'q' to quit): ")

        if task_to_complete.lower() =="q":
            return
        try:
            task_to_complete = int(task_to_complete)
            if 1 <= task_to_complete <= len(tasks):
                tasks[task_to_complete - 1]["completed"] = True
                print(f"Task {task_to_complete} marked as complete!")
            else:
                print("Invalid task number")

        except ValueError:
            print("Please enter a valid number")



print("Welcome to the ToDo App ...!")
print("Create your todo => ")

while True:
    print("\nMenu:")
    print("1. Add Tasks")
    print("2. View Tasks")
    print("3. Complete Tasks")
    print("4. Delete Tasks")
    print("5. Exit")
    
    choice = input("Choose an option (1-5): ")
    
    if choice == "1":
        addTask()
    elif choice == "2":
        viewTask()
    elif choice == "3":
        completeTask()
    elif choice == "4":
        delTask()
    elif choice == "5":
        print("Thank you for using ToDo App!")
        break
    



