import sqlite3
con = sqlite3.connect('employee.db')
cur = con.cursor()
sqlite_query = '''CREATE TABLE employee_table(employee_id INTEGER PRIMARY KEY ,
                 first_name TEXT NOT NULL,
                 last_name TEXT NOT NULL,
                 salary INTEGER NOT NULL )'''
#cur.execute(sqlite_query)
print('table is created sucessfully')
sqlite_insert_query = '''INSERT INTO employee_table
                         (employee_id, first_name, last_name,  salary) VALUES
                         (100, 'SIYA', 'PAL', 24000),
                         (101, 'SHIVAM', 'PATIL', 17000),
                         (102, 'KHUSHI', 'JAMWAL', 6000),
                         (103, 'KIRAN', 'KOUR', 4500),
                         (104, 'DIKSHA', 'SHARMA', 4800)'''
#cur.execute(sqlite_insert_query)
con.commit()
print('Content of the employee table:')
cur.execute(''' SELECT * FROM employee_table WHERE first_name = 'KHUSHI' AND last_name = 'JAMWAL' ''')
print(cur.fetchall())
con.close()


