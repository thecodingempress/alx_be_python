task = input("Enter your task: ")
priority = input("Priority (high, medium, low): ")
time_sensitive = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_sensitive.lower() == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is a low priority task. Consider completing it when you have free time.")
    case "medium":
        if time_sensitive.lower() == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be completed soon.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Consider completing it when you have time.")
    case "low":
        if time_sensitive.lower() == "yes":
            print(f"Reminder: '{task}' is a low priority task that should be completed soon.")
        else:
            print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have time.")