# Product Movement Tracker

Flask Application to track the movement of the product between multiple locations

## About Application
### Overview
Product Movement Tracker is a web-based application that keeps track of the movement of the product. In Retail businesses many times different products stored at different physical locations. This application will help them to track the products transactions between these locations

### Features
* **Product Management** - Create, Edit, Delete Products
* **Location Management** - Create, Edit, Delete Locations
* **Transactions Logger** - Create, Delete Product Movement Transactions
* **Report** - gives the overview of product quantities to the respective location


### Technologies Used
* Python - Programming Language
* Flask - Framework
* Jinja2 - Templating Engine
* SQLLite - Database
* Flask-SQLalchemy - SQL ORM

### Future Improvements
- [ ] Separate routes and models in a different modules
- [ ] Error Handling - Give proper user feedback if something goes wrong
- [ ] Feature: Add edit Product Movement feature


## Flask Application Structure 

- [ ] TODO: add folder structure

### Demo:
- [ ] TODO: Add Screenshots

---

## Development Setup
### Virtual Environment (optional)
Create an environment

```
$ python3 -m venv venv
```

Activate the environment

```
$ . venv/bin/activate
```

### Installation

Install with `pip`:

```
$ pip install -r requirements.txt
```

### Setting up environment variables
```
$ export FLASK_APP=product_movement_tracker.py
$ export FLASK_ENV=development
```

Alternatively, you can use `.flaskenv` file to preserve the env variables


### Run Flask Server
```
$ flask run
```
Make sure your virtual environment is active.
