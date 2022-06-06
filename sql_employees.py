
import mysql.connector
 
con = mysql.connector.connect(host="localhost", user="root", password="password", database="employees")


def Add_Employ():
 
    Id = input("Enter employee Id : ")
   
    if(check_employee(Id) == True):
        print("Employee aready exists\nTry Again\n")
        menu()
         
    else:
        First_name = input("Enter Employee First_name : ")
        Last_name  = input("Enter employee Last_name: ")
        Age = input("Enter employee age: ")
        Job = input("Enter employee Post : ")
        Salary = input("Enter employee Salary : ")
        data = (Id, First_name, Last_name, Age, Job, Salary)
     
        sql = 'insert into employees values(%s,%s,%s,%s,%s,%s)'
        c = con.cursor()
         
      
        c.execute(sql, data)
         
        con.commit()
        print("Employee Added Successfully ")
        menu()

def Promote_Employee():
    Id = float(input("Enter Employ's Id"))
     
   
    if(check_employee(Id) == False):
        print("Employee does not  exists\nTry Again\n")
        menu()
    else:
        Amount = int(input("Enter increase in Salary"))
        sql = 'select salary from employees where id=%s'
        data = (Id,)
        c = con.cursor()  
        c.execute(sql, data)
        r = c.fetchone()
        t = r[0]+Amount
         
        sql = 'update employees set salary=%s where id=%s'
        d = (t, Id)
      
        c.execute(sql, d)
         
        con.commit()
        print("Employee Promoted")
        menu()


def Remove_Employ():
    Id = input("Enter employee Id : ")
    if(check_employee(Id) == False):
        print("Employee does not  exists\nTry Again\n")
        menu()
    else:
        sql = 'delete from employees where id=%s'
        data = (Id,)
        c = con.cursor()
         
        
        c.execute(sql, data)
         
       
        con.commit()
        print("Employee Removed")
        menu()
 

def check_employee(employee_id):
    sql = 'select * from employees where id=%s'
    c = con.cursor(buffered=True)
    data = (employee_id,)
    c.execute(sql, data)
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False
 

def Display_Employees():
     
   
    sql = 'select * from employees'
    c = con.cursor()
     
    c.execute(sql)
     

    r = c.fetchall()
    for i in r:
        print("Employee Id : ", i[0])
        print("Employee First_name : ", i[1])
        print("Employee Last_name : ", i[2])
        print("Employee Age: ", i[3])
        print("Employee Salary : ", i[4])
        print("---------------------\
        -----------------------------\
        ------------------------------\
        ---------------------")
         
    menu()
 

def menu():
    print("Welcome to employee management record")
    print("Press ")
    print("1 to Add employee")
    print("2 to Remove employee ")
    print("3 to Promote employee")
    print("4 to Display employees")
    print("5 to Exit")
 
    ch = int(input("Enter your choice "))
    if ch == 1:
        Add_Employ()
    elif ch == 2:
        Remove_Employ()
    elif ch == 3:
        Promote_Employee()
    elif ch == 4:
        Display_Employees()
    elif ch == 5:
        exit(0)
    else:
        print("Invalid choice")
        menu()
 
 

menu()