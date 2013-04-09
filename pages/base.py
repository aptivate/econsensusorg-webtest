from contextlib import contextmanager
from selenium.common.exceptions import NoSuchElementException
import pytest


class Base:

    @contextmanager
    def assert_element_visible(self):
        try:
            yield
            self.driver.passed = True
        except (NoSuchElementException):
            self.driver.passed = False
            pytest.fail("Element Not Visible")


class Login(Base):

    def __init__(self, driver, server_credentials):
        self.driver = driver
        self.username = server_credentials['username']
        self.password = server_credentials['password']
        login_url = "/".join([self.driver.baseurl, 'accounts/login'])
        self.driver.get(login_url)

    def login_with_credentials(self):

        usernameinput = self.driver.find_element_by_name("username")
        passwordinput = self.driver.find_element_by_name("password")

        # Enter the credentials
        usernameinput.send_keys(self.username)
        passwordinput.send_keys(self.password)

        loginbutton = self.driver.find_element_by_class_name("button")
        loginbutton.click()

    def assert_is_logged_in(self):
        # Wait for Logout item to appear so you know you're logged in
        with self.assert_element_visible():
            logout_element = self.driver.find_element_by_partial_link_text('Logout')
        return self.driver.passed


class Organizations:

    def __init__(self, driver):
        self.driver = driver
        organizations_url = "/".join([self.driver.baseurl, 'organizations'])
        self.driver.get(organizations_url)

    def get_all_organizations_slugs(self):
        """
        Returns an array with the org slugs for the logged in user.
        (Well it should, but it doesn't, right now it just returns smurfs
        need to add class name to org list to make this easy).
        """
        return ['smurfs']
