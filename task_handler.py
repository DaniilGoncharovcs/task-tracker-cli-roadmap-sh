from copy import deepcopy
from datetime import datetime
from models import Task, TaskStatus
from json_handler import JsonHandler

class TaskHandler:

    def __init__(self):
        self.json_handler = JsonHandler()
        self.task_list: list[Task] = self.json_handler.load_tasks()

    def get_tasklist(self, filter_argument: str):
        print('##### Task List #####')
        print('id\tstatus\tdescription\tcreatedAt\t\tupdatedAt')
        print('-' * 80)

        match filter_argument:
            case 'todo':
                filter = 1
            case 'in-progress':
                filter = 2
            case 'done':
                filter = 3

        for task in self.task_list:
            if task.status == filter:
                print(task.id, filter_argument, task.description, task.createdAt, task.updatedAt, sep='\t')
    
    def create_task(self, arguments: list[str]):
        new_task = Task(
            id=len(self.task_list) + 1,
            description=' '.join(arguments),
            status=TaskStatus.todo.value,
            createdAt=datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
            updatedAt=datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
        )

        self.json_handler.dump_task(new_task)
    
    def update_task(self, id: int, description: list[str]):
        old_task = [task for task in self.task_list if task.id == id][0]
        updated_task = Task(
            id=old_task.id,
            description=' '.join(description),
            status=old_task.status,
            createdAt=old_task.createdAt,
            updatedAt=datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        )

        self.json_handler.dump_task(updated_task)       

    def delete_task(self, id: int):
        self.json_handler.remove_file()  
