import datetime
import os, shutil
import time

tasks = ["Check emails", "Team meeting", "Code review"]
tasks.append("Write documentation")
print(tasks)

print("Reminder: Meeting at 3:00 PM today -->", datetime.date.today())

note = input("Ideas for today's projects: ")

with open("daily_note.txt", "a") as file:
    file.write(note + "\n")
print(note, "Note saved.")

os.makedirs("Documents", exist_ok=True)
shutil.move("daily_note.txt", "Documents/daily_note.txt")
print("Moved daily_note.txt to Documents folder.")

print("First script execution completed.")

print("Sleeping for 5 seconds...")
time.sleep(5)
print("Awake again!")

shutil.move("Documents/daily_note.txt", "daily_note.txt")
print("Moved daily_note.txt from Documents folder to the root folder.")

print("Second script execution completed.")

event = {"title": "Team meeting", "date": "2023-10-30", "time": "15:00"}
print(f"{event['title']} at {event['date']} at {event['time']} on {datetime.date.today()}")

with open("daily_note.txt", "a") as file:
    file.write("Completed Python scripts. \n")
print("Log updated.")

meet_time = datetime.datetime.now() + datetime.timedelta(hours=2)
print("Meeting in:", meet_time - datetime.datetime.now())