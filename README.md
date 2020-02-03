### Lib
Folder contains basic actions - browser session and base test setup

#### Actions
Contains classes for basic navigation over page elements eg. waiting for elements nad element visibility etc.

From this folder only **[`Actions`](Actions/__init__.py)** class (from \__init\__.py) is imported to **BaseTestSetup** class.

#### BaseTestsSetup
Contains file with base class **[`BaseTestsSetup`](BaseTestsSetup/BaseTestSetup.py)** that allows to set session .
Has to be imported to basic class that sets tests for a particular product eg. ShareLink - **[`ShareLinkTestSetup`](EgnyteProducts/TestCases/ShareLink/Lib/ShareLinkTestSetup.py)**

#### DriverSession
Contains:
* class checking that **Driver** has all required paramters set.
* class **[`Driver`](DriverSession/Driver.py)**, that returns appropriate session of WebDriver based on given parameters.

### Installation

* Tests were written and tested on Linux system
* install python 3.8
* install needed libraries - pip install -r requirements.txt
* if needed instal Chrome version 79.0.3945.130 and coressponding Chromedriver

### Running tests
* This project contains 5 test cases

* Before launching tests ensure that you have provided all necessary data in **[`settings.py`](settings.py)**.

* To launch all tests - run **pytest** command in **(EgnyteProducts/TestCases/ShareLink/Test)** folder

* Run one test file  - run **pytest test_name.py** for eg. **pytest test_login.py** command in in **(EgnyteProducts/TestCases/ShareLink/Test)** folder

* Run one test case from test file - run **pytest test_name.py::TestClass::test_method** for eg. **pytest test_login.py::TestLogin::test_login_positive** command in **(EgnyteProducts/TestCases/ShareLink/Test)** folder