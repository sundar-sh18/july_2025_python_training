import mysql.connector
def connect_to_database():
    conn = mysql.connector.connect(
    host='103.25.175.234',
    user='root',
    password='password',
    database='sundar'
    )
    return conn 

