# Super Simple Stocks

Tech Demo for a super simple stock system.

## Requirements

This project assumes that python 3.6+ is available on the system.

## Setup

First setup a virtual environment using your desired python version 
(must be greater or equal than 3.6). For example on a linux 
installation:

```sh
python3 -m venv ~/.venv
# or the following if python 3 is the default:
# python -m venv ~/.venv
source ~/.venv/bin/activate
```

You will then need to install the dependencies using `poetry install`. 

## Running Tests

The following runs all tests and outputs coverage information.
```sh
pytest --cov=super_simple_stocks tests
```

