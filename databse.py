import sqlite3
from  typing import List
from main import Todo
import datetime


# ! let us create the database

# * first we will connect the database
connect = sqlite3.connect('todo.db')
# * now we will create the cursor
cursor = connect.cursor() # ! it is use to execute sql commad
# * now we will create the table

def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS todo(
        task text,
        category text,
        date_added text,
        date_completed text,
        status integer,
        position integer
        )""")
    connect.commit() # it will run the sql cmd

create_table()

# ! insert the task
def insert_task(todo:Todo):
    cursor.execute('select count(*) FROM todo')
    count = cursor.fetchone()[0] # ! to get the first item
    todo.position = count  if count else 0 # ! if we have no item then start form 0
    with connect:
        cursor.execute("""INSERT INTO todo VALUES(:task,:category,:date_added,:date_completed,:status,:position)""",
        {
            # ! we give all th value for our table
            'task':todo.task,
            'category':todo.category,
            'date_added':todo.date_added,
            'date_completed':todo.date_completed,
            'status':todo.status,
            'position':todo.position
        })

# ! get all of our task 

def get_all_tasks():
    cursor.execute('SELECT * FROM todo')
    tasks = cursor.fetchall()
    todos=[]
    for result in tasks:
        todos.append(Todo(*result)) # ! append all the column 
    return todos
