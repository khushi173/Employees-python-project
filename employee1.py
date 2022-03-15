import sqlite3
con = sqlite3.connect('employee3.db')
cur = con.cursor()
sqlite_query = '''CREATE TABLE employee3_table(empCode INTEGER PRIMARY KEY ,
                  name TEXT NOT NULL,
                  phone INTEGER NOT NULL,
                  email VARCHAR NOT NULL,
                  designation TEXT NOT NULL,
                  salary INTEGER NOT NULL,
                  companyName TEXT NOT NULL)'''
#cur.execute(sqlite_query)
print('table is created sucessfully')
sqlite_insert_query = '''INSERT INTO employee3_table
                         (empCode, name, phone,  email, designation, salary, companyName) VALUES
                         (1001, 'JACK', 8945633301, 'jk', 'Manager', 24000, 'TCS'),
                         (1002, 'SCARLET', 7689543945, 'st', 'Assistant Manager',  57000, 'IBM'),
                         (1003, 'JAY', 7689764589, 'jy', 'Receptionist',  66000, 'Cognizant'),
                         (1004, 'SAM', 8998097665, 'sm', 'Accountant',  45000, 'Veritas'),
                         (1005, 'ROSE', 7898654578, 're', 'Salesman',  58000, 'HARMAN')'''
cur.execute(sqlite_insert_query)
con.commit()
print('Content of the employee3 table:')
#2. View All employees
#cur.execute(''' SELECT * FROM employee3_table ''')
#print(cur.fetchall())
#con.close()


#3. Search an employee using employee name
#cur.execute('''SELECT * FROM employee3_table WHERE name = 'SCARLET' ''')
#print(cur.fetchall())
#con.close()

#4.Update an employee details using employee Code
#cur.execute(''' UPDATE employee3_table SET name = 'TOM' WHERE  empCode = 1004 ''')
#print('Table Updated')

#print('Content of the employee table after update:')
#cur.execute(''' SELECT * from employee3_table''')
#print(cur.fetchall())
#con.commit()
#con.close()

#5.Delete an employee using employee Code
#cur.execute(''' DELETE FROM employee3_table WHERE empCode= 1002 ''')
#print('Employee Deleted')
#print('Content of the employee table after deleting:')
#cur.execute(''' SELECT * from employee3_table''')
#print(cur.fetchall())
#con.commit()
#con.close()

#6.Display all the details of employees whose salary is greater than 50000
#cur.execute(''' SELECT * FROM employee3_table WHERE salary > 50000 ''')
#print(cur.fetchall())
#con.close()

#7.Display the count of total number of employees in the company:-
#cur.execute(''' SELECT count(*) FROM employee3_table ''')
#print(cur.fetchall())
#con.close()

#8.Display all the employee details in alphabetical order, within the specific salary range(lower salary amount and higher amount range should be read from the user. Eg: lowersalary range 25000 & higher salary range 60000).
#cur.execute('''SELECT * FROM employee3_table WHERE salary>=25000 AND salary<=60000 ORDER BY name ASC ''')
#print(cur.fetchall())
#con.close()


#9.Display all the employees data, whose salary is less than the average salary of all the employee
cur.execute('''SELECT * FROM employee3_table WHERE salary < (select avg(salary) from employee3_table ); ''')
print(cur.fetchall())
con.close()











