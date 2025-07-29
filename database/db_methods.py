from config import connect_to_database

conn = connect_to_database()
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

def insertData(id,name,email,mobile):
    cur = conn.cursor()
    print('using sundar db for inserting data')
    insert = 'insert into user values(%s,%s,%s,%s)'
    val = (id,name,email,mobile)
    cur.execute(insert,val)
    print('inserted data into user table')
    conn.commit()
    conn.close()
    

def deleteData(id):
    delete = 'delete from user where id = %s'
    val= (id,)
    print('deleted data of id:', id)
    cur.execute(delete, val)
    conn.commit()
    conn.close()


def update():
    return ''


def selectTable():
   select = 'select * from user'
   cur.execute(select)
   for data in cur.fetchall():
       print(data)
   conn.commit()
   conn.close()


def describe():
    desc = 'desc user'
    cur.execute(desc)
    result = cur.fetchall()
    print(result)
    conn.commit()
    conn.close()
    


