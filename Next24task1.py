
import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    age = entry_age.get()
    
    # You can add code here to save the data or process it as needed
    messagebox.showinfo("Registration Form", f"Name: {name}\nEmail: {email}\nAge: {age}")

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create a label and entry for the name
label_name = tk.Label(root, text="Name")
label_name.grid(row=0, column=0, padx=10, pady=10)

entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

# Create a label and entry for the email
label_email = tk.Label(root, text="Email")
label_email.grid(row=1, column=0, padx=10, pady=10)

entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=10)

# Create a label and entry for the age
label_age = tk.Label(root, text="Age")
label_age.grid(row=2, column=0, padx=10, pady=10)

entry_age = tk.Entry(root)
entry_age.grid(row=2, column=1, padx=10, pady=10)

# Create a submit button
button_submit = tk.Button(root, text="Submit", command=submit_form)
button_submit.grid(row=3, columnspan=2, pady=20)

# Start the main loop
root.mainloop()
