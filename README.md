# L'Hopital Setup
Repository to hold setup instructions for lab 7.


- Download project as .zip and extract.
- Install [Python 2.7](https://www.python.org/downloads/release/python-2712/)
- Add Python and Python scripts to path variable, **no spaces**

![path](img/path.PNG)

- Install dependencies *run in cmd as admin in project folder*
```
pip install virtualenv virtualenvwrapper
virtualenv Hospital_ENV
venv\Scripts\activate
pip install -r requirements.txt
python setup.py build
python setup.py install
deactivate
```
- Install [PostgreSQL](https://www.postgresql.org/download/windows/)
- Make sure to install pgAdmin4 as well

### PostgreSQL Database Setup
- Follow the instruction [here](https://confluence.atlassian.com/display/CONF30/Database+Setup+for+PostgreSQL+on+Windows)
- When you are asked to create a password for the root user, make it **root**
- When creating a database, make sure to create a database with the following info

- open up pgAdmin4
- add new add new database
- enter in the configuration details

- Once you have created a database go to tools -> Query tool, use the Queries in db\schemas to create tables.

# PyCharm IDE Setup
- Download and install [PyCharm](https://www.jetbrains.com/pycharm/)

- To add your virtual environment as your interpreter, under File go to Settings.
- Click on 'Project Interpreter', click the gear icon next to the interpreter selector, click 'Add local'
- Browse to the location of your virtual environment, by default the location is
```
C:\Users\<Your User Name>\Envs\Hospital_ENV
```

# Run Project
- To run, click the green arrow button besides the dropdown used for configuration
