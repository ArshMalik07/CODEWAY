task_list = []#Initially list is empty
def add_task():# Function to add task
   
    task = input("Enter a task:\n")
    task_list.append(task)#add the task to the list.
    print("task added successfully!!")
    print("List: ",task_list)#print new list. 


def delete_task():#Function to delete task
    print(task_list)
    print("Which task you want to delete??(enter number)")
    num = int(input("Enter task number"))
    if 1 <= num <= len(task_list):
        task_list.pop(num - 1)# delete particular task from the list.
        print("New list:",task_list)#print new list.
    else:
        print("Invalid task number, please try again.")#if task not present in list.


#Calling the functions with conditions.
while True:
    operation = input("Enter operation!! (add/remove/quit)")
    if operation.lower() == "add":
        add_task()
    elif operation.lower() == "remove":
        delete_task()
    elif operation.lower() == "quit":
        print("Quitting the program.")
        break
    else:
        print("Please enter a valid operation (add/remove/quit).")
