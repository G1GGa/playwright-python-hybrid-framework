from pages.login_page import LoginPage

def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.navigate()

    login_page.login("standard_user", "secret_sauce")

    assert "inventory.html" in page.url

def test_locked_out_user_login(page):
    login_page = LoginPage(page)
    login_page.navigate()

    login_page.login("locked_out_user", "secret_sauce")
    error_msg = login_page.get_error_message()
    assert "Epic sadface" in error_msg