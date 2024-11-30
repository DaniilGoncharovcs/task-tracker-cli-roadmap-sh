from sys import argv

class ConsoleHandler:
    def __init__(self):
        self.arguments = argv
        self.command: str = self.get_command()
        self.command_arguments: list[str] = None

        if self.command not in ['add', 'update', 'delete', 'mark-in-progress', 'mark-done', 'list']:
            print('Please use one of this command:')
            print('# add - Adding a new task')
            print('task-cli add Buy groceries\n')
            print('# update - Update task by task id')
            print('task-cli update 1 Buy groceries and cook dinner\n')
            print('# delete - Delete task by id')
            print('task-cli delete 1\n')
            print('# mark-<status> - Mark task as in progress or done')
            print('task-cli mark-in-progress 1')
            print('task-cli mark-done 1\n')
            print('# list <status>- Listing all tasks by status')
            print('task-cli list')
            print('task-cli list done')
            print('task-cli list todo')
            print('task-cli list in-progress')
            exit(0)
        
        match self.command:
            case 'add':
                pass
            case 'list':
                if len(self.arguments) == 2 or self.arguments[2] not in ['done', 'todo', 'in-progress']:
                    exit('You give uncorrct status. You should to use done, todo, in-progress')                
            case _:
                if not self.arguments[2].isnumeric():
                    exit('You give uncorrect id. You should to use a number')
        
        self.command_arguments = self.arguments[2::]

    def get_command(self):
        if len(self.arguments) == 1:
            return None
        else:
            return self.arguments[1]
    
    def parse_cli(self):
        return self.command, self.command_arguments 
