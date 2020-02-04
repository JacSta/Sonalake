### Lib
Folder contains basic actions - browser session and base test setup

#### Actions
Contains classes for basic navigation over page elements eg. waiting for elements and element visibility etc.

From this folder only **[`Actions`](Lib/Actions/__init__.py)** class (from \__init\__.py) is imported to **BaseTestSetup** class.

#### BaseTestsSetup
Contains file with base class **[`BaseTestsSetup`](Lib/BaseTestsSetup/BaseTestSetup.py)** that allows to set session .
Has to be imported to basic class that sets tests for a particular product eg. Calculator - **[`CalculatorTestSetup`](TestCases/Calculator/Lib/CalculatorTestSetup.py)**

#### DriverSession
Contains:
* class checking that **Driver** has all required paramters set.
* class **[`Driver`](Lib/DriverSession/Driver.py)**, that returns appropriate session of WebDriver based on given parameters.

### Installation

* Tests were written and tested on Linux system
* install python 3.8
* install needed libraries - pip install -r requirements.txt
* if needed instal Chrome version 79.0.3945.130 and coressponding Chromedriver

### Running tests
* This project contains one test case

* Before launching tests ensure that you have provided all necessary data in **[`settings.py`](settings.py)**.

* To launch all tests - run **pytest** command in **(Sonalake/TestCases/Calculator/Test)** folder

* Run one test file  - run **pytest test_calculate.py** command in in **(Sonalake/TestCases/Calculator/Test)** folder
