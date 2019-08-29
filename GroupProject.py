list=["Cut the grass","Clean the fridge","Clean my room", "Wash clothes","Make dinner","Wash dishes"]

def listTask():
    for i in range (0, len(list)):
        print(f"{i+1}.{list[i]}")

def addTask():
    listTask()
    add = 0
    while add == 0:
        taskInput= input("Enter new task to add\nor Press x to go back: ")
        if taskInput == "x" or taskInput == "X":
            add +=1
        else:
            list.append(taskInput)
            add +=1

def deleteTask():
    listTask()
    deleteInput=input("Which task would you like to delete? ")
    list.pop(int(deleteInput)-1)