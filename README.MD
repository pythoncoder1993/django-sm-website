Steps to run this project:

1. Create a directory using following command:

mkdir socialMediaWebsite

2. Go into this directory using following command:

cd socialMediaWebsite

3. Create virtual environment using following command:

python -m venv socialmediawebsiteVenv or python3 -m venv socialmediawebsiteVenv

4. Activate the environment created in step 3:

For mac users, source socialmediawebsiteVenv/bin/activate
For windows users, socialmediawebsiteVenv/Scripts/activate.ps1

5. Install django and pillow in this environment:

pip install django or pip3 install django
pip install pillow or pip3 install pillow

6. Copy the folder you downloaded in socialMediaWebsite folder

7. To create superuser: python manage.py createsuperuser

8. To run server: python manage.py runserver


Link Views and Templates,

* Create a view
* Add path related to view in urls.py
* Create template
* Link template with view

Models,

* Create models
* Register the model in admin.py
* Run makemigrations
* Run migrate

Create a view which require user login and that views should list down all the posts in the webiste