print("\nWelcome to my to-do list program :3")
print("===================================")

tasks = [] # da list


# comments for future self probably learn to use return !


### -------------------------------------- ###



### function that adds task to the list "tasks" ###
def addTask():
    while True:
        addTaskInput = input("Enter a task to add to the list [Enter 0 to cancel]: ")
        if addTaskInput == "0":
            menu()
        else:
            tasks.append(addTaskInput) # addTaskInput goes into tasks
            print("Task added successfully!")
            menu()
### ------------------------------------ ###



### function to remove task ------------ ###
def removeTask():

    if len(tasks) == 0:
        print("List is empty!")
        menu()
    else:
        print(', '.join(tasks)) 

    removeTask = int(input("\nEnter the index of the task you want to delete [Enter 0 to cancel]: "))

    if removeTask == 0:
        menu()
    elif 0 < removeTask <= len(tasks): # starts from 1 
        tasks.pop(removeTask-1) # turns the index 0 into 1 soo it starts from [1] :)
        print(f"Task {removeTask} deleted successfully!")
        menu()
### ------------------------------------- ###



### function to edit tasks --------------- ###
def editTask():
    if len(tasks) == 0:
        print("List is empty!")
        menu()
    else:
        editTaskInput = int(input("Please enter the task index you want to edit [Enter 0 to cancel]: ")) 

    if editTaskInput == 0:
        menu()
    elif 0 < editTaskInput <= len(tasks): # 1-infinite index
        editChange = input("Enter change here: ")
        tasks[editTaskInput - 1] = editChange # replaces wit da edit
        print("Done!")
        menu()
    else:
        print("Invalid index")
        editTask()
### --------------------------------------- ###



### function to view tasks --------------- ###
def viewTasks():
    if len(tasks) == 0:
        print("List is empty!")
        menu()
    else:
        print(', '.join(tasks)) # prints the list without brackets but leaves the comma
        menu()
### --------------------------------------- ###



### MENU ---------------------------------- ###
def menu():
    while True:
    
        print("Options")
        
        print("1 - Add a new task")
        print("2 - Remove a task")
        print("3 - Edit an existing task")
        print("4 - View tasks")
        optionSelection = str(input("Select an option: "))

        if optionSelection == "1":
            addTask()
            break
        elif optionSelection == "2":
            removeTask()
            break
        elif optionSelection == "3":
            editTask()
            break
        elif optionSelection == "4":
            viewTasks()
            break
        else:
            print("Please enter a valid option")
            menu()
### --------------------------------------- ###


# calls menu at launch
menu()


