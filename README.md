# Todo App
This is a Django Todo app with models for BaseModel (with uid, created_at, and updated_at), Time (start/end time), and Todo (user, time, title, description, completion status). Built using ForeignKey relationships.

## Requirements
* Python 3.x
* Django 3.x
* Django Rest Framework

## Installation
1. Clone the repository <br>
``` git clone https://github.com/UsmanRepos/django-rest-frame-work-todo-app.git ``` <br><br>
2. Install the required packages <br>
``` pip install -r requirements.txt ``` <br><br>
3. Run migrations <br>
``` python manage.py migrate ``` <br><br>
4. Run the development server  
``` python manage.py runserver ``` <br><br>

# Models
## BaseModel
The BaseModel is an abstract model that serves as a base for other models in the app. It includes the following fields:
* uid: a unique identifier for the model instance, generated using the Python UUID library.
* created_at: the date when the model instance was created.
* updated_at: the date when the model instance was last updated.

## Time
The Time model represents the time period for which a Todo item is planned. It includes the following fields:
* time_id: a unique identifier for the model instance, generated as an auto-incrementing primary key.
* start_time: the start time of the todo.
* end_time: the end time of the todo.

## Todo
The Todo model represents a single Todo item. It includes the following fields:
* user: a ForeignKey to the Django User model, indicating the user who created the Todo item.
* time: a ForeignKey to the Time model, indicating the time period for which the Todo item is planned.
* todo_title: the title of the Todo item, with a maximum length of 100 characters.
* todo_description: a description of the Todo item.
* is_done: a Boolean field indicating whether the Todo item has been completed or not. 

# Serializers
## TodoSerializer
The TodoSerializer is the serializer for the Todo model and includes the following fields:
* id (AutoField) - a unique identifier for the plan
* todo_title (CharField) - the title of the todo
* todo_description (TextField) - a detailed description of the todo
* is_done (Boolean) - the status of the todo

## TimeSerializer
The TimeSerializer is the serializer for the Time model and includes the following fields:
* id (AutoField) - a unique identifier for the time
* start_time (CharField) - the time when todo start
* start_time (CharField) - the time when todo end

## Field-level validators
The project includes field-level validators to ensure that the data entered is valid. These validators check the special characters and length of the title and description fields to ensure that they do not exceed a specified length.

## Contributing
Contributions are welcome! If you would like to contribute to this project, you can start by forking the repository



