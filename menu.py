from GroupProject import listTask
from GroupProject import addTask
from GroupProject import deleteTask

f=open("user.txt","w")
f.write("Hello! This is your current Task List: \n")
f.write()
f.close()


menuExit = 0
while menuExit == 0:
    user = int(input("Congratulations! You're running [YOUR NAME]'s Task List program.\nWhat would you like to do next?\n1.List all tasks.\n"
                     "2.Add a task to the list.\n3.Delete a task.\n0.To quit the program\n"))
    if user == 0:
        menuExit +=1
    elif user == 1:
        listTask()
        send = input("Press enter to continue.")
    elif user == 2:
        addTask()
    elif user == 3:
        deleteTask()
    else:
        print("INVALID ANSWER")

