menuExit = 0
while menuExit == 0:
    user = int(input("Congratulations! You're running [YOUR NAME]'s Task List program.\nWhat would you like to do next?\n1. List all tasks.\n"
                     "2. Add a task to the list.\n3. Delete a task.\n0. To quit the program\n"))
    if user == 0:
        menuExit +=1