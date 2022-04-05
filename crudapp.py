import tkinter as tk


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
    btn_back = tk.Button(text="<", height=1, width=1, command=lambda: main())
    btn_back.grid(column=0, row=0)
    lbl_title = tk.Label(text="Create", height=4, width=30)
    lbl_title.grid(column=0, row=1, columnspan=2)
    btn_newMovie = tk.Button(text="Movie", height=2,
                             width=10, command=lambda: main())
    btn_newMovie.grid(column=0, row=2)
    btn_newActor = tk.Button(text="Actor", height=2,
                             width=10, command=lambda: main())
    btn_newActor.grid(column=1, row=2)
    btn_newCast = tk.Button(text="Cast", height=2,
                            width=10, command=lambda: main())
    btn_newCast.grid(column=0, row=3)
    btn_newDirector = tk.Button(text="Director", height=2,
                                width=10, command=lambda: main())
    btn_newDirector.grid(column=1, row=3)


if __name__ == '__main__':
    root = tk.Tk(className='Sqlite CRUD')
    main()
    root.mainloop()
