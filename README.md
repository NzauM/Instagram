## @Moments.
# Author
[NzauM](https://github.com/NzauM/Galleria.git)

# Description
A mock up of the famous social media app Instagram 

# Setup Instructions:
Requirements
# 1. Clone the repository
* Clone the the repository by running

* git clone https://github.com/NzauM/Instagram.git
or download a zip file of the project from github

* Navigate to the project directory

* cd Galleria
# 2. Create a virtual environment
* Install Virtualenv
 pip install virtualenv
 
* To create a virtual environment named virtual, run
virtualenv virtual

* To activate the virtual environment we just created, run
source virtual/bin/activate

# 3. Create a database
* You'll need to create a new postgress database, Type the following command to access postgress

 * $ psql
  * Then run the following query to create a new database named gallery

# 4.create database instagram
# 5.Install dependencies
* To install the requirements from requirements.txt file,

  * pip install -r requirements.txt
# 6.Create Database migrations
* Making migrations on postgres using django

* python3 manage.py makemigrations gram
* then run the command below;

* python3 manage.py migrate
# 7.Run the app
* To run the application on your development machine,

* python3 manage.py runserver
# Running Tests
To run tests;
python3 manage.py test

# Technologies Used
This project was generated with
  * [Python](https://www.python.org/) version 3.8.0.
  * Django
  * Bootstrap.
  * javascript.
  * PSQL database.
  * HTML,CSS
# User stories
As a user of the application I should be able to:

*  Sign in to the application to start using.
 * Upload my pictures to the application.
* See my profile with all my pictures.
* Follow other users and see their pictures on my timeline.
* Like a picture and leave a comment on it.
# Bugs
There are no know bugs at the moment


# License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/NzauM/Instagram/blob/master/LICENSE)
MIT License
\_ **Nzau Mercy @2019**


# Collaboration Information
Clone the repository
Make changes and write tests
Push changes to github
Create a pull request
## Support and contact details
 For any issues ,contact at https://github.com/NzauM/Instagram/issues <br>
 Or for any pull requests, https://github.com/NzauM/Instagram/pulls
  Incase you need more clarification, feel free to send an email to: 
Email: mercywaenu16@gmail.com

