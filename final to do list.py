
tasks =[]
def add_task():
    task=input("Enter the new task:")
    tasks.append(task)
    print("Task will added successfully........!:")
def view_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for i ,task in enumerate(tasks,start=1):
            print(f"{i}.{task}")
def mark_completed():
    view_tasks()
    task_number=int(input("Enter the number of the completed task:"))
    if 1<=task_number<= len(tasks):
        completed_task=tasks.pop(task_number - 1)
        print(f"'{completed_task}'marked as completed...!")
    else:
        print("Invalid task number....!")
def quit():
    print("GoodBYeeee.......!")
while True:
    print("\n TO-DO List Application")
    print("1.Add Task")
    print("2.View Task")
    print("3.Mark Task as Completed")
    print("4.Quit")
    choice=input("Enter your choice(1/2/3/4):")
    
    if choice=="1":
        add_task()
    elif choice=="2":
        view_tasks()
    elif choice=="3":
        mark_completed()
    elif choice=="4":
        quit()
        break
    else:
        print("Invalid choice.please enter valid choice and try again")

