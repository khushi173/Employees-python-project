import sqlite3
def insertData (id, name, marks) :
    con = sqlite3.connect('employs.db')
    cur = con.cursor()

#parametrized query
    insert_query = '''INSERT INTO emp_marks
                      VALUES (?,?,?)'''
    cur.execute(insert_query, (id, name, marks))

    con.commit()

    con.close()

a= int(input('enter the employs id:'))
b = input('enter the employs name:')
c = int(input('enter the employs mark:'))
insertData(a,b,c)