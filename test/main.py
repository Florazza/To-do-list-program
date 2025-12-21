print("\nWelcome to my to-do list program :3")
print("===================================")

tasks = []

#--------------------------------------

### adds task to the list "tasks" ###
def addTask():
    print("")


### MENU ###
def menu():
    while True:
    
        print("Options")
        
        print("1 - Add a new task")
        print("2 - Remove a task")
        print("3 - Edit an existing task")
        print("4 - View tasks")
        optionSelection = int(input("Select an option: "))

        if optionSelection == 1:
            addTask()
            break
        elif optionSelection == 2:
            removeTask()
            break
        elif optionSelection == 3:
            editTask()
            break
        elif optionSelection == 4:
            viewTasks()
            break

# calls menu at launch
menu()


