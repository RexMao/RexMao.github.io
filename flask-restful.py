from flask import Flask, request
from flask_restful import Resource, Api, reqparse, fields, marshal_with
import sqlite3 as sql
import json

app = Flask(__name__)
api = Api(app)

# this function is try to validate Title argument.
def title_validation_function(value):
    return value+"revised"
    
    '''
    # if you want to check the input is a formed JSON.
    try:
        return json.loads(data)
    except:
        raise ValueError('Malformed JSON')
    '''

# define output format, it can control what can be seen by our clients
resource_fields = {
    # 'Uri': fields.String,
    'Title': fields.String,
    'Description': fields.String}

# Task
# shows a single task item and lets you delete a task item	
class Task(Resource):
    def get(self, task_id):
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
        return each_task

    def delete(self, task_id):
        conn = sql.connect('database.db')
        cur = conn.cursor()
        try:
            cur.execute("DELETE FROM Tasks WHERE Uri=(?)", (task_id,))
            msg = "delete sucessfully!"
            conn.commit()
        except:
            msg = "Something worong!"
        finally:
            conn.close()
            return {'Message': msg}

    def put(self, task_id):
        conn = sql.connect('database.db')
        cur = conn.cursor()
        try:
            cur.execute("UPDATE Tasks SET Title = (?) WHERE Uri=(?)", (request.json['Title'],task_id,))
            msg = "update successfully!"
            conn.commit()
        except:
            msg = "Something wrong!"
        finally:
            conn.close()	    
            return {'Message': msg}

# TaskList
# shows a list of all tasks, and lets you POST to add new tasks		
class TaskList(Resource):
    
    def __init__(self):
        #Initial reqparse.RequestParser() to help control request arguments
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(name='Uri', location='json',required=True, type=str, help='id for this resource')
        self.parser.add_argument(name='Title', location='json', type=title_validation_function)
        self.parser.add_argument(name='Description', location='json')
	
    @marshal_with(resource_fields)
    def get(self):
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
        return task_list
    
    def post(self):
        conn = sql.connect('database.db')
        cur = conn.cursor()
        with conn:
            args = self.parser.parse_args()
            task = (args['Uri'], args['Title'], args['Description'],0)
            cur.execute("INSERT INTO Tasks (Uri,Title,Description,Done) VALUES (?,?,?,?)"
            , task)
            conn.commit()
        return task, 201

##
## Actually setup the Api resource routing here
##		
api.add_resource(TaskList, '/tasks')
api.add_resource(Task, '/tasks/<task_id>')

if __name__ == '__main__':
    app.run(debug=True)