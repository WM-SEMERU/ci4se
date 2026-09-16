def _local_browser_class(browser_name):
    LOGGER.info('Using local browser: %s [Default is firefox]', browser_name)
    browser_class = BROWSERS.get(browser_name)
    headless = os.environ.get('BOKCHOY_HEADLESS', 'false').lower() == 'true'
    if browser_class is None:
        raise BrowserConfigError(
            'Invalid browser name {name}.  Options are: {options}'.format(
            name=browser_name, options=', '.join(list(BROWSERS.keys()))))
    else:
        if browser_name == 'firefox':
            log_path = os.path.join(os.getcwd(), 'geckodriver.log')
            if os.path.exists(log_path):
                os.remove(log_path)
            firefox_options = FirefoxOptions()
            firefox_options.log.level = 'trace'
            if headless:
                firefox_options.headless = True
            browser_args = []
            browser_kwargs = {'firefox_profile': _firefox_profile(),
                'options': firefox_options}
            firefox_path = os.environ.get('SELENIUM_FIREFOX_PATH')
            firefox_log = os.environ.get('SELENIUM_FIREFOX_LOG')
            if firefox_path and firefox_log:
                browser_kwargs.update({'firefox_binary': FirefoxBinary(
                    firefox_path=firefox_path, log_file=firefox_log)})
            elif firefox_path:
                browser_kwargs.update({'firefox_binary': FirefoxBinary(
                    firefox_path=firefox_path)})
            elif firefox_log:
                browser_kwargs.update({'firefox_binary': FirefoxBinary(
                    log_file=firefox_log)})
        elif browser_name == 'chrome':
            chrome_options = ChromeOptions()
            if headless:
                chrome_options.headless = True
            chrome_options.add_argument('--use-fake-device-for-media-stream')
            chrome_options.add_argument('--use-fake-ui-for-media-stream')
            browser_args = []
            browser_kwargs = {'options': chrome_options}
        else:
            browser_args, browser_kwargs = [], {}
        return browser_class, browser_args, browser_kwargs