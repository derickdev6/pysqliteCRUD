import sqlite3
import tkinter as tk
from tkinter import *


def queryHandler(request):
    sqliteConnection = sqlite3.connect('hwood.db')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")
    cursor.execute(request)
    records = cursor.fetchall()
    cursor.close()
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")
        return records


def insertHandler(request):
    sqliteConnection = sqlite3.connect('hwood.db')
    cursor = sqliteConnection.cursor()
    print("DB Connected --------------------------------")
    cursor.execute(request)
    sqliteConnection.commit()
    print("Record inserted/deleted successfully ", cursor.rowcount)
    cursor.close()
    if sqliteConnection:
        sqliteConnection.close()
        print("DB Disconnected -----------------------------")


def main():
    for widget in root.winfo_children():
        widget.destroy()

    lbl_title = tk.Label(text="Main Menu", height=4, width=30)
    lbl_title.grid(column=2, row=1)

    btn_create = tk.Button(text="Create", height=2,
                           width=14, command=lambda: CGUI())
    btn_create.grid(column=2, row=2, pady=5, padx=40)
    btn_read = tk.Button(text="Read", height=2, width=14,
                         command=lambda: RGUI())
    btn_read.grid(column=2, row=3, pady=5, padx=40)
    btn_update = tk.Button(text="Update", height=2,
                           width=14, command=lambda: UGUI())
    btn_update.grid(column=2, row=4, pady=5, padx=40)
    btn_delete = tk.Button(text="Delete", height=2,
                           width=14, command=lambda: DGUI())
    btn_delete.grid(column=2, row=5, pady=5, padx=40)


def CGUI():
    for widget in root.winfo_children():
        widget.destroy()

    btn_back = tk.Button(text="<", height=1, width=1, command=lambda: main())
    btn_back.grid(column=0, row=0)
    lbl_title = tk.Label(text="Create new Movie", height=4, width=30)
    lbl_title.grid(column=0, row=1, columnspan=2)

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
        f"""INSERT INTO Movies (Id, Title, \"Character\", Premiere, Director)
        VALUES ({ent_id.get()}, '{ent_title.get()}', '{ent_character.get()}',
        '{ent_premiere.get()}', '{ent_director.get()}')"""),
        ent_id.delete(0, 100), ent_title.delete(0, 100),
        ent_character.delete(0, 100), ent_premiere.delete(0, 100),
        ent_director.delete(0, 100)])
    btn_create.grid(column=0, row=7, columnspan=2)


def RGUI():
    for widget in root.winfo_children():
        widget.destroy()

    btn_back = tk.Button(text="<", height=1, width=1, command=lambda: main())
    btn_back.grid(column=0, row=0)
    lbl_title = tk.Label(text="Reading options", height=4, width=30)
    lbl_title.grid(column=0, row=1, columnspan=2)

    btn_detailed = tk.Button(text="Detailed View",
                             height=2, width=14, command=lambda: detailedView())
    btn_detailed.grid(column=0, row=2, pady=5, padx=40, columnspan=2)

    btn_year = tk.Button(text="Movies by Year", height=2,
                         width=14, command=lambda: yearView())
    btn_year.grid(column=0, row=3, pady=5, padx=40, columnspan=2)

    btn_director = tk.Button(text="Movies by Director",
                             height=2, width=14, command=lambda: directorView())
    btn_director.grid(column=0, row=4, pady=5, padx=40, columnspan=2)

    def detailedView():
        # Creating the root window
        root = Tk(className="Result")

        # Creating a Listbox and
        # attaching it to root window
        listbox = Listbox(root, width=120, height=50)

        # Adding Listbox to the left
        # side of root window
        listbox.pack(side=LEFT, fill=BOTH)

        # Creating a Scrollbar and
        # attaching it to root window
        scrollbar = Scrollbar(root)

        # Adding Scrollbar to the right
        # side of root window
        scrollbar.pack(side=RIGHT, fill=BOTH)

        # Fetch results from DB
        results = queryHandler("""SELECT *FROM Movies m """)

        # Insert elements into the listbox
        line = "  ", "Id", " " * (4-2), "Title", " " * (42-5), "Character", " " * (
            32-9), "Premiere", " " * (15-8), "Director"
        listbox.insert(END, "".join(line))
        for values in results:
            line = "  ", str(values[0]), " " * (4-len(str(values[0]))), values[1], " " * (42-len(str(values[1]))), values[2], " " * (
                32-len(str(values[2]))), values[3], " " * (15-len(str(values[3]))), values[4]
            listbox.insert(END, "".join(line))

        # Attaching Listbox to Scrollbar
        # Since we need to have a vertical
        # scroll we use yscrollcommand
        listbox.config(yscrollcommand=scrollbar.set, font='TkFixedFont')

        # setting scrollbar command parameter
        # to listbox.yview method its yview because
        # we need to have a vertical view
        scrollbar.config(command=listbox.yview)

        root.mainloop()

    def yearView():
        # Creating the root window
        root = Tk(className="Result")

        # Creating a Listbox and
        # attaching it to root window
        listbox = Listbox(root, width=40, height=20)

        # Adding Listbox to the left
        # side of root window
        listbox.pack(side=LEFT, fill=BOTH)

        # Creating a Scrollbar and
        # attaching it to root window
        scrollbar = Scrollbar(root)

        # Adding Scrollbar to the right
        # side of root window
        scrollbar.pack(side=RIGHT, fill=BOTH)

        # Fetch results from DB
        results = queryHandler("""SELECT COUNT(Id) as cantidad,strftime('%Y', Premiere) as dat
FROM Movies m
GROUP BY dat
ORDER BY cantidad desc""")

        # Insert elements into the listbox
        line = "  ", "Movies", " " * (10-6), "Year",
        listbox.insert(END, "".join(line))

        for values in results:
            line = "  ", str(values[0]), " " * (10-len(str(values[0]))
                                                ), values[1]
            listbox.insert(END, "".join(line))

        # Attaching Listbox to Scrollbar
        # Since we need to have a vertical
        # scroll we use yscrollcommand
        listbox.config(yscrollcommand=scrollbar.set, font='TkFixedFont')

        # setting scrollbar command parameter
        # to listbox.yview method its yview because
        # we need to have a vertical view
        scrollbar.config(command=listbox.yview)

        root.mainloop()

    def directorView():
        # Creating the root window
        root = Tk(className="Result")

        # Creating a Listbox and
        # attaching it to root window
        listbox = Listbox(root, width=40, height=20)

        # Adding Listbox to the left
        # side of root window
        listbox.pack(side=LEFT, fill=BOTH)

        # Creating a Scrollbar and
        # attaching it to root window
        scrollbar = Scrollbar(root)

        # Adding Scrollbar to the right
        # side of root window
        scrollbar.pack(side=RIGHT, fill=BOTH)

        # Fetch results from DB
        results = queryHandler("""SELECT COUNT(Id) as cantidad, Director
FROM Movies m
GROUP BY Director
ORDER BY cantidad desc""")

        # Insert elements into the listbox
        line = "  ", "Movies", " " * (10-6), "Director",
        listbox.insert(END, "".join(line))

        for values in results:
            line = "  ", str(values[0]), " " * (10-len(str(values[0]))
                                                ), values[1]
            listbox.insert(END, "".join(line))

        # Attaching Listbox to Scrollbar
        # Since we need to have a vertical
        # scroll we use yscrollcommand
        listbox.config(yscrollcommand=scrollbar.set, font='TkFixedFont')

        # setting scrollbar command parameter
        # to listbox.yview method its yview because
        # we need to have a vertical view
        scrollbar.config(command=listbox.yview)

        root.mainloop()


def UGUI():
    for widget in root.winfo_children():
        widget.destroy()

    btn_back = tk.Button(text="<", height=1, width=1, command=lambda: main())
    btn_back.grid(column=0, row=0)
    lbl_title = tk.Label(
        text="Update Movie\nFirst, select a movie to update", height=4, width=30)
    lbl_title.grid(column=0, row=1, columnspan=2)

    lbl_id = tk.Label(text="Id", height=2, width=10)
    lbl_id.grid(column=0, row=2, padx=10)
    ent_id = tk.Entry()
    ent_id.grid(column=1, row=2, padx=10, sticky="w")

    btn_create = tk.Button(text="Select by Id",
                           command=lambda: verify("Id", ent_id.get()))
    btn_create.grid(column=0, row=3, columnspan=2)

    lbl_title = tk.Label(text="Title", height=2, width=10)
    lbl_title.grid(column=0, row=4, padx=10)
    ent_title = tk.Entry()
    ent_title.grid(column=1, row=4, padx=10, sticky="w")

    btn_create = tk.Button(text="Select by Title",
                           command=lambda: verify("Title", ent_title.get()))
    btn_create.grid(column=0, row=5, columnspan=2)

    def verify(type, check):
        search = queryHandler(
            f"""Select * FROM Movies WHERE {type} = '{check}'""")
        if (len(search) != 0):
            update(search[0], type, check)
        else:
            UGUI()

    def update(search, type, check):
        for widget in root.winfo_children():
            widget.destroy()

        btn_back = tk.Button(text="<", height=1, width=1,
                             command=lambda: UGUI())
        btn_back.grid(column=0, row=0)
        lbl_title = tk.Label(text="Updating Movie", height=4, width=30)
        lbl_title.grid(column=0, row=1, columnspan=2)

        lbl_id = tk.Label(text="Id", height=2, width=10)
        lbl_id.grid(column=0, row=2, padx=10)
        ent_id = tk.Label(text=search[0], height=2)
        ent_id.grid(column=1, row=2, padx=10, sticky="w")

        lbl_title = tk.Label(text="Title", height=2, width=10)
        lbl_title.grid(column=0, row=3, padx=10)
        ent_title = tk.Entry()
        ent_title.insert(END, search[1])
        ent_title.grid(column=1, row=3, padx=10, sticky="w")

        lbl_character = tk.Label(text="Character", height=2, width=10)
        lbl_character.grid(column=0, row=4)
        ent_character = tk.Entry()
        ent_character.insert(END, search[2])
        ent_character.grid(column=1, row=4, padx=10, sticky="w")

        lbl_premiere = tk.Label(text="Premiere", height=2, width=10)
        lbl_premiere.grid(column=0, row=5)
        ent_premiere = tk.Entry()
        ent_premiere.insert(END, search[3])
        ent_premiere.grid(column=1, row=5, padx=10, sticky="w")

        lbl_director = tk.Label(text="Director", height=2, width=10)
        lbl_director.grid(column=0, row=6)
        ent_director = tk.Entry()
        ent_director.insert(END, search[4])
        ent_director.grid(column=1, row=6, padx=10, sticky="w")

        btn_update = tk.Button(text="Update", command=lambda: [insertHandler(
            f"""UPDATE Movies 
SET Title = '{ent_title.get()}',
"Character" = '{ent_character.get()}',
Premiere = '{ent_premiere.get()}',
Director = '{ent_director.get()}'
WHERE {type} = {check}"""), UGUI()])
        btn_update.grid(column=0, row=7, columnspan=2)


def DGUI():
    for widget in root.winfo_children():
        widget.destroy()

    btn_back = tk.Button(text="<", height=1, width=1, command=lambda: main())
    btn_back.grid(column=0, row=0)
    lbl_title = tk.Label(text="Delete Movie", height=4, width=30)
    lbl_title.grid(column=0, row=1, columnspan=2)

    lbl_id = tk.Label(text="Id", height=2, width=10)
    lbl_id.grid(column=0, row=2, padx=10)
    ent_id = tk.Entry()
    ent_id.grid(column=1, row=2, padx=10, sticky="w")

    btn_create = tk.Button(text="Delete by Id", command=lambda: [insertHandler(
        f"""DELETE FROM Movies WHERE Id = {ent_id.get()}"""), ent_id.delete(0, 100)])
    btn_create.grid(column=0, row=3, columnspan=2)

    lbl_title = tk.Label(text="Title", height=2, width=10)
    lbl_title.grid(column=0, row=4, padx=10)
    ent_title = tk.Entry()
    ent_title.grid(column=1, row=4, padx=10, sticky="w")

    btn_create = tk.Button(text="Delete by Title", command=lambda: [insertHandler(
        f"""DELETE FROM Movies WHERE Title = '{ent_title.get()}'"""), ent_title.delete(0, 100)])
    btn_create.grid(column=0, row=5, columnspan=2)


if __name__ == '__main__':
    root = tk.Tk(className='Sqlite CRUD')
    main()
    root.mainloop()
