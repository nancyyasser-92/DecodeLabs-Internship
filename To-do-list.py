# 1 add tasks to a list
message = """1-Add tasks to a list
2-Mark tasks as complete
3-View tasks
4-Quit"""
def add_task():
    # get task from user
    task=input("Enter your task:")  
    # define task status 
    task_info={"task":task,"completed":False}
    # add task to the list of tasks
    tasks.append(task_info)
    print("Task added to the list successfuly")
def mark_task_complete():     
    # get list of incomplete tasks
    incomlete_tasks=[task for task in tasks if task['completed']==False]
    if not incomlete_tasks:
        print("No tasks to mark as complete")
        return
    # show them to the user 
    for i ,task in enumerate(incomlete_tasks):
        print(f'{i+1}-{task["task"]}')
        print("-"*30)
    # get the task from the user 
    task_number=int(input("Choose the task to complete:") )
    # mark the task as completed
    tasks[task_number-1]["completed"]=True
    # print the message to the user
    print("Task marked completed")
def view_tasks():
    if not tasks:
        print("No tasks to view")
        return
    for i,task in enumerate(tasks):
        if task["completed"]:
            status ="Done"
        else:
            status="Pending" 
        print(f'{i+1}.{task["task"]}-{status}')       

tasks=[]
while True:
    print(message)
    choice=input('Enter your Choice')
    if choice=="1":
        add_task()
    elif choice=="2":
        mark_task_complete()
    elif choice=="3":
        view_tasks()
    elif choice=="4":
        break
    else:
        print("Invalid choice, please enter a number between 1 and 4")






