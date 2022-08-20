# Test Documentation

## Unit tests

Unit testing is done with automated tests using Pytest. The UI is excluded from the coverage reports, and there are no unit tests for the UI.

### Running the tests

If it's your first time running the tests, make sure you have all the needed dependencies installed by running

`poetry install`

Run tests:

`poetry run invoke test`

Generate test coverage report:

`poetry run invoke coverage-report`


### Test Coverage

<img width="778" alt="Screenshot 2022-08-20 at 18 45 15" src="https://user-images.githubusercontent.com/32310572/185755337-7a8cbfa2-2310-4870-9f20-3394c8465b2d.png">


## Code quality

Code quality is monitored and measured with pylint. The configuration can be found in the [.pylintrc](https://github.com/picada/haikov/blob/main/.pylintrc) file. The UI and the tests are excluded from the style checks.

### Running the style checks

Install the needed dependendies (if not done before)

`poetry install`

Run style checks:

`poetry run invoke lint`

The current code quality score is  9.95/10.0. 

## Manual testing

The program has been tested manually with different kinds of input and settings. As there are no automatic unit tests for the UI, testing this part of the program lies heavily on manual testing. 

