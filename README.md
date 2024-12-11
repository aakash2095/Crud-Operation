 # CRUD Operations using Django

This project explains how to perform **CRUD operations** (Create, Read, Update, Delete) in Django. CRUD helps you manage records in a database.

Features
- Add records (Create)
- View records (Read)
- Edit records (Update)
- Delete records (Delete)
- Simple design using Bootstrap

Technologies Used
- Django
- HTML/CSS with Bootstrap Framework

To Run the Project
   Follow these steps:

Install all the necessary thing that are require to run the Django 

Migrate the database : In Terminal
    python manage.py migrate

Run the Server:
    python manage.py runserver

To check the Admin panel :
    /admin
    username: root
    password: root

Main Files

crud_operation          Project Folder
|
|-- core/               Main App
|   |-- templates/      HTML Templates
|   |-- static/         CSS/JS Files
|   |-- forms.py        Forms for CRUD
|   |-- models.py       Database Models
|   |-- views.py        CRUD Logic
|   |-- urls.py         URL Configuration
|
|-- manage.py           Django Commands
|-- db.sqlite3          Database File
|-- requirements.txt    Dependencies

