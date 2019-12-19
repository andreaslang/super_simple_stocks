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

