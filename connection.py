import sqlite3


def main():
    try:
        sqliteConnection = sqlite3.connect('chinook.db')
        cursor = sqliteConnection.cursor()
        print("Database created and Successfully Connected to SQLite")

        sqlite_select_query = """SELECT LastName , Title FROM employees e  """
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        # print("Printing each row")
        # for row in records:
        #     print("Name: ", row[0])
        #     print("Title: ", row[1])
        #     print("\n")
        print(records)

        cursor.close()
    except sqlite3.Error as exception:
        print("Database not created and Failed to Connect" + exception)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


if __name__ == '__main__':
    main()
