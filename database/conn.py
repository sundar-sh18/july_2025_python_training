import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='roottoor',
    database='sundar_cse'
)

print(conn)

cur = conn.cursor()
