from datetime import datetime
import nepali_datetime
import tkinter as tk

# Get the Nepali date
nepaliDate = nepali_datetime.date.today().strftime("%Y %B %d")

# Get the day of the week in English
day_of_week = datetime.now().strftime("%A") 

completeDate = nepaliDate + ", " + day_of_week

root = tk.Tk()
root.title("Nepali Date")

label = tk.Label(root, text=completeDate, font=("Segoe UI", 40, 'bold'), padx=20, pady=20)
label.pack(anchor='center')

root.mainloop()