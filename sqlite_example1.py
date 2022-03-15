import sqlite3
con = sqlite3.connect('employs.db')
cur = con.cursor()

sqlite_query1 = '''CREATE TABLE emp_marks(id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL, 
                 marks INTEGER NOT NULL)'''
#cur.execute(sqlite_query1)
print('table is created sucessfully')
sqlite_insert_query1 = '''INSERT INTO emp_marks
                         VALUES(1101, 'KHUSHI',199)'''
#cur.execute(sqlite_insert_query1)
print('a student record is inserted')
con.commit()
print(cur.fetchall())
con.close()
