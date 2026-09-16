def firefox(headless=True):
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options
    if headless:
        driver_key = 'headless'
        firefox_options = Options()
        firefox_options.add_argument('-headless')
    else:
        driver_key = 'headed'
        firefox_options = None
    if os.path.isdir(PROFILE_DIR):
        firefox_profile = webdriver.FirefoxProfile(PROFILE_DIR)
    else:
        firefox_profile = None
    if FIREFOX_INSTANCE[driver_key] is None:
        FIREFOX_INSTANCE[driver_key] = webdriver.Firefox(firefox_profile=
            firefox_profile, firefox_options=firefox_options)
    yield FIREFOX_INSTANCE[driver_key]