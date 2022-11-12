from flask import Flask,  render_template, request
import os
import sqlite3

app = Flask(__name__)

## initialize the sqlite database
## database.db will be created
## In the schema, everytime this executescript is run, it will remove existing data and create a new table.

connection = sqlite3.connect('database.db')
with open('schema.sql') as f:
    connection.executescript(f.read())


@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/page1/')
def page1():
    return render_template("page1.html")

@app.route('/form', methods = ['GET','POST'])
def form():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        display_text = "You have submitted the username of: " + str(user) + " : " + password 
        connection = sqlite3.connect('database.db')
        cur = connection.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                (user, password)
                )
        connection.commit()
        connection.close()

    elif request.method == 'GET':
        display_text = "You have submitted a GET requrest. No form data available."
    return render_template("form.html",display_text=display_text)

@app.route('/read_db/')
def read_db():
    connection = sqlite3.connect('database.db')
    users = connection.execute('SELECT * FROM users').fetchall()
    connection.close()
    return render_template('read_db.html', users=users)

if __name__ == '__main__':
    # run flask server on this machine's local host
    # works with cloud servers
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)), use_reloader=False, debug=True)