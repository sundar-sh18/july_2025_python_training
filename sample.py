# print("HELLO WORLD")
# name = input("Please Enter the Name : ")
# print(f'Youre name is {name}')



# age = input('Enter the Age of a Person : ')
# if(int(age) < 10):
#     print("You're child")
# else:
#     print("You're not a child")




# num = int(input("Enter a number: "))

# for i in range(1,num+1):
#     print(i)




# arr = [10,23,1,54,2,54,6]
# index = int(input("Enter a index to search: "))
# if(index > len(arr)-1):
#     print("Array index out of bound")
# else: 
#     print(f'Number is : {arr[index]}')


# from datetime import datetime
# fname = str(datetime.now()).replace('.', '_')
# file = fname.replace(":", '_')
# msg = input("Enter a message : ")
# with open(file+'.txt', 'w') as file_:
#     file_.write(msg)
# print(f'message written successfully')





import sqlite3
conn = sqlite3.connect('mydata.db')
cur = conn.cursor() 
# cur.execute('''
#     create table if not exists users(
#         id integer primary key autoincrement,
#         name text not null,
#         age integer
#     )
#     '''
#     )

# conn.commit()
# conn.close()



# try:
#     num = int(input('Enter a num: '))
#     if(num < 0):
#         raise Exception("IT IS A NOT A NUMBER")
# except Exception as err:
#     print(err)



# try:
#     num1 = int(input('Enter a Number:  '))
#     num2 = int(input('Enter another Number:  '))
#     op = input('Enter a operator : ')

#     if(op == '+'):
#         print(f'{num1}{op}{num2} = {num1+num2}')
#     if(op == '-'):
#         print(f'{num1}{op}{num2} = {num1-num2}')
#     if(op == '*'):
#         print(f'{num1}{op}{num2} = {num1*num2}')
#     if(op == '/'):
#         print(f'{num1}{op}{num2} = {num1//num2}')
#         raise Exception("Denominator cannot be Zero")

    
# except Exception as e:
#     print(e)

# except:
#     print("invalid Operator")



# cur.execute('insert into users (name, age) values(?,?)',('Sundar S', 21))
# cur.execute('insert into users (name,age) values (?,?)', ('Hema', 21))

select = 'select * from users'
insert = 'insert into users (name, age) values(?,?)'
delete = 'delete from users where id=?'
update = 'update users set age=? where id=?'


n = int(input('Enter the number of users you want to insert : '))
for i in range(n):
    name = input('Enter the name : ')
    age = int(input('Enter the age: '))
    val = (name,age)
    cur.execute(insert,val)
print(cur.rowcount, 'rows affected')
cur.execute(select)
rows = cur.fetchall()

for data in rows:
    print(data)
conn.commit()
conn.close()