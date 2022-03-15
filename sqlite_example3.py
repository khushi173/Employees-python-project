import sqlite3
con = sqlite3.connect('customer.db')
cur = con.cursor()

sqlite_query1 = '''CREATE TABLE customer_table(id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL, 
                 marks INTEGER NOT NULL,
                 city TEXT NOT NULL)'''
#cur.execute(sqlite_query1)
print('table is created sucessfully')
sqlite_insert_query1 = '''INSERT INTO customer_table
                         (id, name, marks, city) VALUES
                         (1, 'SAM', 45, 'Pune'),
                         (2, 'RAM', 35, 'Banglore'),
                         (3, 'SUMIT', 25, 'Chennai'),
                         (4, 'TOM', 30, 'Delhi'),
                         (5, 'ROHIT', 50, 'Jammu'),
                         (6, 'SIYA', 45, 'Gujarat'),
                         (7, 'ARUSHI', 20, 'Jaipur'),
                         (8, 'MAYUR', 31, 'Agra'),
                         (9, 'JOHN', 44, 'UP'),
                         (10, 'JAY', 22, 'Mumbai')'''
#cur.execute(sqlite_insert_query1)
con.commit()
print('Content of the customer table:')
cur.execute(''' SELECT * from customer_table  ''')
print(cur.fetchall())

#updating the record
sql = ''' UPDATE customer_table SET city = 'Indore' WHERE  id = 3'''
cur.execute(sql)
print('Table Updated')

print('Content of the customer table after update:')
cur.execute(''' SELECT * from customer_table''')
print(cur.fetchall())
con.commit()
con.close()

