from config import connect_to_database

conn = connect_to_database()
cur = conn.cursor()

class Database:
    def insert(self,id,name,email,mobile):
        insert = 'insert into user values(%s,%s,%s,%s)'
        val = (id,name,email,mobile)
        cur.execute(insert,val)
        print('inserted data into user table')
        conn.commit()
        conn.close()