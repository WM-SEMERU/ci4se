def wait_for_login(self, timeout=90):
    WebDriverWait(self.driver, timeout).until(EC.
        visibility_of_element_located((By.CSS_SELECTOR, self._SELECTORS[
        'mainPage'])))