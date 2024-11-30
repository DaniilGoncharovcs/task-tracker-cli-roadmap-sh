from dataclasses import asdict
from pathlib import Path
from json import dump, loads, JSONDecodeError
from models import Task

class JsonHandler:
    def __init__(self):
        self.tasks_path = Path("json_tasks")
        self.tasks_path.mkdir(parents=True, exist_ok=True)
        pass

    def load_tasks(self) -> list[Task]:
        files_path = self.tasks_path.glob('*.json')
        file_names = [file for file in files_path if file.is_file()]
        
        task_list: list[Task] = []
        for file in file_names:
            with file.open() as f:
                try:
                    json_dict = loads(f.read())
                    task = Task.from_dict(json_dict, file.name)
                    
                    task_list.append(task)
                except JSONDecodeError:
                    print(f'Failed to load task from {file.name}')
                    exit(1)
        
        return task_list
    
    def dump_task(self, task: Task):
        file_path = Path(f'{self.tasks_path.name}/task{task.id}.json')
        print(file_path)
        with file_path.open('w', encoding='UTF-8') as f:
            dump(asdict(task), f, indent=4, default=str)
