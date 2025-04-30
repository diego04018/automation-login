## Features
Login automation test using the page : https://practicetestautomation.com/practice-test-login/
It will do 1 positive test and 2 negative tests

## Requirements
- Python 3.13.3 or newer
- Git
- pip (Python package manager)

## Installation
Follow the steps below to set up the project on your local machine:

### 1. Clone the Repository
git clone https://github.com/diego04018/automation-login.git

### 2. Install Dependencies
open a new terminar and execute the command
pip install -r requirements.txt

### 3. Execute the tests
open a new terminar and execute the command
pytest test --alluredir=allure-results

### 4. Check test reports
open a new terminar and execute the command
allure serve allure-results  
