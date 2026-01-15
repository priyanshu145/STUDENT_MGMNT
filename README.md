##Technologies Used
Python
Django
HTML
CSS
SQLite (default Django database)
Virtual Environment (venv)







### Commands Used


## to create a vertual envoirement
python -m venv venv  

## to activate venv
venv\Scripts\activate  

## to install djnago in venv
pip install django  

## to create a project
django-admin startproject project_name  

## go inside the project folder
cd project_name  

## to create an app
python manage.py startapp app_name  

## to run the project
python manage.py runserver




## to link with git

## hidden .git directory in project
git init   
git config --global user.name "Priyanshu Kushwaha"
git config --global user.email "priyanshukushwaha145@gmail.com"
## email should be same as github account
git add . 

git commit -m "Initial commit - STUDENT_MGMNT"
git remote add origin github-repo-url
git remote -v
git branch -M main
git push -u origin main


## making changes in file and then upload it again in github through git
git status
git add .
git commit -m "Massage"
git push


