class LoginPage:
    textbox_username_name = "uid"
    textbox_password_name = "password"
    button_login_name = "btnLogin"
    link_logout_link_text = "Logout.php"

    def __init__(self, driver):
        self.driver = driver

    def setusername(self, username):
        self.driver.find_element_by_name(self.textbox_username_name).clear()
        self.driver.find_element_by_name(self.textbox_username_name).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element_by_name(self.textbox_password_name).clear()
        self.driver.find_element_by_name(self.textbox_password_name).send_keys(password)

    def clicklogin(self):
        self.driver.find_element_by_name(self.button_login_name).click()

    def clicklogout(self):
        self.driver.find_element_by_link_text(self.link_logout_link_text).click()
