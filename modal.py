from datetime import datetime


class TODO:
    def __init__(self,task,category,date_added=None,date_completed=None,status=None, positon=None):
        self.task=task
        self.category=category
        # ! if the date is not given then we are setting the date as current time
        self.date_added=date_added if date_added is not None else datetime.datetime.now().isoformate()
        self.date_completed=date_completed  if date_completed is not None else None
        self.status=status if status is not None else 1 
        # ! 1 --> pending 2 -->finished
        self.positon=positon  if  position is not None else None
        # ! if the position is not given then we are setting the position as last

    def __data__(self):
        return f'{self.task},{self.category},{self.date_added},{self.date_completed},{self.status},{self.positon}'