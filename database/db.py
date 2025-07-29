import sqlite3
conn = sqlite3.connect('e_commerce.db')
cur = conn.cursor()
cur.execute("PRAGMA foreign_keys = ON;")


cur.execute(''' create table if not exists Customer(
            u_id integer primary key autoincrement,
            name text not null,
            email text not null,
            password text not null
        )
    ''')

cur.execute('''

            create table if not exists Orders(
            o_id integer primary key autoincrement,
            c_id integer not null references Customer (u_id),
            amt integer not null,
            date text not null )
            ''')

cur.execute('''
create table if not exists Product(
            p_id integer primary key autoincrement,
            name text not null,
            price integer not null,
            desc text)
            ''')

cur.execute('''
create table if not exists Payment(
            pay_id integer primary key autoincrement,
            type text not null,
            amt integer not null)
            ''')

cur.execute('''
create table if not exists Category(
            cat_id integer primary key autoincrement,
            name text not null,
            picture text,
            desc text)
            ''')

cur.execute('''
create table if not exists Cart(
            cart_id integer primary key autoincrement,
            u_id integer references Customer (c_id))
            ''')
conn.commit()
conn.close()
