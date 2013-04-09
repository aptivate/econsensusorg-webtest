import pytest
from selenium import webdriver
import httplib
import base64
try:
    import json
except ImportError:
    import simplejson as json


def pytest_addoption(parser):
    parser.addoption("--baseurl",
                     action='store',
                     dest='baseurl',
                     default='http://localhost:8000',
                     help='url for the econsensus under test \
                     (default localhost:8000)')
    parser.addoption('--username',
                     action='store',
                     dest='username',
                     default='admin',
                     help='econsensus username (default admin)')
    parser.addoption('--password',
                     action='store',
                     dest='password',
                     default='admin',
                     help='econsensus password (default admin)')
    parser.addoption('--sauce_username',
                     action='store',
                     dest='sauce_username',
                     help='Supply username to run on saucelabs')
    parser.addoption('--sauce_api',
                     action='store',
                     dest='sauce_api',
                     help='Supply api key to run on saucelabs')
    parser.addoption('--timeout',
                     action='store',
                     dest='timeout',
                     default=30,
                     help='Selenium Implicit Wait value (default 30s)')


@pytest.fixture()
def driver(request):
    sauce_username = request.config.option.sauce_username
    sauce_api = request.config.option.sauce_api
    base64string = base64.encodestring('%s:%s' %
                                      (sauce_username, sauce_api))[:-1]

    def set_test_status(jobid, passed=True):
        body_content = json.dumps({"passed": passed})
        connection = httplib.HTTPConnection("saucelabs.com")
        connection.request('PUT',
                           '/rest/v1/%s/jobs/%s' % (sauce_username,
                                                    jobid),
                           body_content,
                           headers={"Authorization": "Basic %s" % base64string})
        result = connection.getresponse()
        return result.status == 200

    if sauce_username and sauce_api:
        caps = webdriver.DesiredCapabilities.FIREFOX
        caps['platform'] = "Linux"
        caps['version'] = "19"
        caps['name'] = 'Econsensus Test Suite on Firefox'
        command_executor = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub" % (sauce_username, sauce_api)
        driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor=command_executor
        )
    else:
        driver = webdriver.Firefox()

    driver.implicitly_wait(request.config.option.timeout)

    def tearDown():
        if sauce_username and sauce_api:
            if driver.passed:
                set_test_status(driver.session_id, passed=True)
            else:
                set_test_status(driver.session_id, passed=False)
            print("Link to your job: https://saucelabs.com/jobs/%s" % driver.session_id)
        driver.quit()
    request.addfinalizer(tearDown)

    driver.baseurl = request.config.option.baseurl
    return driver


@pytest.fixture()
def server_credentials(request):
    server_credentials = {}
    server_credentials['username'] = request.config.option.username
    server_credentials['password'] = request.config.option.password
    return server_credentials
