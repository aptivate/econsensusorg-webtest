User Interface testing for econsensus
=====================================
These pytest-based user interface tests are invoked locally to use:

1. local selenium and Firefox to test against a local or hosted instance of 
econsensus, or 
1. saucelabs.com to test against a hosted version of econsensus 

We can therefore use them to test:
* a local instance of econsensus running via django dev server
* econsensus.stage.aptivate.org from a development machine
* econsensus.stage.aptivate.org via saucelabs (intended for
invocation by Jenkins)

Tests are currently only setup to run on Firefox. Edit conftest.py to change
this.

Setup
-----

    pip install pytest

If you want to run the tests locally, ensure you have Firefox installed and:

    pip install selenium

To run the tests
----------------

py.test [OPTIONS] [FILE...]

py.test will discover tests to run as described [here](
http://pytest.org/latest/goodpractises.html#test-discovery), or you can 
specify a list of directories and/or filenames to run a smaller set of tests.

The following OPTIONS are available:

--baseurl - location of econsensus (defaults to http://localhost:8000)

--username - econsensus username (defaults to "admin")

--password - econsensus password (defaults to "admin")

--sauce_username - saucelabs username, if using

--sauce_api - saucelabs api key, if using

--timeout - selenium implicit timeout (defaults to 30)

If you want to run tests locally against a local or remote instance of 
econsensus, you must have Firefox and selenium installed. Results will be 
reported via stdout.

Examples:

    py.test
    py.test tests/test_login.py
    py.test --password my_local_password_is_not_admin
    py.test --baseurl http://econsensus.stage.aptivate.org --password staging_password

If you want to run on saucelabs server against a hosted instance of econsensus, you'll need 
the username and api key for our saucelabs account (see the wiki). Results will 
be reported via stdout and on the [saucelabs dashboard](https://saucelabs.com/login), 
which will also include a video of each test run.

Examples:

    py.test --baseurl http://econsensus.stage.aptivate.org --username admin --password staging_password --sauce_username saucelabs_username --sauce_api saucelabs_api_key
    py.test --baseurl http://econsensus.stage.aptivate.org --username admin --password staging_password --sauce_username saucelabs_username --sauce_api saucelabs_api_key tests/test_login.py


Troubleshooting
---------------

If you get an optparse.OptionConflictError on 'baseurl', you probably have 
pytest-mozwebqa installed - you can check this by doing:

    pip freeze | grep pytest-mozwebqa

Try pip uninstalling it, and running the test again. If you still get the error, 
you'll need to delete the corresponding package file and directory. It seems 
that pip uninstall doesn't actually remove the files, just prevents importing 
them from python, and py.test must be getting round that somehow.
