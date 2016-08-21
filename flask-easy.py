from passlib.apps import custom_app_context as pwd_context
from flask import Flask, abort, jsonify, request
from flask_httpauth import HTTPBasicAuth
import sqlite3 as sql
import hashlib

app = Flask(__name__)
auth = HTTPBasicAuth()

@app.route('/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
    conn = sql.connect('database.db')
    cur = conn.cursor()
    cur.execute("select * from Tasks")
    rows = cur.fetchall()
    task_list = list()
    for row in rows:
        each_task = dict()
        each_task['Uri'] = row[0]
        each_task['Title'] = row[1]
        each_task['Description'] = row[2]
        each_task['Done'] = row[3]
        task_list.append(each_task)
    conn.close()
    return jsonify(task_list)

@app.route('/tasks', methods=['POST'])
@auth.login_required
def create_task():
    if not request.json or not 'Uri' in request.json:
        abort(400)    
    conn = sql.connect('database.db')
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO Tasks (Uri,Title,Description,Done) VALUES (?,?,?,?)"
        , (request.json['Uri'], request.json['Title'], request.json.get('Description', ''), 0))
        conn.commit()
    return jsonify({'Message': 'Insert successfully'}), 201

@app.route('/users', methods=['POST'])
@auth.login_required
def insert_user():
    conn = sql.connect('database.db')
    cur = conn.cursor()
    #hash = hashlib.md5()
    #hash.update(request.json['password'].encode('utf-8'))
    cur.execute("INSERT INTO Users (username,password) VALUES (?,?)"
    , (request.json['username'], pwd_context.encrypt(request.json['password'])))
    conn.commit()
    return jsonify({'Message': 'Insert successfully'})

@app.route('/tasks/<task_id>', methods=['DELETE'])
@auth.login_required
def delete_task(task_id):   
    conn = sql.connect('database.db')
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM Tasks WHERE Uri=(?)", (task_id,))
        msg = "delete successfully!"
        conn.commit()
    except:
        msg = "Something wrong!"
    finally:
        conn.close()	    
        return jsonify({'Message': msg})

@app.route('/tasks/<task_id>', methods=['PUT'])
@auth.login_required
def update_task(task_id):
    # You need to update Title and Description column.
    # Then, return your response and correct response code to your client!
    conn = sql.connect('database.db')
    cur = conn.cursor()
    try:
        cur.execute("UPDATE Tasks SET Title = 'success!!' WHERE Uri=(?)", (task_id,))
        msg = "update successfully!"
        conn.commit()
    except:
        msg = "Something wrong!"
    finally:
        conn.close()	    
        return jsonify({'Message': msg})
	
    

@app.route('/tasks/<task_id>', methods=['GET'])
@auth.login_required
def get_a_task(task_id):
    # You need to select a specific task and return to your client.
    conn = sql.connect('database.db')
    cur = conn.cursor()
    cur.execute("select * from Tasks WHERE Uri=(?)",(task_id,))
    row = cur.fetchone()
    each_task = dict()
    each_task['Uri'] = row[0]
    each_task['Title'] = row[1]
    each_task['Description'] = row[2]
    each_task['Done'] = row[3]
    conn.close()
    return jsonify(each_task)




def hash_password(password):
    password_hash = pwd_context.encrypt(password)
    return password_hash

def verify_hash(password, password_hash):
    return pwd_context.verify(password, password_hash)

@auth.verify_password
def verify_password(username, password):
    
    con = sql.connect('database.db')
    cur = con.cursor()    
    cur.execute("SELECT * FROM Users WHERE username =(?)", (username, ))
    row = cur.fetchone()
    if row:
	    return verify_hash(password, row[1])
    else:
	    return False


if __name__ == '__main__':
    app.run(debug=True)