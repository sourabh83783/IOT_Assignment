import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "sunbeam",
    password = "sunbeam",
    database = "iotdb"
)

#query = "select * from Employee order by Salary DESC;"" select Name from Employee;"" select * from Employee; "

#cursor = connection.cursor()

#cursor.execute(query)

#records = cursor.fetchall()     

#print(records)

#cursor.close()

#connection.close()

query1 = "select * from Employee order by Salary DESC;"
query2 = " select Name from Employee;"
query3 = " select Department from Employee;"
query4 = "select * from Employee order by Salary ASC;"

cursor = connection.cursor()

temp = input("Enter your choice : ")
if(temp == "high"):
    
    cursor.execute(query1)

    records = cursor.fetchall()     

    print(records)

elif(temp == "low"):

    cursor.execute(query4)

    records = cursor.fetchall()     

    print(records)

cursor.execute(query2)

records = cursor.fetchall()     

print(records)

cursor.execute(query3)

records = cursor.fetchall()     

print(records)

cursor.close()

connection.close()