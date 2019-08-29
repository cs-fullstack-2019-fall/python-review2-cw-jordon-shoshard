list=["Cut the grass","Clean the fridge","Clean my room", "Wash clothes","Make dinner","Wash dishes"]
f = oper(list.py,'r')

def listTask():
    for i in range (0, len(list)):
        print(f"{i+1}.{list[i]}")

def addTask():
    listTask()
    add = 0
    while add == 0:
        taskInput= input("Enter new task to add\nor Enter 'x' to go back: ")
        if taskInput == "x" or taskInput == "X":
            add +=1
        else:
            list.append(taskInput)
            add +=1

def deleteTask():
    listTask()
    delete = 0
    while delete == 0:
        deleteInput=input("Which task would you like to delete?\nor Enter 'x' to go back: ")
        if deleteInput == "x" or deleteInput == "X":
            delete +=1
        elif int(deleteInput) > 0 and int(deleteInput) <= len(list):
            list.pop(int(deleteInput)-1)
            delete +=1
        else:
            print("INVALID ANSWER")
