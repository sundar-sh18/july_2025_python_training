import mysql.connector

conn = mysql.connector.connect(
    host='103.25.175.234',
    user='root',
    password='password'
    )

cur = conn.cursor()


def createTable():
    cur.execute('use sundar')
    print('using sundar db')
    create = '''create table user(
    id int primary key not null,
    name varchar(50),
    email varchar(50),
    mobile varchar(10)
    )'''
    cur.execute(create)
    print('created table user')

def insertData(id,name,email):
    
    insert = 'insert into user values(?,?,?)'
    val = (id,name,email)
    cur.execute(insert,val)
    conn.commit()
    conn.close()
    

def deleteData():
    delete = 'delete from '


def update():
    return ''


def selectTable(table):
   select = 'select * from ?'
   cur.execute(select, table,)
   conn.commit()
   conn.close()



