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

## Repository Structure

```
super_simple_stocks - project source code
├── __init__.py -
├── exchange.py - Exchange class to cover 'Global Beverage Corporation Exchange' from assignment docs
├── model.py - Models used within this project for stocks and trades
├── trade_repository.py - Repository classes to store trades
└── utils.py - some helper functions for basic calculations

tests - unit tests
├── __init__.py
├── conftest.py - pytest additional config file (not in use for this project)
├── test_data.csv - test data based on the assignment doc
├── test_exchange.py - test code for exchange
├── test_model.py - test code for model
└── test_trade_repository.py - test code for trade repositories

```

## Running Tests

The following runs all tests and outputs coverage information.
```sh
pytest --cov=super_simple_stocks tests
```

The tests should also give a good idea about how to use the different
components in isolation.

## Basic Example tying it all together

A basic example which shows on a high level how all components can be
tied together is in `demo.py`. 

## Potential Improvements if this was a real project

1. Aside for unit tests, I tried to not use a wide variety on non-base
python libraries. A lot of the tasks in here can be performed better
and more performance using specialised libraries or tools. For example
while staying in python memory I could have used pandas/numpy to 
vectorise my operations (i.e. have them run in C) and to simplify tasks
like CSV loading. Given this is a demo of my skills this would not have
been very useful here. Also in a practical use case, having a trade
database for example, some of my code would have been moved to SQL.
2. Streaming is not explicitly dealt with here. There are libraries
like Apache Spark Structured streaming which could help to make 
calculations directly at the stream level. Again, no point for this
demo.


