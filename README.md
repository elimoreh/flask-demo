

  

## Python Test

  

This repository is a demonstration of a Python Flask platform with a sqlite database along with a simple flask cache. The sqlite database is populated with data from Github's User API.

  

### Project Structure

--------

  

```sh

├── app/
│ ├── __init__.py
│ ├── cache.py
│ ├── routes/
│ │ ├── __init__.py
│ │ └── users.py
│ ├── static/
│ │ └── main.css
│ ├── store/
│ │ ├── __init__.py
│ │ ├── sql_helpers.py
│ │ └── users.py
│ ├── templates/
│ │ └── users.html
│ └── utils/
│ ├── __init__.py
│ └── users.py
├── README.md
├── requirements.txt
├── run.py
├── tests/
│ ├── conftest.py
│ ├── __init__.py.py
│ └── unit/
│ ├── seed.py
│ └── users.py
├── seed.py
├── .gitignore
```

  

### Screenshots

  ![Alt Text](https://media.giphy.com/media/1WcFmqwsv4cLFNzD9R/giphy.gif)  


### Quick Start

  ![Alt Text](https://media.giphy.com/media/pCa5zfdwtV122PL4lY/giphy.gif)

1. Clone the repo

```
$ git clone https://github.com/elimoreh/flask-demo

$ cd flask-demo
```

  

2. Initialize and activate a virtualenv:

```
$ python3 -m venv env

$ source env/bin/activate
```

  

3. Install the dependencies:

```
$ pip3 install -r requirements.txt
```

  

4. Seed the database

```
$ python seed.py
```

  

5. Run the development server:

```
$ python run.py
```

  

The default will add 25 users from the Github api. Add the `-t` or `--total`  along with the number of users you want the database to be populated with.

  

Navigate to [http://localhost:5000/users](http://localhost:500/users)

   

### API Guide

------

  

You may add a parameter or a combination of parameters to the url to get more tailored results.

  

The user fields are the following: `username`, `id`, `type`, `image_url`, `profile_url`

  

You may filter based on any combination of user fields. For example, if you want to filter based of `type`:

  

```
http://localhost:5000/users?type=User
```

  

You may also order by any user field. For example, if you want to order by `username`:

  

```
http://localhost:5000/users?order_by=id
```

  

Change the pagination size:

  

```
http://localhost:5000/users?pagination=100
```

  

The following are the default values if the parameters:

```
order_by: id
pagination: 25
page_number: 1
filters: None
```

  

### Testing

------

  

This demonstration has very simple testing at the moment. To run the test on the seeding cli and users route, run `pytest` in the root directory.

  

 ### Additional Notes

------

  
The application cannot be deployed on Heroku because of SQLite. SQLite runs in memory, and backs up its data store in files on disk. While this strategy works well for development, Heroku’s stack has an ephemeral filesystem. The contents will be cleared periodically. 

In a normal setting, sqlAlchemy would be a better choice for querying SQL. The platform uses raw sql queries to more clearly demonstrate proficiency in sql.

  

Github has a rate limiter, placing a limits on the API used for seeding. A rotation of account, and proper timeouts could be used to maximized the number of users in the db.


The caching system is flask-caching, essentially a simple python dictionary. In production, Redis would be a better caching system.

  

In production, the routes would send either be graphql responses or JSON responses. Due to the lack of front end, the routes send HTML templates.