tasks = []

def addTask():
    while True:
        addTaskList = input("Add Task: ")
        task_number = len(tasks) + 1
        tasks.append(f"{task_number}. {addTaskList}")

        addAnotherTask = input("Would you like to add another task ? Please answer 'Yes' or 'No': ")
        if addAnotherTask.lower() != 'yes':
            print("Exiting task add.")
            return


def delTask():
    while True :
        delTaskList = input("Choose the number of the task you want to delete or No to break")
        if delTaskList.lower() == "no":
            print("Thank you!")
            return "no"
        
        try:
            task = int(delTaskList)
            if 1 <= task <= len(tasks): 
                del tasks[task - 1]  
                print(f"Task {task} deleted.")
            else:
                print("Invalid task number.")
                continue
        except ValueError:
            print("Please enter a valid task number or 'No' to exit.")
            continue
                
            
        delAnotherTask = input("Would you like to delete another task ? Please answer 'Yes' or 'No': ")
        if delAnotherTask.lower() != 'yes':
            print("Exiting task delete.")
            return "deleted"    
    
def viewTask():
    while True:
        while True:
            viewList = input("If you wanna see all your tasks write tasks else write the number of the task or 'q' to quit: ")
            if viewList.lower() == "tasks":
                print(tasks)
                return
            elif viewList.lower() == "q":
                return
            else:
                try:
                    task = int(viewList)  
                    if 1 <= task <= len(tasks):  
                        print(tasks[task - 1])
                        break
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number or 'tasks' to see all.")
    
        seeAnotherTask = input("Would you like to see another task ? Please answer 'Yes' or 'No': ")
        if seeAnotherTask.lower() != 'yes':
            print("Exiting task view.")
            return "deleted"
            

def completeTask():
    return

print("Welcome to the ToDo App ...!")
print("Create your todo => ")

i = 0
for i in range(len(tasks) + 1):
    addTask()
    viewTask()


print("would you like to delete the task? ")

print(tasks)
for i in range(len(tasks) + 1):
    if delTask().lower() == "no":
        break
    
print(tasks)


