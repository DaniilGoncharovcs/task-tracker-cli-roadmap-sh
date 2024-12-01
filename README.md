# Task Tracker CLI
This repository containes an implementation of a Task Tracker CLI. The ide for the project was taken from [roadmap.sh](https://roadmap.sh/projects/task-tracker).

## Description

Call without arguments return description of each command:

```sh
./task-cli
```

### Supported commands:

- `./task-cli add description`  - Creates a new Task object with a description and saves as a json file in `json_tasks/`.
- `./task-cli update 1` - Creates a new Task instance and overwrites the old task file.
- `./task-cli delete 1` - Removes task file.
- `./task-cli list all|todo|in-progress|done` - Prints a list of tasks using a filter.
- `./task-cli mark-inprogress|mark-done 1` - Updates task status
