import sqlite3
con = sqlite3.connect('employs.db')

cur = con.cursor()

sqlite_select_query1 = '''SELECT * FROM emp_marks'''

cur.execute(sqlite_select_query1)
records = cur.fetchall()
print(records)

'''for row in records:
    print('id:', row[0])
    print('name:',row[1])
    print('marks:',row[2])'''

con.close()