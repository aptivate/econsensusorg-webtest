These selenium tests can be run against your local instance or against a hosted
version of econsensus. Use selenium locally or saucelabs (www.saucelabs.org).

Tests are currently only setup to run on Firefox. Edit conftest.py to change
this.

Setup
-----

    pip install pytest
    pip install selenium

To run the tests
----------------

The following options are available

--username (defaults to admin) - the username to login to econsensus with

--password (defaults to admin) - the password to login to econsensus with

--baseurl (defaults to http://localhost:8000) - location of econsensus

--sauce_username - if you wish to run tests on saucelabs, supply username

--sauce_api - if you wish to run tests on saucelabs, supple api key

--timeout (defaults to 30) - the selenium implicit timeout

Assuming you have firefox on your local machine, and want to run locally:

    py.test --username <username> --password <password>

To run on saucelabs server:

    py.test --username <username> -- password <password> --baseurl <econsensus url e.g. http://econsensus.stage.aptivate.org> --sauce_username <saucelabs_username> --sauce_api <saucelabs_api_key>

Troubleshooting
---------------

If you get an optparse.OptionConflictError on 'baseurl', you probably have pytest-mozwebqa installed - check this by doing:

    pip freeze | grep pytest-mozwebqa

Try pip uninstalling it, and running the test again. If you still get the error, delete the corresponding package file and directory (to find their location, pip install again, then import pytest-mozwebqa in a python session, and then call __path__ on it). It seems that pip uninstall doesn't actually remove the files, just prevents importing them from python, and py.test must be getting round that somehow.

