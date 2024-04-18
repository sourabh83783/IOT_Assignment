import dbconn

def delete_Employee(EmpId):
 
    conn = dbconn.get_connection()

    query = f"delete from Employee where EmpId = %s;"
    val = (EmpId, )

    cursor = conn.cursor()

    cursor.execute(query, val)

    conn.commit()

    cursor.close()
    conn.close()



delete_Employee(11)












