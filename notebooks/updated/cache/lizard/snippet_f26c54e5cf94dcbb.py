def login_password(self, value):
    password = self.selenium.find_element(*self._password_input_locator)
    password.clear()
    password.send_keys(value)