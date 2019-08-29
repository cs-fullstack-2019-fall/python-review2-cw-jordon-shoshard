list=["Cut the grass","Clean the fridge","Clean my room", "Wash clothes","Make dinner","Wash dishes"]

def listTask():
    for i in range (0, len(list)):
        print(f"{i+1}.{list[i]}")


def addTask():
    listTask()
    taskInput= input("Enter new task to add:  ")
    list.append(taskInput)


