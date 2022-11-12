# HTML web application with Flask(Python) and SQLite3

Use the Linux system provided by your instructor, or in VirtualBox. You can run this on any OS.

# Basic linux commands
Check current user
```
whoami 
```
Present working directory
```
ls
ls -la
```
Change directory
```
# change one directory up
cd ../
```
```
# change to a folder in the current directory
cd ./myfolder
```
# 1. Copy the project folder
```
git clone https://github.com/djengineer/flask-python3-starter-kit.git
```


# 2. Set up Python environment (Linux)

If you are using Anaconda for Python, Anaconda manages the virtual environments for us.

## 1. Change your directory to inside the flask kit
```
cd flask-python3-starter-kit
```
## 2. Create Python virtual environment
```
python3 -m venv env
```
The output folder, which we called "env" will be where a virtual Python is stored.
```
source env/bin/activate
```
You should see a (env) in the terminal now.
## Install the depencies
```
pip install -r requirements.txt
```
If you need to update the requirements after using pip install, you can use the following. Freeze will only output what is installed in the current environment.
```
pip freeze > requirements.txt
```
# 3. Run the Flask web application
Change the port number first.
```
python ./flask_app.py
```
# 4. Creating a new page.

Flask works by a templating engine called Jinja2.

1. Create/edit the menu layout
2. Create a new html file in the templates menu
3. Edit the flask_app.py to include the the routing for the URL.

Unlike normal PHP or plain HTML, we can have different names for the file and the URL.
