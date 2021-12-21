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

### Screenshots
#### Home - Report
![image](https://user-images.githubusercontent.com/43115036/146883045-033ce56e-63dc-4fc3-af47-3c071b79c9fb.png)

#### Product Movements
![image](https://user-images.githubusercontent.com/43115036/146883251-187cfcb4-b24f-4717-964f-1a84008643cb.png)
![image](https://user-images.githubusercontent.com/43115036/146883219-3216e429-ecf7-431f-a7b7-179aab5c27ac.png)


#### Products
![image](https://user-images.githubusercontent.com/43115036/146883105-d2e57439-30a7-4d3b-a26b-0a453a840388.png)

#### Locations
![image](https://user-images.githubusercontent.com/43115036/146883147-a6c5d6d0-3de9-4b66-a35e-1030444a6ab9.png)





### Future Improvements
- [ ] Separate routes and models in a different modules
- [ ] Error Handling - Give proper user feedback if something goes wrong
- [ ] Feature: Add edit Product Movement feature

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
