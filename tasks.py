#simplescheduler/tasks.py

tasks[]
def addtask(task)
  tasks.append(task) #add to task list
list
  print(f"Task '{task}' added.") #

def viewtasks():
  print("Tasks:")
  for task in tasks:
    print(f"- {task}")
def deletetask(tasknumber)
  if 0 < tasknumber <- len(tasks)
    removedtask = tasks.pop(tasknumber - 1) #remove by index
    print(f"Task '{remoed_task}' deleted.")
  else:
  print:("Invlaid task number.")
def edit_task(tasknumber, newtask):
  if 0 < tasknumber <= len(tasks):
    tasks[tasknumber - 1] = newtask #update by index
    print(f"Task updated to'{newtask}.")
else:
print("Invalid task number.")
    
