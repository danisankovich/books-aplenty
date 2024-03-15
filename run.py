import tkinter as tk
import sqlite3

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

    c.execute("INSERT INTO searches (search) VALUES (?)", (search,))
    conn.commit()
    conn.close()
    update_listbox()
    entry.delete(0, len(search))
    # entry.insert(0, "")

app = tk.Tk()
app.title("Books Aplenty App")
app.geometry("400x300")

label = tk.Label(app, text="Enter A Title or Author: ")
label.pack()

entry = tk.Entry(app)
entry.pack()

submit_button = tk.Button(app, text="Search", command=on_submit)
submit_button.pack()


def update_listbox():
    conn = sqlite3.connect("searches.sqlite")
    c = conn.cursor()

    c.execute("SELECT * FROM searches")
    rows = c.fetchall()

    listbox.delete(0, tk.END)
    for row in rows:
        listbox.insert(tk.END, row[1])
    
    conn.close()

listbox = tk.Listbox(app)
listbox.pack()

update_listbox()

app.mainloop()
