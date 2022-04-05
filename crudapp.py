import sqlite3
import tkinter as tk


def queryHandler(request):
    sqliteConnection = sqlite3.connect('hwood.db')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")
    cursor.execute(request)
    records = cursor.fetchall()
    print(records)
    cursor.close()
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")


def insertHandler(request):
    sqliteConnection = sqlite3.connect('hwood.db')
    cursor = sqliteConnection.cursor()
    print("DB Connected --------------------------------")
    cursor.execute(request)
    sqliteConnection.commit()
    print("Record inserted successfully ", cursor.rowcount)
    cursor.close()
    if sqliteConnection:
        sqliteConnection.close()
        print("DB Disconnected -----------------------------")


def main():
    for widget in root.winfo_children():
        widget.destroy()
    lbl_title = tk.Label(text="Bienvenido", height=4, width=30)
    lbl_title.grid(column=2, row=1)

    btn_create = tk.Button(text="Create", height=2,
                           width=14, command=lambda: CGUI())
    btn_create.grid(column=2, row=2, pady=5, padx=40)
    btn_read = tk.Button(text="Read", height=2, width=14)
    btn_read.grid(column=2, row=3, pady=5, padx=40)
    btn_update = tk.Button(text="Update", height=2, width=14)
    btn_update.grid(column=2, row=4, pady=5, padx=40)
    btn_delete = tk.Button(text="Delete", height=2, width=14)
    btn_delete.grid(column=2, row=5, pady=5, padx=40)


def CGUI():
    for widget in root.winfo_children():
        widget.destroy()
    btn_back = tk.Button(text="<", height=1, width=1,
                         command=lambda: main())
    btn_back.grid(column=0, row=0)
    lbl_title = tk.Label(text="Create new Movie", height=4, width=30)
    lbl_title.grid(column=0, row=1, columnspan=2)

    # queryBox = tk.Text(width=30, height=20)
    # queryBox.grid(column=0, row=2, columnspan=2)

    lbl_id = tk.Label(text="Id", height=2, width=10)
    lbl_id.grid(column=0, row=2, padx=10)
    ent_id = tk.Entry(width=3)
    ent_id.grid(column=1, row=2, padx=10, sticky="w")

    lbl_title = tk.Label(text="Title", height=2, width=10)
    lbl_title.grid(column=0, row=3, padx=10)
    ent_title = tk.Entry()
    ent_title.grid(column=1, row=3, padx=10, sticky="w")

    lbl_character = tk.Label(text="Character", height=2, width=10)
    lbl_character.grid(column=0, row=4)
    ent_character = tk.Entry()
    ent_character.grid(column=1, row=4, padx=10, sticky="w")

    lbl_premiere = tk.Label(text="Premiere", height=2, width=10)
    lbl_premiere.grid(column=0, row=5)
    ent_premiere = tk.Entry()
    ent_premiere.grid(column=1, row=5, padx=10, sticky="w")

    lbl_director = tk.Label(text="Director", height=2, width=10)
    lbl_director.grid(column=0, row=6)
    ent_director = tk.Entry()
    ent_director.grid(column=1, row=6, padx=10, sticky="w")

    btn_create = tk.Button(text="Create", command=lambda: [insertHandler(
        f"INSERT INTO Movies (Id, Title, \"Character\", Premiere, Director) VALUES ({ent_id.get()}, '{ent_title.get()}', '{ent_character.get()}', '{ent_premiere.get()}', '{ent_director.get()}')"), ent_id.delete(0, 100), ent_title.delete(0, 100), ent_character.delete(0, 100), ent_premiere.delete(0, 100), ent_director.delete(0, 100)])
    btn_create.grid(column=0, row=7, columnspan=2)


if __name__ == '__main__':
    root = tk.Tk(className='Sqlite CRUD')
    main()
    root.mainloop()
