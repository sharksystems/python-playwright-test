# python-playwright-test
https://sharksystems.github.io/python-playwright-test

## Summary

This repository contains automated tests for the [Automation Excercise](https://www.automationexercise.com/) website. The tests are written using the Playwright framework on Python

## Requirements

- Python 3
- Java - for Allure reports

## Steps to Install

1. Clone the repository or go to Code > Download ZIP
   
2. Set up environment and install dependencies:
   
 ```
 python -m pip install --upgrade pip
 pip install pipenv
 pipenv install --system
 playwright install
 ```
Note: In some cases if you have Python 3 installed on your system you may have to use the ```python3``` and ```pip3``` commands instead

## Running tests

```pytest```

Running on a specific browser:

```pytest --browser-name firefox```

```pytest --browser-name webkit```

## Generating a report

Reports are generated automatically after tests. View report:

```allure serve reports```