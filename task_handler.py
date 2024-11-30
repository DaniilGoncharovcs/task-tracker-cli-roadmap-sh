from models import Task, TaskStatus
from json_handler import JsonHandler

class TaskHandler:

    def __init__(self):
        self.json_handler = JsonHandler()
        self.task_list: list[Task] = self.json_handler.load_tasks()

        print(self.task_list)

        test_task = self.task_list[0]

        test_task.id = 2

        #self.json_handler.dump_task(test_task)

    def get_tasklist():
        pass

    def create_task():
        pass
    
    def update_task():
        pass

    def remove_task():
        pass
