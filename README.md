# Trading App

## About this project

"trading" is a mini-app which suggests the best times to buy and sell stocks for maximising profits from a given data set.

## Getting started

1. Clone this project locally.
2. Set up the virtual environment by running `make create-venv`.  
    This will install the required dependencies from the following places:  
        - trading/requirements.txt  
        - trading/requirements-dev.txt  
        - tests/requirements.txt  
    If there are issues with running this command,  
    then please modify the `PYTHON` variable and `create-venv` command in the Makefile.
3. Activate the newly created virtual environment.  
    Mac OS/Linux: `source .venv/bin/activate`  
    Windows: `.\venv\Scripts\activate`  
4. Run the application by running `make run`.

## Development notes

- This project follows the MVC design pattern - (Models were not required).
- The main app is in the trading/ directory.
- All data is the trading/data/ path.
- This project uses pre-commit git hooks and these are in .pre-commit-config.yaml.  
    You can install the hooks for the project by running `make install-lint`.
- Run `make help` for a list of commands related to the project.  
    The make commands will help you set up the virtual environment, run tests, lint the code, perform clean up and run the main app.

## Future improvement ideas (this will help make this a production level app)

- Benchmark tool to check for algorithm effeciency
- Utilise CI/CD
- Data source validation and sanisation (CSV could have invalid values, formatting, NaN, null values)
- Use logging
- Have user accounts and authentication
- Use error tracking tools (for AWS it would be CloudWatch)
- Use higher precision for price data type in pydantic (i.e. use double instead of float)
- Write tests for views and mock the user inputs.
- Allow for time periods which are not int (datetime as string or floats i.e. mins.seconds format)
- Serve this on the web or a GUI. Benefits of this include:
  - user can input data more easily
  - better user experience for trade recommendations (can have images and other aesthically pleasing output)
- Allow other file formats: json, xlsx, etc. Currently only allows csv.
