from pages.login_page import LoginPage

def test_valid_login(driver):
    login = LoginPage(driver)
    login.load()
    login.enter_username("student")
    login.enter_password("Password123")
    login.click_login()
    assert login.get_success_message() == "Logged In Successfully"


def test_invalid_login_username(driver):
    login = LoginPage(driver)
    login.load()
    login.enter_username("wronguser")
    login.enter_password("Password123")
    login.click_login()
    assert "Your username is invalid!" in login.get_error_message()

def test_invalid_login_password(driver):
    login = LoginPage(driver)
    login.load()
    login.enter_username("student")
    login.enter_password("wrongpass")
    login.click_login()
    assert "Your password is invalid!" in login.get_error_message()