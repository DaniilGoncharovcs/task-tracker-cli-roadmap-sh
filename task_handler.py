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
        print('id\tstatus     \tdescription\tcreatedAt\t\tupdatedAt')
        print('-' * 80)

        match filter_argument:
            case 'todo':
                filter = 1
            case 'in-progress':
                filter = 2
            case 'done':
                filter = 3
            case _:
                filter = None

        for task in self.task_list:
            if filter is None or task.status == filter:
                status_str = TaskStatus(task.status).name
                print(task.id, status_str, task.description, task.createdAt, task.updatedAt, sep='\t')
    def create_task(self, arguments: list[str]):
        new_task_id = len(self.task_list) + 1

        new_task = Task(
            id=new_task_id,
            description=' '.join(arguments),
            status=TaskStatus.todo.value,
            createdAt=datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
            updatedAt=datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
            filename = f'task{new_task_id}.json'
        )

        self.json_handler.dump_task(new_task)
    
    def update_task(self, id: int, description: list[str]):
        old_task = self.find_task_by_id(id)

        updated_task = Task(
            id=old_task.id,
            description=' '.join(description),
            status=old_task.status,
            createdAt=old_task.createdAt,
            updatedAt=datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
            filename = f'task{old_task.id}.json'
        )

        self.json_handler.dump_task(updated_task)       

    def delete_task(self, id: int):
        deleted_task = self.find_task_by_id(id)

        self.json_handler.remove_json(deleted_task)
    
    def mark_task(self, mark_type: str, id: int):
        marked_task = self.find_task_by_id(id)
        match mark_type:
            case 'mark-in-progress':
                marked_task.status = TaskStatus.in_progress.value
            case 'mark-done':
                marked_task.status = TaskStatus.done.value
            case _:
                exit(f'Error: Unknown mark type {mark_type}')        

        self.json_handler.dump_task(marked_task)
    
    def find_task_by_id(self, id: int) -> Task:
        try:
            return self.task_list[id - 1]
        except IndexError:
            exit(f'Error: task with id {id} was not found')
