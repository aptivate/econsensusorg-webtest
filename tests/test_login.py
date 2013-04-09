from pages.base import Login


def test_login(driver, server_credentials):
    # Login
    login = Login(driver, server_credentials)
    login.login_with_credentials()

    login.assert_is_logged_in()
    login.assert_is_logged_in()
