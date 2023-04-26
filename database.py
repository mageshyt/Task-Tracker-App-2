import sqlite3
from  typing import List
from model import Todo
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


# !  delete the task 
def delete_task(position:int):
    cursor.execute('select count(*) from todo')
    count= cursor.fetchone()[0] # ! fetch only one
    with connect:
        cursor.execute("DELETE from todo WHERE position=:position", {"position": position})
        for position in range(position+1,count):
            change_position(position,position-1,False)
            # ! here we are shifting the position of the task one by one


def change_position(old_position,new_position,commit=True):
    cursor.execute('UPDATE todo SET position=:new_position WHERE position=:old_position',{'old_position':old_position,'new_position':new_position})
    if commit:
        connect.commit()


# ! update the task
def update_task(position:int,task:str=None,category:str=None):
    with connect:

            # !we are setting out task and category if they both are given to the given position
        if task is not None and category is not None:
            cursor.execute("""UPDATE todo SET task=:task,category=:category WHERE position=:position""",
            {
                'task':task,
                'category':category,
                'position':position
            })
        #! we set the task only if task  only  given
        elif task is not None:
            cursor.execute("""UPDATE todo SET task=:task WHERE position=:position""",
            {
                'task':task,
                'position':position
            })
        # ! we set the category only if category  only  given
        elif category is not None:
            cursor.execute("""UPDATE todo SET category=:category WHERE position=:position""",
            {
                'category':category,
                'position':position
            })

#! complete the todo
def complete_task(position:int):
    current_time = datetime.datetime.now() 
    end_time=f'{current_time.day}/{current_time.month} {current_time.hour}:{current_time.minute}'
    with connect:
        cursor.execute("""UPDATE todo SET status=2,date_completed=:date_completed WHERE position=:position""", 
        {
            'date_completed':end_time,
            'position':position
        })
        