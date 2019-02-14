<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
</head>
<body>
    <h1>Documentation</h1>
    <p>Before install django make sure you have installed latest version of <b>python</b>, you can download from <a href="https://www.python.org/downloads/" target="_blank">here</a>.</p>
<h3>Let's begin Django installation</h3>
<nav>
    <ul>
        <li>Installing django on Virtual Environment </li>
        <h4>First setup virtual environment on your system as:</h4>
        <pre>C:\WINDOWS\system32>pip install virtualenvwrapper-win</pre>
        <h4>Make virtualenv where your project folder will exist: </h4>
        <p>C:\Users\subham\projects>mkvirtualenv py1</p>
        <p>Here, virtual environment named as py1 you can give any name as you want.</p>
        <h4>Install django on vitual environment</h4>
        <p>(py1)C:\Users\subham\projects>pip install django</p>
        <li>Set a project name inside 'projects' folder in this case</li>
        <h4>Set a project name</h4>
        <p>C:\Users\subham\projects>django-admin startproject projectname</p>
        <p>Here, you can give any name instead of 'projectname'</p>
        <h4>Working on py1 which is a virtual env we have made</h4>
        <p>C:\Users\subham\projects\projectname>workon py1</p>
        <p>(py1)C:\Users\subham\projects\projectname></p>
        <li>Check django working</li>
        <p>(py1)C:\Users\subham\projects\projectname>python manage.py runserver</p>
    </ul>
    <h4>Login to administrator</h4>
    <nav><ul>
        <li>Go to localhost http://127.0.0.1:8000/admin</li>
        <p>login from below ||</p>
        <li>Create admin login username and password</li>
        <p>(py1)C:\Users\subham\projects\projectname>python manage.py createsuperuser</p>
    </ul></nav>
</nav>
</body>
</html>
