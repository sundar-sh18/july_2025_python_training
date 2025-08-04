from flask import Flask, jsonify, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'roottoor'
app.config['MYSQL_DB'] = 'sundar_cse'

mysql = MySQL(app)
@app.route('/', methods = ['GET','POST'])
def get():
    if request.method == 'GET':
        return render_template('input.html')
    else:
        name = request.form.get('name')
        email = request.form.get('email')

        cur = mysql.connection.cursor()
        sql = "insert into user values (106,%s,%s,'saapsas')"
        val = (name,email)
        cur.execute(sql,val)
        mysql.connection.commit()
        cur.close()
        return 'inserted'


@app.route('/userInfo')
def userInfo():
    id = request.args.get('id')
    sql =''
    if id is None:
        sql = 'select * from user'
    else:
        sql = f'select * from user where id = {id}'
    
    cur = mysql.connection.cursor()
    cur.execute(sql)
    res = cur.fetchall()
    cur.close()
    return render_template('user.html', userlist = res)


@app.route('/getdata')
def getData():
    cur = mysql.connection.cursor()
    cur.execute('select * from user')
    res = cur.fetchall()
    cur.close()
    return jsonify(res)

@app.route('/sample', methods=['post'])
def sample():

    # title = request.form.get('title')
    # content = request.form.get('content')
    json = request.get_json()
    title = json.get('title')
    content = json.get('content')
    cur = mysql.connection.cursor()
    cur.execute('insert into blog (title,content) values (%s,%s)', (title,content))
    mysql.connection.commit()
    cur.close()
    return 'updated'


if __name__ == '__main__':
    app.run()



