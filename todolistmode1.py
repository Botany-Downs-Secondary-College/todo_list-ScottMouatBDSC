#ToDoList.py
#This makes a list to add jobs or view list
#Scott Mouat, Feb 2021

def menu():
    print("1: Add a new task")
    print("2: View List")
    print("3: Exit")
    mode = input("What would you like to do? ")
    
def mode_one():
    more_tasks == "Y"
    while more_tasks == "Y":
        new_task = input("What new task would you like to add? Or would you like to exit? ")
        new_task.capitalize()
        if new_task == "Exit":
            to_do_list.append(new_task)
            more_tasks = input("Would you like to add more tasks?(Y/N) ")
        else:
            menu()

to_do_list = []

