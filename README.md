# A2_CSCI4140

Project needs python Flask, as well as flask_mysqldb to run

Python flask installation: https://flask.palletsprojects.com/en/2.2.x/installation/
* note: If command pip install Flask doesn't work, use python3 -m pip install Flask
* Install flask_mysqldb: pip install -U flask_mysqldb, if the command doesn't work, use python3 -m pip install flask_mysqldb

To run the program:

MACOS/Linux:
From the project folder, run "py -3 -m venv venv" to create a virtual env, then activate it with "$ . venv/bin/activate". After that, run command "$ pip install Flask" to install flask, pip install -U flask_mysqldb to install mysqldb extension, and run the file run.py to run the application, make sure the localhost database is online as well

Windows:
From the project folder, run "$ python3 -m venv venv" to create a virtual env, then activate it with "venv\Scripts\activate". After that, run command "python3 -m pip install Flask" to install flask, python3 -m pip install flask_mysqldb to install mysqldb extension, and run the file run.py to run the application, make sure the localhost database is online as well