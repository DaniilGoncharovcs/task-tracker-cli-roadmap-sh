from datetime import datetime
from dataclasses import dataclass, field
from enum import Enum

class TaskStatus(Enum):
    todo = 1
    in_progress = 2
    done = 3

@dataclass
class Task:
    id: int
    description: str = field()
    status: TaskStatus = field()
    createdAt: datetime = field()
    updatedAt: datetime = field()
    filename: str = field()

    @classmethod
    def from_dict(cls, data: dict, file_name: str):
        try:
            task_id = int(data.get('id', None))
        except ValueError:
            exit(f"Error: can't convert id from {file_name}")

        try: 
            task_status = int(data.get('status', None))
            if task_status not in [1,2,3]:
                raise ValueError
        except ValueError:
            exit(f"Error: can't convert status from {file_name}")

        try:
            task_created = datetime.strptime(data.get('createdAt', ''), '%Y-%m-%d %H:%M:%S')
            task_updated = datetime.strptime(data.get('updatedAt', ''), '%Y-%m-%d %H:%M:%S')
        except ValueError:
            exit(f"Error: can't convert date from {file_name}")

        return cls(
            id = task_id,
            description = data.get('description'),
            status = task_status,
            createdAt = task_created,
            updatedAt = task_updated,
            filename = file_name
        )
