from flask import Flask, jsonify, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST']= '103.25.175.234'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'sundar'

mysql = MySQL(app)
@app.route('/')
def myHtml():
    return render_template('input.html')

@app.route('/about/<name>')
def about(name):
    return jsonify({'name': name, 'email': 'sundar@gmail.com'})


@app.route('/mydetails', methods = ['get','post'])

@app.route('/getdata')
def getData():
    cur = mysql.connection.cursor()
    cur.execute('select * from user')
    res = cur.fetchall()
    cur.close()
    return jsonify(res)

if __name__ == '__main__':
    app.run()



