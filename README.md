# Description
### This app is a social media site in which users can post pictures but also the users can like, dislike, and comment on them.


## Screenshots

### Home Page

![Home Page](https://user-images.githubusercontent.com/58488936/138161354-a7ccfbe4-09dd-4d92-b6e4-07f30fa8c6bb.png)


### Item Details Page with user logged in

![User logged in](https://user-images.githubusercontent.com/58488936/138161384-7e4e2789-0833-4fc0-b040-e42d77039005.png)


### Item Details Page without user logged in

![User not logged in](https://user-images.githubusercontent.com/58488936/138161467-e645897d-8041-44a9-81fd-e34dd1b53372.png)


## Technologies
- HTML5
- CSS3
- Bootstrap 5
- Python 3
- Django 3.2.8
- Postgresql 14


## Requirements
- Git
- Python 3
- Django 3.2.8
- Postgresql 14


## Installation/Running the app
- Fork this repository.
- Clone your forked repository.
- Open up your terminal/command line to go to your cloned repository on your local machine.
- Type in ```pipenv shell``` to enter the environment shell.
- Then type ```pip install . ```  or ```pipenv install . ``` to get all the packages needed to run the server.
- Then type in ```psql``` to enter to your postgresql shell and type in ```\i settings.sql``` to get your database set up locally.
- Enter ```python manage.py migrate``` to get all the models for the database.
- Finally run ```python manage.py runserver``` and you will see that your server is going to be running.
- Open up your preferred browser and type in ```localhost:8000``` and you should be all set.


## Contribution
Feel free to create an issue, and/or send an email.
