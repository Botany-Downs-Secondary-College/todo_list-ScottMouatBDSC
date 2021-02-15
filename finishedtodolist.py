#ToDoList.py
#This makes a list to add jobs or view list
#Scott Mouat, Feb 2021

def menu():
    print("1: Add a new task")
    print("2: View List")
    print("3: Exit")
    while True:
        try:
            mode = int(input("What would you like to do? "))
            if mode > 3 or mode < 0:
                ValueError
            elif mode == 3:
                print("You have exited the program")
                break
            else:
                return mode
        except ValueError:
            print("Please enter a valid number corresponding to a mode")
            
    
def mode_one():
    more_tasks = "Y"
    while more_tasks == "Y":
        new_task = input("What new task would you like to add? Or would you like to exit? ")
        new_task.capitalize()
        if new_task == "Exit":
            x = menu()
            choose_mode(x)            
        else:
            to_do_list.append(new_task)
            more_tasks = input("Would you like to add more tasks?(Y/N) ") 
    x = menu()
    choose_mode(x)

            
def mode_two():
    print("Here is your to do list")
    print(to_do_list)
    x = menu()
    choose_mode(x)

def choose_mode(x):
    if x == 1:
        mode_one()
    elif x == 2:
        mode_two()

to_do_list = []
x = menu()
choose_mode(x)

