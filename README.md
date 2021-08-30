[![codecov](https://codecov.io/gh/Derhks/DonRep/branch/main/graph/badge.svg?token=TSSVOG5SPC)](https://codecov.io/gh/Derhks/DonRep)

# DonRep
Application that shows on a map the movies that have been filmed in San Francisco.


## Table of Content

* [Development Environment Configuration](#development-environment-configuration)
* [Test the Application](#test-the-application)
* [Built With](#built-with)
* [Authors](#authors)


## Development Environment Configuration

Download the files from this repository.

```bash
git clone git@github.com:Derhks/DonRep.git
```

Create a virtual environment with Anaconda

```bash
conda create -n donrep_test python=3.8 -y
```

Now, let's activate the created virtual environment

```bash
conda activate donrep_test
```

With the virtual environment activated we are going to install
the requirements used in the project

```bash
pip3 install -r requirements.txt
```

We must export the environment variables that we need in our project.
Change the name of the `example.env` file to `.env`, fill in the
environment variables with their corresponding value and finally execute
the following command:

```bash
export $(cat .env | grep -v ^# | xargs)
```


### Run tests

The application has its unit tests, run the following command:

```bash
coverage run -m unittest discover
```

We can view the report with the command:

```bash
coverage report -m
```


### Run server

Finally, run the application server

```bash
python -m uvicorn main:app --reload --use-colors
```

or

```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

## Test the Application

### Develop

#### Locally

If you are running the project locally, visit the following link to test the application:

```bash
http://localhost:8000
```

### Production

See the following link for production testing of the application

```bash
https://donrep-test.herokuapp.com
```


## Built With

- [Python](https://www.python.org/) - Programming language
- [FastApi](https://fastapi.tiangolo.com) - Web framework
- [HTML](https://www.w3schools.com/html/) - Markup language
- [CSS](https://www.w3schools.com/css/) - Style language


## Authors
- **Julián Sandoval [derhks]** https://github.com/Derhks
