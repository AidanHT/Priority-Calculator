from tkinter import *
from datetime import datetime
from tkinter import _setit

##Variables
global task, due_dates, difficulties, priorities, time_per_day
task = []
due_dates = []
difficulties = []
priorities = []
days_until_due = []
time_per_day = 0


##Functions
def addTask():
    global task, due_dates, difficulties, priorities, days_until_due, time_per_day
    current_time = datetime.now()
    user_task = task_var.get()
    user_month_due = month_var.get()
    user_day_due = day_var.get()
    user_year_due = year_var.get()
    user_difficulty = difficulty_var.get()
    user_priority = priority_var.get()
    user_time_per_day = time_per_day_var.get()
    # Subtracting the Current Date from The Due Date to Calculate the Time left until Task is Due
    years_left = user_year_due - current_time.year
    months_left = user_month_due - current_time.month
    days_left = user_day_due - current_time.day

    total_days_left = (years_left * 365) + (months_left * 30) + days_left
    days_until_due.append(total_days_left)
    print(days_until_due)
    task.append(user_task)
    due_dates.append([user_month_due, user_day_due, user_year_due])
    difficulties.append(user_difficulty)
    priorities.append(user_priority)
    time_per_day = user_time_per_day

    print(task)
    print(due_dates)
    print(difficulties)
    print(priorities)

    resetEntry()


def resetEntry():
    task_var.set("")
    month_var.set(1)
    day_var.set(1)
    year_var.set(2023)
    difficulty_var.set(1)
    priority_var.set(1)

    priority_scale.configure(bg="#32A956")
    difficulty_scale.configure(bg="#32A956")


##THE ALGORITHMM!!!SSS
def algorithm():
    global task, due_dates, difficulties, priorities, days_until_due, time_per_day

    sorted_days_until_due = sorted(days_until_due)
    key_list_due_dates = []
    days_until_due_algorithm = []
    for i in range(len(sorted_days_until_due)):
        key_list_due_dates.append(
            [sorted_days_until_due[i], sorted_days_until_due[len(sorted_days_until_due) - (i + 1)]])
    print(key_list_due_dates)

    for i in range(len(key_list_due_dates)):
        if i == (1 + len(key_list_due_dates)) / 2 - 1:
            days_until_due_algorithm.append(sorted_days_until_due[int((1 + len(sorted_days_until_due)) / 2)])
        else:
            finder = sorted_days_until_due.index(days_until_due[i])
            days_until_due_algorithm.append(key_list_due_dates[finder][1])

    print(days_until_due_algorithm)

    time_to_work = []
    time = time_per_day_var.get()
    due_date_time = time * 0.7
    priority_time = time * 0.2
    difficulty_time = time * 0.1
    total_days_until_due = 0
    total_priority_level = 0
    total_difficulty = 0
    for i in range(len(task)):
        total_days_until_due += days_until_due[i]
        total_priority_level += priorities[i]
        total_difficulty += difficulties[i]

    due_date_time_segment = due_date_time / total_days_until_due
    priority_time_segment = priority_time / total_priority_level
    difficulty_time_segment = difficulty_time / total_difficulty
    for i in range(len(task)):
        time_for_due_date = due_date_time_segment * days_until_due_algorithm[i]
        time_for_priority = priority_time_segment * priorities[i]
        time_for_difficulty = difficulty_time_segment * difficulties[i]
        total_time = time_for_due_date + time_for_priority + time_for_difficulty
        time_to_work.append(f'{total_time:.0f}')

    display_frame.grid()

    

    for i in range(len(task)):
        display_task = Label(display_frame, text=task[i])
        display_task.grid(row=i+1, column=1)
        display_time_allotted = Label(display_frame, text=str(time_to_work[i]))
        display_time_allotted.grid(row= i + 1, column=2, sticky=E)
    print(time_to_work)




##Functions for Colour Coordinating Priority and Difficulty Scale, Red = HighPriority/Difficulty, Green = LowPriority/Difficulty
def scale_color_priority(ignore):
    priority_level = priority_var.get()
    
    if priority_level == 1:
        priority_scale.config(bg="#32A956")
    elif priority_level == 2:
        priority_scale.config(bg="#9ACD32")
    elif priority_level == 3:
        priority_scale.config(bg="#f2ab23")
    elif priority_level == 4:
        priority_scale.config(bg="#ea861a")
    else:
        priority_scale.config(bg="#FF0000")


def scale_color_difficulty(ignore):
    difficulty_level = difficulty_var.get()

    if difficulty_level == 1:
        difficulty_scale.config(bg="#32A956")
    elif difficulty_level == 2:
        difficulty_scale.config(bg="#9ACD32")
    elif difficulty_level == 3:
        difficulty_scale.config(bg="#f2ab23")
    elif difficulty_level == 4:
        difficulty_scale.config(bg="#ea861a")
    else:
        difficulty_scale.config(bg="#FF0000")


##Priority Calculator MainFrame Title and Add a Task to Scedhule Label Frame


#MAINFRAME
root = Tk()
root.title("Priority Calculator")
mainframe = Frame(root)
root.config(bg="#ea861a")

main_menu_frame = LabelFrame(mainframe, padx=10, pady=10)

add_task_menu_frame = LabelFrame(main_menu_frame, text='Add a Task to Schedule', padx=10, pady=10,
                                 font=('Anonymous Pro', 15))
add_task_menu_frame.config(bg="#f7e8ac")

title_label = Label(main_menu_frame, text="Priority Calculator", fg="#f2ab23", font=("Anonymous Pro", 30))

# Activity Label
task_label = Label(add_task_menu_frame, text="Activity", font=("Anonymous Pro", 10), bg="#f7e8ac")
task_var = StringVar()
task_entry = Entry(add_task_menu_frame, width=19, textvariable=task_var)

##Label and SpinBox For Date, (Month, Year and Day)
date_label = Label(add_task_menu_frame, text="Date (MM/DD/YYYY)", font=("Anonymous Pro", 10), bg="#f7e8ac")
month_var = IntVar()
month_spin = Spinbox(add_task_menu_frame, textvariable=month_var, from_=1, to=12, width=3)

day_label = Label(add_task_menu_frame, text="Day", font=("Anonymous Pro", 10))
day_var = IntVar()
day_spin = Spinbox(add_task_menu_frame, textvariable=day_var, from_=1, to=31, width=3)

year_var = IntVar()
year_spin = Spinbox(add_task_menu_frame, textvariable=year_var, from_=datetime.today().year + 1,
                    to=datetime.today().year + 2, width=4)

##Label and Entry for time per day
time_per_day_label = Label(add_task_menu_frame, text="Time/Day (minutes)", bg="#f7e8ac", font=("Anonymous Pro", 10))
time_per_day_var = IntVar()
time_per_day_entry = Entry(add_task_menu_frame, width=19, textvariable=time_per_day_var)

# Label and Scale for DifficultySS
difficulty_label = Label(add_task_menu_frame, text="Difficulty", font=("Anonymous Pro", 10), bg="#f7e8ac")
difficulty_var = IntVar()
difficulty_scale = Scale(add_task_menu_frame, variable=difficulty_var, from_=1, to=5, orient=HORIZONTAL, bg="#32A956",
                         troughcolor="#c9be91", showvalue=False, command=scale_color_difficulty)
Label(add_task_menu_frame, text="Priority", font=("Anonymous Pro", 10), )
difficulty_scale.bind("<ButtonRelease-1>", scale_color_difficulty)
# Label and Scale for Priority
priority_label = Label(add_task_menu_frame, text="Priority", font=("Anonymous Pro", 10), bg="#f7e8ac")
priority_var = IntVar()
priority_scale = Scale(add_task_menu_frame, variable=priority_var, from_=1, to=5, orient=HORIZONTAL, bg="#32A956",
                       troughcolor="#c9be91", showvalue=False, command=scale_color_priority)

priority_scale.bind("<ButtonRelease-1>", scale_color_priority)

##Button for Add Task
add_button = Button(add_task_menu_frame, text="Add Task", command=addTask, width=22, bg="#99cba6")

##Button for Reset
reset_button = Button(add_task_menu_frame, text="Reset", command=resetEntry, width=22, bg="#99cba6")

##Button to display
display_button = Button(add_task_menu_frame, text="Display Schedule", command=algorithm, bg="#99cba6", width=48)

display_frame = LabelFrame(main_menu_frame, text='Time Alotted per Task', padx=10, pady=10, font=('Anonymous Pro', 15))
display_frame.config(bg="#f7e8ac")
##GRID
##Placement for all Labels, Spinbox, Scales and Buttons
root.minsize(width=450, height=200)

mainframe.grid(padx=50, pady=50)

## Gridding frames that house menus within them
main_menu_frame.grid(row=1, column=1)
add_task_menu_frame.grid(row=2, column=1)
title_label.grid(row=1, column=1, pady=10)

task_label.grid(row=1, column=1, columnspan=2, sticky=W)
task_entry.grid(row=1, column=2, columnspan=4, sticky=W)

date_label.grid(row=2, column=1, sticky=W)
month_spin.grid(row=2, column=2, sticky=W, padx=5, pady=10)
day_spin.grid(row=2, column=3, sticky=W, padx=5, pady=10)
year_spin.grid(row=2, column=4, sticky=W, pady=10)
time_per_day_entry.grid(row=3, column=2, sticky=W, columnspan=4)
time_per_day_label.grid(row=3, column=1, sticky=W, pady=10)
difficulty_label.grid(row=4, column=1, sticky=W, padx=5)
priority_label.grid(row=5, column=1, sticky=W, padx=5)

difficulty_scale.grid(row=4, column=2, columnspan=2, sticky=N + W)
priority_scale.grid(row=5, column=2, columnspan=2, sticky=N + W, pady=10)
add_button.grid(row=6, column=1, columnspan=2)
reset_button.grid(row=6, column=3, columnspan=2)
display_button.grid(row=7, column=1, columnspan=5)

display_frame.grid(row=3, column=1)

root.mainloop()





