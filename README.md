# Page_Object_Framework_UI

The robotframework-PageObjectLibrary has been used for this project which is supported in python 3.

Tests\test_started.robot is the main test suite.It contains 2 test cases:
1. Verify details of getting started page
2. Verify that user can search.

##**Technology / Frameworks used:**

  1. python 3
  2. robotframework 3.1.2
  3. robotframework-seleniumlibrary 3.3.1
  4. robotframework-pageobjectlibrary 1.0.2
  5. selenium 3.141.0
  
##**Installation:**

`git clone git@github.com:BASNETANAMIKA/Page_Object_Framework_UI.git && cd Page_Object_Framework_UI`

`pip install -r requirements.txt`

##**How to Run tests:**

`Set PYTHONPATH=c:\\Python3\\DLLs;c:\\Python3\\Lib;c:\\Python3;c:\\Python3\\Lib\\site-packages;<path_to_project_directory>\\Modules;`

`robot --outputdir Logs\Latest --pythonpath resources tests/test_started.robot`
  
