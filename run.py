import tkinter as tk
import json
from tkinter import END, Text
from tkinter.ttk import Button
import sqlite3
from req import fetch_by_title

def create_database():
    conn = sqlite3.connect("searches.sqlite")
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS searches (
              id INTEGER PRIMARY KEY,
              search TEXT
    )""")

    conn.commit()
    conn.close()

create_database()

def on_submit():
    search = entry.get()
    conn = sqlite3.connect('searches.sqlite')
    c = conn.cursor()

    result = fetch_by_title(search)
    display = json.dumps(result, indent=4)
    text_box.delete('1.0', END) 
    text_box.insert(END, display) 
    c.execute("INSERT INTO searches (search) VALUES (?)", (search,))
    conn.commit()
    conn.close()
    update_listbox()
    entry.delete(0, len(search))

app = tk.Tk()
app.title("Books Aplenty App")

label = tk.Label(app, text="Enter A Title or Author: ")
label.pack()
entry = tk.Entry(app)
entry.pack()

submit_button = tk.Button(app, text="Search", command=on_submit)
submit_button.pack()

text_box = Text(app, height = 20, width = 60)
text_box.pack()
label_listbox = tk.Label(app, text="Search History: ")
label_listbox.pack()
listbox = tk.Listbox(app)
listbox.pack()
app.geometry("600x600")

def update_listbox():
    conn = sqlite3.connect("searches.sqlite")
    c = conn.cursor()

    c.execute("SELECT * FROM searches")
    rows = c.fetchall()

    listbox.delete(0, tk.END)
    for row in rows:
        listbox.insert(tk.END, row[1])
    
    conn.close()


update_listbox()

app.mainloop()
