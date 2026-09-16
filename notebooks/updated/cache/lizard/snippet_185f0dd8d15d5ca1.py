def get_session(session, baseurl, config):
    if environ.get('HTTP_PROXY'):
        myProxy = environ.get('HTTP_PROXY')
        proxy = Proxy({'proxyType': ProxyType.MANUAL, 'httpProxy': myProxy,
            'ftpProxy': myProxy, 'sslProxy': myProxy, 'noProxy': ''})
    else:
        proxy = None
    if 'login' in config['DEFAULT']:
        login, password = credentials(config['DEFAULT']['login'])
    else:
        login, password = credentials()
    browser = webdriver.Firefox(proxy=proxy)
    browser.get(baseurl)
    browser.find_element_by_name('login').send_keys(login)
    browser.find_element_by_name('passwd').send_keys(password)
    cookie = {'PHPSESSID': browser.get_cookie('PHPSESSID')['value']}
    prof_session.cookies = requests.utils.cookiejar_from_dict(cookie)
    print('Please log using firefox')
    while True:
        try:
            browser.find_element_by_css_selector('select')
            break
        except:
            sleep(0.5)
    browser.close()
    set_sessid(cookie['PHPSESSID'])
    if not verify_session(session, baseurl):
        print('Cannot get a valid session, retry')
        get_session(session, baseurl, {'DEFAULT': {}})