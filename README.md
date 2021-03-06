# Python + Selenium

This project has the objective of presenting the organization and code writting skills using Python and Selenium to write scenarios for login to Team Shift.

### Tools
  - VS Code
  - Python 3.x
  - Selenium
  - Firefox
  - Gecko Driver

### Instructions to execute tests
1. Clone the repository;
2. Install [Python 3.x](https://www.python.org/downloads/)
3. Open the command prompt and install the resources in requirements.txt file (found in the repository root) using the `pip install <package name>` command
4. Download the latest version of [Firefox](https://www.mozilla.org/pt-BR/firefox/new/) and [Geckodriver](https://github.com/mozilla/geckodriver/releases).
5. Put the executable file from geckodriver in any folder from PATH environment variable.
6. On the command prompt, type `pytest <path to repository root>\tests` to execute all the tests
7. To use chromedriver, put the executable in the same folder as the geckodriver executable file and change the browser name in the login_test.py file to `Chrome` on the class setup function.
