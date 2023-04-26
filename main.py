import typer
from rich.table import Table
from rich.console import Console

# import out database and modal

from database import get_all_tasks, insert_task, delete_task, insert_task, update_task, complete_task
from model import Todo
console = Console()
app = typer.Typer()


#  * decorator the terminal
#! Add method
@app.command(short_help='adds an item')
def add(task: str, category: str):
    typer.echo(f'Adding {task} to {category}')  # use to print in terminal
    # ! we create a new task
    todo = Todo(task, category)
    # ! now we will insert the task
    insert_task(todo)
    show()

# ! delete method


@app.command(short_help='deletes an item')
def delete(position: int):
    typer.echo(f'Deleting item {position}')
    # *indices in our UI begins from 1 but in our database starts from 0 so we minus -1
    delete_task(position-1)

    show()

#!updating the item


@app.command(short_help='updates an item')
def update(position: int, task: str = None, category: str = None):
    typer.echo(f"updating {position}")
    update_task(position-1, task, category)
    show()
# ! complete method


@app.command(short_help='completes an item')
def complete(position: int):
    typer.echo(f'Completing item {position}')
    complete_task(position-1)
    show()

#! delete from items


@app.command(short_help='deletes all items')
def delete_from(position: int):
    tasks = get_all_tasks()
    typer.echo('Deleting all items')
    print(position)
    for idx in range(position):
        delete_task(idx-1)

    # delete_task(0)
    show()
# !show method


@app.command(short_help='shows all items')
def show():
    tasks = get_all_tasks()
    console.print('[bold magenta]Your Task[/bold magenta]!', '📈')
    # * here we are declaring the console using rich library
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column('No', style='bright', width=6)
    table.add_column('Task', min_width=20)
    table.add_column('Category', min_width=12, justify='right')
    table.add_column('status', min_width=12, justify='right')
    table.add_column('date added', min_width=12, justify='right')
    table.add_column('date added', min_width=12, justify='right')

    # for category color method
    def category_color(category):
        colors = {'coding': 'green', 'shopping': 'yellow', 'Home': 'blue',
                  'work': 'red', 'other': 'magenta', 'workout': 'cyan'}
        if category in colors:
            return colors[category]
    # ! if we find that category in the dictionary then return the
    # !color otherwise return default as white
        return 'pink'
    for idx, task in enumerate(tasks, start=1):
        clr = category_color(task.category)
        task_status = '✅' if task.status == 2 else '😅'
        table.add_row(str(idx), task.task, f'[{clr}]{task.category}[/{clr}]',
                      task_status, task.date_added, task.date_completed)
    console.print(table)


if __name__ == '__main__':
    app()
