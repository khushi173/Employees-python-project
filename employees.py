import sqlite3
con = sqlite3.connect('employees.db')
cur = con.cursor()
sqlite_query = '''CREATE TABLE if not exists employees(
                  empCode INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  phone INTEGER NOT NULL UNIQUE,
                  email TEXT NOT NULL UNIQUE,
                  designation TEXT NOT NULL,
                  salary REAL NOT NULL,
                  company_name TEXT NOT NULL)'''
cur.execute(sqlite_query)
check=1
while check:
    c = int(input(
     " Main Menu\n1) Add new Record\n2) View all Records \n3) Search specific record by name \n"
 "4) Update specific record \n5) Delete specific record \n"
 "6) Display all details of Employee whose salary is greater than 50000 \n"
 "7) Display the count of total records \n8) All the employees details in alphabetical order, within the specific salary range \n"
 "9) All the employees data, whose salary is less than the average salary of all the employees \n10) Exit\n"))
    if c == 1:
        n = int(input("Enter How Many Record You Enter? "))
        for i in range(n):
            empCode = int(input("Enter Id:"))
            name = (input("Enter Name: "))
            phone = int(input("Enter Phone Number: "))
            email = (input("Enter Address: "))
            designation = (input("Enter Designation: "))
            salary = int(input("Enter the Salary: "))
            company_name = (input("Enter company name: "))
            sqlite_insert_query = f"insert into employees VALUES ({empCode},'{name}',{phone},'{email}','{designation}',{salary},'{company_name}')"
            cur.execute(sqlite_insert_query)
            con.commit()
    elif c == 2:
         select_query = "SELECT * FROM employees"
         cur.execute(select_query)
         result = cur.fetchall()
         for record in result:
             print(record)
    elif c == 3:
        id1 = input("Enter Name:")
        search_query = f"SELECT * FROM employees WHERE name='{id1}' "
        cur.execute(search_query)
        result1 = cur.fetchall()
        for record in result1:
            print(record)
        con.commit()
    elif c == 4:
       id2 = int(input("Enter Empcode:"))
       addr2 = (input("Enter the updated name: "))
       update_query = f"update employees set name='{addr2}' where empCode={id2}"
       cur.execute(update_query)
       print(cur.rowcount, "Record updated")
       con.commit()
    elif c == 5:
       id3 = int(input("Enter Id:"))
       delete_query = f"delete from employees where empCode={id3}"
       cur.execute(delete_query)
       print(cur.rowcount, "Record deleted")
       con.commit()
    elif c == 6:
       sqlite_select1_query = '''SELECT * FROM employees WHERE salary>50000 '''
       cur.execute(sqlite_select1_query)
       record3 = cur.fetchall()
       for record in record3:
           print(record)
       con.commit()
    elif c == 7:
       sqlite_count_query = '''SELECT COUNT(*) FROM employees; '''
       cur.execute(sqlite_count_query)
       record4 = cur.fetchall()
       print(record4)
       con.commit()
    elif c == 8:
       print("All the employees details in alphabetical order, within the specific salary range of 20000 & 60000: ")
       sqlite_display_query = '''SELECT * FROM
       employees
       WHERE
       salary > 20000
       AND
       salary < 60000
       ORDER
       BY
       name; '''
       cur.execute(sqlite_display_query)
       record5 = cur.fetchall()
       for record in record5:
            print(record)
    elif c == 9:
       print("All the employees data, whose salary is less than the average salary of all the employees: ")
       sqlite_display1_query = '''select * from employees where salary < (select
avg(salary) from employees); '''
       cur.execute(sqlite_display1_query)
       record6 = cur.fetchall()
       for record in record6:
           print(record)
           con.commit()
       else:
           print("Program Terminated")
           check = 0
           print("ThanK You")