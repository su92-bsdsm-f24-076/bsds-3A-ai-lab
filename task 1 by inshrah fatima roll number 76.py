def set_tasks():
    tasksname=input("Enter your task name :")
    while True:
        try:
            priority =int(input("Enter task priority :"))  
            break
        except ValueError:
            print("priority should be numeric")
    with open("tasks.txt","a") as f:
        f.write(f"{tasksname},{priority}\n")
def tasks_list():
    taskslist=[]
    with open("tasks.txt","r") as f:
        data=f.readlines()
        for line in data:
            line=line.strip().split(",")
            taskslist.append(line)
    taskslist.sort(key=lambda x: int(x[1]))
    for task in taskslist:
        print(f"Your task is {task[0]} and priority is {task[1]}\n")
def remove_task():
    task_to_remove=input("Enter task name to remove task or mark as complete :").lower()
    taskslist=[]
    with open("tasks.txt","r") as f:
        data=f.readlines()
        for line in data:
            line=line.strip().split(",")
            taskslist.append(line)
    with open("tasks.txt","w") as f:
        for task in taskslist:
            if task_to_remove != task[0]:
                f.write(",".join(task)+"\n")

while True:
    print("___Your task Manager___")
    print("press 1 to add task")
    print("press 2 to see task list")
    print("press 3 to remove task")
    print("press e to exit")
    option = input("Select an option from above (1/2/3/e):").lower()
    if option=="e":
        break
    elif option == "1":
        set_tasks ()
    elif option=="2":
        tasks_list()
    elif option=="3":
        remove_task()
    else:
        print("invalid input")

