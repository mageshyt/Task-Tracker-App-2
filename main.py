from turtle import width
import typer
from rich.table import Table
from rich.console import Console

console = Console()
app=typer.Typer()


#  decorator the terminal
#! Add method
@app.command(short_help='adds an item')
def add(task:str ,category:str):
    typer.echo(f'Adding {task} to {category}') # use to print in terminal
    show()

# ! delete method
@app.command(short_help='deletes an item')
def delete(position:int):
    typer.echo(f'Deleting item {position}')
    show()

#!updating the item
@app.command(short_help='updates an item')
def update(position:int,task:str=None,category:str=None):
    typer.echo(f'Updating item {position}')
    show()

# !show method
@app.command(short_help='shows all items')
def show():
    tasks = [('Buy milk', 'Home'), ('Buy eggs', 'Home'), ('Buy bread', 'Home')]
    console.print('[bold magenta]Todos[/bold magenta]!','🖥️') 
    # * here we are declaring the console using rich library
    table=Table(show_header=True, header_style="bold magenta")
    table.add_column('#',style='dim',width=6)
    table.add_column('Task',min_width=20)
    table.add_column('Category',min_width=12,justify='right')
    table.add_column('Done',min_width=12,justify='right')
    # for category color method
    def category_color(category):
        colors={'coding':'green','shopping':'yellow','Home':'blue','work':'red'}
        if category in colors:
            return colors[category]
    # ! if we find that category in the dictionary then return the 
    # !color otherwise return default as white
        return 'white'
    for i , task in enumerate(tasks,start=1):
        clr=category_color(task[1]) #! here we are calling the category color method to get the color for the added task
        # ! we are checking if the task is done or not 
        task_status_check= '✅' if True  else '❌'
        table.add_row(str(i),task[0],f'[{clr}]{task[1]}[/{clr}]',task_status_check)
    console.print(table)
        # * if the task is done

if __name__ == '__main__':
    app()