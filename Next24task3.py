import tkinter as tk
from tkinter import messagebox
import requests
def fetch():
    singer = singer_input.get()
    track = track_input.get()
    if singer and track:
        try:
            url = f"https://api.lyrics.ovh/v1/{singer}/{track}"
            response = requests.get(url)
            data = response.json()
            text = data.get("lyrics", "Lyrics not found.")
            output.delete(1.0, tk.END)
            output.insert(tk.END, text)
        except Exception as e:
            messagebox.showerror("Error", f"Could not fetch lyrics: {str(e)}")
    else:
        messagebox.showwarning("Input Error", "Please enter both singer and track name.")

# Create the main window
app = tk.Tk()
app.title("Lyrics Extractor")

# Set background color
app.configure(bg='lightgray')

# Singer label and entry 
tk.Label(app, text="Singer", bg='#f0f0f0', font=('Helvetica', 14)).grid(row=0, column=0, padx=10, pady=10)
singer_input = tk.Entry(app, font=('Helvetica', 12))
singer_input.grid(row=0, column=1, padx=10, pady=10)

# Track label and entry 
tk.Label(app, text="Track", bg='#f0f0f0', font=('Helvetica', 14)).grid(row=1, column=0, padx=10, pady=10)
track_input = tk.Entry(app, font=('Helvetica', 12))
track_input.grid(row=1, column=1, padx=10, pady=10)

# Fetch Lyrics button 
fetch_button = tk.Button(app, text="Fetch Lyrics", command=fetch, bg='#C1FFC1', fg='black', font=('Helvetica', 12, 'bold'))
fetch_button.grid(row=2, column=0, columnspan=2, pady=10)

# Lyrics text box 
output = tk.Text(app, wrap='word', height=15, width=50, bg='#FFB6C1')
output.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the application
app.mainloop()