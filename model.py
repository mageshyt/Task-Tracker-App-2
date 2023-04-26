import datetime


class Todo:
    def __init__(self,task,category,date_added=None,date_completed=None,status=None, position=None):
        self.task=task
        self.category=category
        # get current date 
        current_time = datetime.datetime.now() # ! day added
        starting_time =f'{current_time.day}/{current_time.month} {current_time.hour}:{current_time.minute}'

     

        # ! if the date is not given then we are setting the date as current time
        self.date_added = date_added if date_added is not None else starting_time 
        
        self.status=status if status is not None else 1 
        # ! 1 --> pending 2 -->finished
        # ! task finished days
        self.date_completed = date_completed if date_completed is not None else 'Pending'
        self.position=position  if  position is not None else None
        # ! if the position is not given then we are setting the position as last

    def __data__(self):
        return f'{self.task},{self.category},{self.date_added},{self.date_completed},{self.status},{self.position}'