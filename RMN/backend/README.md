# BACKEND

## To run the backend, cd into RMN/backend

## The first time, create the Python Virtual Environemnt (the venv-folder)
```
py -3 -m venv venv
```

## Start the Python Virtual Environement (everytime you fully restart the IDE)
```
venv\Scripts\activate
```

## The first time, run (requires Python 3.10 or older!)
```
pip install -r requirements.txt
```

## To start the backend server, run
```
flask --app app --debug run --port=5000
```
