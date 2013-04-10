from pages.base import Login


def test_login(driver, server_credentials):
    # Login
    login = Login(driver, server_credentials)
    # login_with_credentials method asserts to check if user is logged in
    login.login_with_credentials()
