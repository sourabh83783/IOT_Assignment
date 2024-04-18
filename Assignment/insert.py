import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "sunbeam",
    password = "sunbeam",
    database = "iotdb"
)

EmpId = int(input("Enter the Employee ID : "))
Name = input("Enter the Name of Employee : ")
Department = input("Enter the Department of the Employee : ")
Email = input("Enter the Email of the Employee : ")
Salary = int(input("Enter the Salary of the employee :"))
DOB = input("Enter the Date of joining of the Employee : ")

query = f"Insert into Employee values({EmpId}, '{Name}', '{Department}', '{Email}',{Salary},'{DOB}');"

cursor = connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()

connection.close()