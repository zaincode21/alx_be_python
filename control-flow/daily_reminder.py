# daily_reminder.py

# Prompt the user to input task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()  # Ensure lower case for matching
time_bound = input("Is it time-bound? (yes/no): ").lower()  # Ensure lower case for matching

# Use a Match Case statement to react based on priority level
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' is a task with unspecified priority"

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Provide the final customized reminder
print(f"Reminder: {reminder}")
