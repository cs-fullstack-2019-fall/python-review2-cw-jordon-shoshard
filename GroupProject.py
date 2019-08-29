list=["Cut the grass","Clean the fridge","Clean my room", "Wash clothes","Make dinner","Wash dishes"]

def listTask():
     for i in range (0, len(list)):
         # print(f"{i+1}.{list[i]}")
         print(list)
         return list

def addTask():
    listTask()
    add = 0
    while add == 0: # !! : while input should be the condition taskInput.toLowerCase == x
        taskInput= input("Enter new task to add\nor Enter 'x' to go back: ")
        if taskInput == "x" or taskInput == "X":
            add +=1
        else:
            list.append(taskInput)
            add +=1
            print(list)

def deleteTask():
    listTask()
    delete = 0
    while delete == 0: # !! : while input should be the condition taskInput.toLowerCase == x
        deleteInput=input("Which task would you like to delete?\nor Enter 'x' to go back: ")
        if deleteInput == "x" or deleteInput == "X":
            delete +=1
        elif int(deleteInput) > 0 and int(deleteInput) <= len(list): # !! : deleteInput should be a string OR the prompt should suggest that it is an integer 
            list.pop(int(deleteInput)-1)
            delete +=1
            print(list)
        else:
            print("INVALID ANSWER")


