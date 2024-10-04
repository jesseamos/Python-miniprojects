import datetime 
import time
# 1. Task List Display: Display all tasks in the list.
# 2. Add Task: Allow users to add new tasks.
# 3. Remove Task: Allow users to remove existing tasks.
# 4. Mark as Completed: Mark tasks as completed.
# 5. Due Date: Assign due dates to tasks.
# 6. Priority: Assign priority levels to tasks (e.g., High, Medium, Low).
# 7. Search: Search for tasks by name or description.
# 8. Save/Load: Save and load tasks from a file.

def todo_list(name="user"):
    def get_current_time():
        curr_time_sec = time.time()
        curr_time = time.gmtime(curr_time_sec).tm_hour
        if 5 <= curr_time < 12:
            return "Morning"
        elif 12 <= curr_time < 18:
            return "Afternoon"
        elif  18 <= curr_time < 22:
            return "Evening"
        else:
            return "Night"
    get_current_hour = get_current_time()    
    print (f"\nGood {get_current_hour},{name} How are you doing?\n\n")

    todo_list = ["Wash plate","Read a book","Code for an hour"]

    def print_todo_list():
        num = 1
        for x in todo_list :
            print("\n TODO LIST💪 🧑‍🏭⚒️")
            if num <= len(todo_list):
                print(f"{num}. {x}")
                num+=1
    print_todo_list()

    user_choice = input(f"{name}, to")
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="provides a personalized game experience." 
    )

    parser.add_argument(
        "-n","--name",metavar="name",
        required=True,help="The name of the person playing the game."
    )
    args = parser.parse_args()
    todo_app = todo_list(args.name)    
    todo_app