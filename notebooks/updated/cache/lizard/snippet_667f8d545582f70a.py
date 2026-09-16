def _init_browser(self):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_experimental_option('prefs', {
        'profile.managed_default_content_settings.notifications': 1})
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.set_page_load_timeout(10)
    browser.implicitly_wait(1)
    browser.maximize_window()
    browser.get(settings.HARNESS_URL)
    self._browser = browser
    if not wait_until(lambda : 'Thread' in browser.title, 30):
        self.assertIn('Thread', browser.title)