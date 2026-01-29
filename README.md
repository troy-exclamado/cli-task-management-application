# cli-task-management-application

## Prerequisites

- Python 3.14.2  
- MySQL server installed and running  
- `mysql-connector-python` package 

## Install requirements

Run `pip install -r requirements.txt`

## Update the database config

Go to database.py and add the config of your MySQL

## Migrate the table

Run `python main.py migrate` to setup the table 

## Start

Run `python main.py` to view the available commands

## Add task

Run `python main.py add --title="Your Titlte" --description="Your description" --due-date=2026-01-29 --priority="Pending"`
You can edit the value of the parameters on your liking

## Show all task

Run `python main.py list` to show the details of all saved task including their id

## Update task

Run `python main.py update {the task id} --status="In Progress"` to update its status

## Complete the task

Run `python main.py complete {the task id}` to complete the task

## Delete the task

Run `python main.py delete {the task id}` to delete the task

