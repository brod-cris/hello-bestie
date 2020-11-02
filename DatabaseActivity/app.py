import sqlite3


def writeDetails():
    uname = input('Enter the user firstname:')
    lname = input('Enter the user lastname:')
    email_id = input('Enter the user email_id:')

    try:
        conn = sqlite3.connect('mydb.db')
        cursor = conn.cursor()

        insert_query = "INSERT INTO UserTable(uname, lname, email_id) VALUES(?,?,?)"
        param = (uname, lname, email_id)

        cursor.execute(insert_query, param)

        print('Data inserted successfully')
        conn.commit()

    except Exception as er:
        print(f'Warning: {er}')

    finally:
        conn.close


def readDetails():
    try:
        conn = sqlite3.connect('mydb.db')
        cursor = conn.cursor()

        select_query = "SELECT * from UserTable"
        cursor.execute(select_query)

        rows = cursor.fetchall()

        for row in rows:
            print(
                f'Id : {row[0]}, Name: {row[1]}, Lastname: {row[2]}, Email_id: {row[3]}')

    except Exception as er:
        print(f'Warning: {er}')

    finally:
        conn.close()


if __name__ == "__main__":
    writeDetails()
    readDetails()
